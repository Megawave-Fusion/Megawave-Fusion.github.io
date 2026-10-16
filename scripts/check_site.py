#!/usr/bin/env python3
"""Verify every generated link, source receipt, tag, and navigation edge."""
import hashlib
import json
import re
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


def check_knowledge_graph(site, tags, config, pages, errors):
    """Audit the published graph independently of the source graph builder.

    Only the leaf inventory is one-to-one with permanent tags. The root,
    chapters and sections are metadata for the UI's larger grouping neurons.
    """
    graph_path = site / 'data/knowledge-graph.json'
    if not graph_path.is_file():
        errors.append('Missing published knowledge graph')
        return {}
    try:
        graph = json.loads(graph_path.read_text())
    except (OSError, ValueError) as exc:
        errors.append('Unreadable published knowledge graph: ' + str(exc))
        return {}
    if not isinstance(graph, dict) or not all(isinstance(graph.get(key), list) for key in ('nodes', 'edges', 'chapters', 'sections', 'paths')):
        errors.append('Malformed published knowledge graph collections')
        return {}
    if any(not isinstance(item, dict) for key in ('nodes', 'edges', 'chapters', 'sections', 'paths') for item in graph[key]):
        errors.append('Malformed published knowledge graph record')
        return {}

    def inventory(items, label):
        result = {}
        for item in items:
            identifier = item.get('id')
            if not isinstance(identifier, str) or not identifier:
                errors.append(f'Missing {label} id')
            elif identifier in result:
                errors.append(f'Duplicate {label} id: {identifier}')
            else:
                result[identifier] = item
        return result

    def page_url(item, expected, label):
        if item.get('url') != expected:
            errors.append(f'Wrong {label} URL: {item.get("id")}')
        target = (site / expected.strip('/') / 'index.html').resolve()
        if target not in pages:
            errors.append(f'Missing {label} destination: {expected}')

    leaves = inventory(graph['nodes'], 'graph tag leaf')
    if len(graph['nodes']) != len(tags) or set(leaves) != set(tags):
        missing = ','.join(sorted(set(tags) - set(leaves)))
        extra = ','.join(sorted(set(leaves) - set(tags)))
        errors.append(f'Graph tag leaves differ from permanent tags (missing={missing}; extra={extra})')
    chapters = inventory(graph['chapters'], 'graph chapter')
    sections = inventory(graph['sections'], 'graph section')
    expected_chapters = {chapter['slug']: chapter for chapter in config['chapters']}
    expected_sections = {slug: chapter['slug'] for chapter in config['chapters'] for slug, _ in chapter['sections']}
    if set(chapters) != set(expected_chapters):
        errors.append('Graph chapter inventory differs from the site configuration')
    if set(sections) != set(expected_sections):
        errors.append('Graph section inventory differs from the site configuration')
    root = graph.get('root')
    if not isinstance(root, dict) or root.get('id') != 'fusion' or root.get('nodeType') != 'root' or not root.get('title'):
        errors.append('Invalid knowledge graph root')
    else:
        page_url(root, '/', 'graph root')
    for identifier, chapter in chapters.items():
        if chapter.get('nodeType') != 'chapter':
            errors.append('Invalid graph chapter node type: ' + identifier)
        page_url(chapter, f'/chapters/{identifier}/', 'graph chapter')
    for identifier, section in sections.items():
        if section.get('nodeType') != 'section' or section.get('chapter') not in chapters:
            errors.append('Invalid graph section parent or type: ' + identifier)
        if section.get('chapter') != expected_sections.get(identifier):
            errors.append('Graph section belongs to the wrong chapter: ' + identifier)
        page_url(section, f'/sections/{identifier}/', 'graph section')
    for identifier, node in leaves.items():
        if identifier not in tags:
            continue
        page_url(node, tags[identifier]['url'], 'graph tag leaf')
        if node.get('title') != tags[identifier]['title']:
            errors.append('Graph tag title differs from permanent entry: ' + identifier)
        section = sections.get(node.get('section'))
        chapter = chapters.get(node.get('chapter'))
        if not section or not chapter or section.get('chapter') != node.get('chapter'):
            errors.append('Graph tag has an invalid section/chapter membership: ' + identifier)
        elif node.get('sectionTitle') != section.get('title') or node.get('chapterTitle') != chapter.get('title'):
            errors.append('Graph tag hierarchy titles are inconsistent: ' + identifier)

    prerequisites = set()
    seen_edges = set()
    successors = {identifier: [] for identifier in leaves}
    indegrees = {identifier: 0 for identifier in leaves}
    for edge in graph['edges']:
        source, target, kind = edge.get('source'), edge.get('target'), edge.get('type')
        if not isinstance(source, str) or not isinstance(target, str) or source not in leaves or target not in leaves:
            errors.append(f'Graph relation has an invalid tag endpoint: {source} -> {target}')
            continue
        if source == target or kind not in ('prerequisite', 'related'):
            errors.append(f'Invalid graph relation: {source} -> {target}')
            continue
        if not isinstance(edge.get('reason'), str) or not edge['reason'].strip():
            errors.append(f'Missing graph relation explanation: {source} -> {target}')
        pair = tuple(sorted((source, target))) if kind == 'related' else (source, target)
        key = (kind, *pair)
        if key in seen_edges:
            errors.append(f'Duplicate graph relation: {source} -> {target}')
            continue
        seen_edges.add(key)
        if kind == 'prerequisite':
            prerequisites.add(pair)
            successors[source].append(target)
            indegrees[target] += 1
    queue = deque(identifier for identifier, degree in indegrees.items() if degree == 0)
    visited = 0
    while queue:
        current = queue.popleft()
        visited += 1
        for following in successors[current]:
            indegrees[following] -= 1
            if indegrees[following] == 0:
                queue.append(following)
    if visited != len(leaves):
        errors.append('Published graph prerequisite relations contain a cycle')
    paths = inventory(graph['paths'], 'graph learning path')
    for identifier, path in paths.items():
        sequence = path.get('nodes')
        if not isinstance(sequence, list) or len(sequence) < 2 or any(not isinstance(node, str) for node in sequence):
            errors.append('Invalid graph learning path sequence: ' + identifier)
            continue
        if len(sequence) != len(set(sequence)) or set(sequence) - set(leaves):
            errors.append('Graph learning path has repeated or unknown tags: ' + identifier)
        if any(pair not in prerequisites for pair in zip(sequence, sequence[1:])):
            errors.append('Graph learning path lacks an adjacent prerequisite edge: ' + identifier)
    return {'tag_leaves': len(leaves), 'chapters': len(chapters), 'sections': len(sections),
            'relations': len(graph['edges']), 'learning_paths': len(paths)}


