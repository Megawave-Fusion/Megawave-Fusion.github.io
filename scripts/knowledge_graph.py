"""Build a complete entry inventory with explicitly curated learning relations.

The graph is a reading aid.  Its arrows are editorial recommendations, not a
claim that the corpus has a complete, strict scientific dependency structure.
"""
from __future__ import annotations

from collections import deque
import re

import markdown
from bs4 import BeautifulSoup


CHAPTER_COLORS = (
    '#1b7895', '#7973b4', '#d27a32', '#76833d', '#b45b79',
    '#4a83bb', '#957148', '#4d917d', '#8b6d9c', '#6c8292',
)


def summarize(text, limit=180):
    """Keep a short source-derived preview without exposing raw TeX."""
    paragraphs = re.split(r'\n\s*\n', text.strip())
    first = next((p for p in paragraphs if p.strip() and not p.lstrip().startswith(('$$', '\\[', '#', '|'))), text)
    first = re.sub(r'\$\$.*?\$\$|\\\[.*?\\\]', '〔公式见正文〕', first, flags=re.S)
    first = re.sub(r'(?<!\\)\$[^$\n]+\$|\\\(.*?\\\)', '〔公式见正文〕', first, flags=re.S)
    plain = BeautifulSoup(markdown.markdown(first, extensions=['tables']), 'html.parser').get_text(' ', strip=True)
    plain = re.sub(r'\s+', ' ', plain)
    plain = plain or '详细定义、适用条件与来源见本条目正文。'
    return plain if len(plain) <= limit else plain[:limit].rstrip('，；： ') + '…'