def check(site):
    errors = []
    pages = {}
    for path in sorted(site.rglob('*.html')):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        ids = [n['id'] for n in soup.find_all(id=True)]
        if len(ids) != len(set(ids)):
            errors.append(f'Duplicate HTML id: {path.relative_to(site)}')
        # Broken Markdown table delimiters can silently drop formula content.
        for block in soup.select('.prose'):
            copy = BeautifulSoup(str(block), 'html.parser')
            for node in copy.select('.arithmatex, code, pre'):
                node.decompose()
            if '$' in copy.get_text():
                errors.append(f'Unrendered math delimiter in {path.relative_to(site)}')
        for table in soup.select('.prose table'):
            width = len(table.select('thead tr th'))
            if width and any(len(row.find_all(['td', 'th'], recursive=False)) != width for row in table.select('tbody tr')):
                errors.append(f'Inconsistent table columns: {path.relative_to(site)}')
        pages[path.resolve()] = (soup, set(ids))
        if not soup.select_one('main#main') or not soup.title:
            errors.append(f'Missing page structure: {path}')
    links = 0
    for path, (soup, _) in pages.items():
        for element in soup.select('[href], [src]'):
            value = element.get('href') or element.get('src')
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            links += 1
            target = (site / unquote(url.path.lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)) if url.path else path
            if target.is_dir() or url.path.endswith('/'):
                target = target / 'index.html'
            target = target.resolve()
            if not target.is_relative_to(site.resolve()) or not target.exists():
                errors.append(f'Broken link in {path.relative_to(site)}: {value}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target][1]:
                errors.append(f'Broken fragment in {path.relative_to(site)}: {value}')
    tags = json.loads((site / 'tags.json').read_text())
    registry = json.loads((ROOT / 'site/tags.json').read_text())
    if set(tags) != {v['tag'] for v in registry.values()}:
        errors.append('Tag export differs from permanent registry')
    index = json.loads((site / 'search-index.json').read_text())
    for tag, entry in tags.items():
        file = (site / entry['url'].strip('/') / 'index.html').resolve()
        if file not in pages:
            errors.append('Missing permanent page: ' + tag)
            continue
        if sum(r.get('tag') == tag for r in index) != 1:
            errors.append('Entry missing or duplicated in search: ' + tag)
        if entry['title'] not in pages[file][0].get_text():
            errors.append('Entry heading missing from page: ' + tag)
    nav = json.loads((site / 'navigation.json').read_text())
    if len({p['url'] for p in nav}) != len(nav):
        errors.append('Duplicate page in reading sequence')
    for i, item in enumerate(nav):
        path = (site / item['url'].strip('/') / 'index.html').resolve()
        soup = pages[path][0]
        # Home has its own entry action; every other reading page has reciprocal links.
        if i == 0:
            continue
        previous = soup.select_one('.reader-nav .previous')
        following = soup.select_one('.reader-nav .next')
        if previous is None or previous['href'] != nav[i-1]['url']:
            errors.append('Wrong previous page: ' + item['url'])
        if i+1 < len(nav) and (following is None or following['href'] != nav[i+1]['url']):
            errors.append('Wrong next page: ' + item['url'])
    receipt = json.loads((site / 'edition.json').read_text())
    for source, expected in receipt['source_files'].items():
        actual = hashlib.sha256((ROOT / source).read_bytes()).hexdigest()
        if expected != actual:
            errors.append('Stale source receipt: ' + source)
    config = json.loads((ROOT / 'site/site.json').read_text())
    graph_report = check_knowledge_graph(site, tags, config, pages, errors)
    for chapter in config['chapters']:
        for slug, source in chapter['sections']:
            headings = re.findall(r'^## (.+)$', (ROOT / source).read_text(), re.M)
            keys = [source + '#' + heading for heading in headings]
            section_page = pages[(site / f'sections/{slug}/index.html').resolve()][0]
            if len(section_page.select('.entry-block')) != len(keys):
                errors.append('Incomplete continuous section: ' + source)
            for key in keys:
                if key not in registry or not section_page.select_one('#' + registry[key]['tag']):
                    errors.append('Missing source heading: ' + key)
    if len(index) != len({r['url'] for r in index}):
        errors.append('Duplicate search destinations')
    if errors:
        raise SystemExit('\n'.join(errors))
    report = {'pages': len(pages), 'local_links': links, 'tags': len(tags), 'search_records': len(index),
              'source_files': len(receipt['source_files']), 'reading_pages': len(nav),
              'knowledge_graph': graph_report, 'result': 'passed'}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '_site'
    check(ROOT / target)