def validate_graph(graph):
    """Reject dangling/duplicate relations, cycles, and broken curated paths."""
    if graph.get('version') != 1:
        raise ValueError('Unsupported knowledge graph version')
    root = graph.get('root')
    if not isinstance(root, dict) or root.get('id') != 'fusion' or root.get('nodeType') != 'root' or root.get('url') != '/' or not root.get('title'):
        raise ValueError('Knowledge graph needs its global fusion root')
    nodes = graph.get('nodes', [])
    ids = [node['id'] for node in nodes]
    known = set(ids)
    if len(known) != len(ids):
        raise ValueError('Duplicate knowledge graph node')
    chapters = graph.get('chapters', [])
    chapter_ids = {chapter['id'] for chapter in chapters}
    if len(chapter_ids) != len(chapters):
        raise ValueError('Duplicate knowledge graph chapter')
    chapter_map = {chapter['id']: chapter for chapter in chapters}
    for chapter in chapters:
        if chapter.get('nodeType') != 'chapter' or chapter.get('url') != f'/chapters/{chapter["id"]}/':
            raise ValueError('Invalid knowledge graph chapter metadata')
    sections = graph.get('sections', [])
    section_map = {section['id']: section for section in sections}
    if len(section_map) != len(sections):
        raise ValueError('Duplicate knowledge graph section')
    for section in sections:
        if section.get('chapter') not in chapter_ids:
            raise ValueError('Unknown chapter for graph section: ' + section['id'])
        if section.get('nodeType') != 'section' or section.get('url') != f'/sections/{section["id"]}/':
            raise ValueError('Invalid knowledge graph section metadata')
        if not all(isinstance(section.get(key), str) and section[key] for key in ('title', 'description')):
            raise ValueError('Incomplete knowledge graph section: ' + section['id'])
    if {section['chapter'] for section in sections} != chapter_ids:
        raise ValueError('Every graph chapter must contain its registered sections')
    for node in nodes:
        if node['chapter'] not in chapter_ids:
            raise ValueError('Unknown graph chapter: ' + node['id'])
        if node.get('section') not in section_map:
            raise ValueError('Unknown graph section: ' + node['id'])
        section = section_map[node['section']]
        if section['chapter'] != node['chapter']:
            raise ValueError('Graph entry and section disagree on chapter: ' + node['id'])
        if node.get('chapterTitle') != chapter_map[node['chapter']]['title'] or node.get('sectionTitle') != section['title']:
            raise ValueError('Graph entry has inconsistent hierarchy titles: ' + node['id'])
        if not re.fullmatch(r'MF\d{6}', node['id']) or node['url'] != f'/tag/{node["id"]}/':
            raise ValueError('Graph node must use its permanent tag and URL')
        if not all(isinstance(node.get(key), str) and node[key] for key in ('title', 'chapterTitle', 'section', 'sectionTitle', 'summary', 'status')):
            raise ValueError('Incomplete graph node: ' + node['id'])
    if {node['section'] for node in nodes} != set(section_map):
        raise ValueError('Graph section inventory does not match its entry membership')
    seen, prerequisites = set(), set()
    children = {node_id: [] for node_id in ids}
    indegree = {node_id: 0 for node_id in ids}
    for edge in graph.get('edges', []):
        source, target, kind = edge['source'], edge['target'], edge['type']
        if source not in known or target not in known:
            raise ValueError(f'Dangling knowledge graph edge: {source} -> {target}')
        if source == target or kind not in ('prerequisite', 'related'):
            raise ValueError(f'Invalid knowledge graph edge: {source} -> {target}')
        if not isinstance(edge.get('reason'), str) or not edge['reason'].strip():
            raise ValueError('Knowledge graph edge needs an editorial reason')
        pair = (source, target) if kind == 'prerequisite' else tuple(sorted((source, target)))
        key = (kind, *pair)
        if key in seen:
            raise ValueError(f'Duplicate knowledge graph edge: {source} -> {target}')
        seen.add(key)
        if kind == 'prerequisite':
            prerequisites.add((source, target))
            children[source].append(target)
            indegree[target] += 1
    queue = deque(node_id for node_id, count in indegree.items() if count == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for target in children[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if visited != len(ids):
        raise ValueError('Prerequisite graph contains a cycle')
    path_ids = set()
    for path in graph.get('paths', []):
        if not path.get('id') or path['id'] in path_ids:
            raise ValueError('Missing or duplicate knowledge path id')
        path_ids.add(path['id'])
        sequence = path.get('nodes', [])
        if len(sequence) < 2 or len(sequence) != len(set(sequence)) or set(sequence) - known:
            raise ValueError('Invalid knowledge path: ' + path['id'])
        if any(pair not in prerequisites for pair in zip(sequence, sequence[1:])):
            raise ValueError('Knowledge path lacks an explicit prerequisite edge: ' + path['id'])
    return graph


def build_graph(chapters, entries, relations, status_label=None):
    """Use every registered entry; curated edges never control node inclusion."""
    if relations.get('version') != 1 or not isinstance(relations.get('note'), str) or not relations['note'].strip():
        raise ValueError('Knowledge relation source needs version 1 and its editorial note')
    nodes = []
    for entry in entries:
        section = entry['section']
        chapter = section['chapter']
        node = dict(
            id=entry['tag'], title=entry['title'], chapter=chapter['slug'],
            chapterTitle=chapter['title'], section=section['slug'],
            sectionTitle=section['title'], url=entry['url'],
            summary=summarize(entry['markdown']), status=entry['status'],
        )
        if status_label:
            node['statusLabel'] = status_label(entry)
        nodes.append(node)
    graph = dict(
        version=1, note=relations['note'],
        root=dict(id='fusion', title='聚变知识库', url='/', nodeType='root'),
        chapters=[dict(id=c['slug'], title=c['title'], url=c['url'],
                       description=c['description'], nodeType='chapter',
                       color=CHAPTER_COLORS[i % len(CHAPTER_COLORS)]) for i, c in enumerate(chapters)],
        sections=[dict(id=s['slug'], title=s['title'], url=s['url'],
                       chapter=c['slug'], description=summarize(s['intro']), nodeType='section')
                  for c in chapters for s in c['sections']],
        nodes=nodes, edges=relations['edges'], paths=relations['paths'],
    )
    validate_graph(graph)
    return graph
