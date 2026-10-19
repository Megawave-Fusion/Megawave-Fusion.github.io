#!/usr/bin/env python3
"""Build the entire reading edition from the registered Markdown sources."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
import markdown
from bs4 import BeautifulSoup

try:
    from .knowledge_graph import build_graph
except ImportError:  # Direct invocation: python scripts/build.py.
    from knowledge_graph import build_graph

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'site/site.json').read_text())
REGISTRY = ROOT / 'site/tags.json'
REPO = 'https://github.com/' + CONFIG['repository']
ESC = html.escape


def json_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_revision():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()


def split_source(path):
    text = (ROOT / path).read_text()
    title = re.match(r'^# (.+)\n', text)
    if not title:
        raise ValueError(f'Missing source title: {path}')
    parts = re.split(r'^## (.+)\n', text[title.end():], flags=re.M)
    entries = [(parts[i].strip(), parts[i+1].strip()) for i in range(1, len(parts), 2)]
    if len({title for title, _ in entries}) != len(entries):
        raise ValueError(f'Duplicate section heading in {path}')
    return title[1], parts[0].strip(), entries


def prepare_content(register=False):
    registry = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}
    used = set()
    tags = [v['tag'] for v in registry.values()]
    if len(tags) != len(set(tags)):
        raise ValueError('Permanent tag collision')
    counter = max([int(t[2:]) for t in tags] or [0])
    chapters, sections, entries = [], [], []
    for ci, raw in enumerate(CONFIG['chapters'], 1):
        chapter = dict(raw, number=ci, url=f'/chapters/{raw["slug"]}/')
        chapter['sections'] = []
        for si, (slug, path) in enumerate(raw['sections'], 1):
            title, intro, parts = split_source(path)
            section = dict(slug=slug, source=path, title=title, intro=intro, chapter=chapter,
                           number=f'{ci}.{si}', url=f'/sections/{slug}/', entries=[])
            for ei, (heading, content) in enumerate(parts, 1):
                key = path + '#' + heading
                used.add(key)
                if key not in registry:
                    if not register:
                        raise ValueError(f'Unregistered heading: {key}. Run build.py --register-tags once.')
                    counter += 1
                    registry[key] = {'tag': f'MF{counter:06d}', 'status': 'draft', 'kind': '专题'}
                record = registry[key]
                # No automatic promotion from draft to reviewed.
                if record['status'] not in ('draft', 'reviewing', 'reviewed', 'archived'):
                    raise ValueError('Unknown review status: ' + key)
                entry = dict(record, title=heading, markdown=content, section=section,
                             number=f'{ci}.{si}.{ei}', url=f'/tag/{record["tag"]}/', source=path)
                section['entries'].append(entry)
                entries.append(entry)
            chapter['sections'].append(section)
            sections.append(section)
        chapters.append(chapter)
    stale = set(registry) - used
    if stale:
        raise ValueError('Registered headings disappeared; migrate their keys, retaining tags: ' + ', '.join(sorted(stale)))
    if register:
        json_write(REGISTRY, registry)
    return chapters, sections, entries


class Builder:
    def __init__(self, output, register):
        self.out = output
        self.chapters, self.sections, self.entries = prepare_content(register)
        self.paths = {s['source']: s['url'] for s in self.sections}
        self.paths.update({'README.md': '/about/', '编写说明.md': '/contributing/',
                           '网站维护.md': '/maintenance/', '核验记录.md': '/verification/',
                           'site/verification.json': '/data/verification.json', '文献资料/来源索引.json': '/data/sources.json',
                           'site/assets/vendor/three/LICENSE': '/assets/vendor/three/LICENSE',
                           'site/assets/vendor/three/provenance.json': '/assets/vendor/three/provenance.json'})
        self.verification = json.loads((ROOT / 'site/verification.json').read_text())
        self.checked_sources = {p for p, h in self.verification.get('source_sha256', {}).items() if (ROOT / p).is_file() and digest(ROOT / p) == h}
        self.graph = build_graph(self.chapters, self.entries,
                                 json.loads((ROOT / 'site/knowledge-relations.json').read_text()), self.status)
        registered_tags = {record['tag'] for record in json.loads(REGISTRY.read_text()).values()}
        if {node['id'] for node in self.graph['nodes']} != registered_tags:
            raise ValueError('Knowledge graph must contain exactly one node per permanent tag')
        self.search = []
        self.pages = []
        self.sequence = [{'url': '/', 'title': CONFIG['title']}]
        for chapter in self.chapters:
            if len(chapter['sections']) > 1:
                self.sequence.append(chapter)
            for section in chapter['sections']:
                self.sequence.append(section)
                self.sequence.extend(section['entries'])
        self.revision = source_revision()
        self.references = json.loads((ROOT / '文献资料/来源索引.json').read_text())
        self.versions = {name: digest(ROOT / 'site/assets' / name)[:10]
                         for name in ('site.css', 'site.mjs', 'math-config.js', 'knowledge-tree.css',
                                      'knowledge-3d.css', 'knowledge-tree.mjs')}
        self.graph_modules = {}
        module_versions = {}
        # Rewrite dependencies before hashing their importers, so changes in the
        # shared core also invalidate the 3D layout and main UI module versions.
        for module in ('knowledge-core.mjs', 'knowledge-3d-layout.mjs', 'knowledge-3d.mjs', 'knowledge-tree.mjs'):
            content = (ROOT / 'site/assets' / module).read_text()
            for dependency, version in module_versions.items():
                content = content.replace(f"'./{dependency}'", f"'./{dependency}?v={version}'")
            self.graph_modules[module] = content
            module_versions[module] = hashlib.sha256(content.encode()).hexdigest()[:10]
        self.versions['knowledge-tree.mjs'] = module_versions['knowledge-tree.mjs']

    def render(self, text, source):
        rendered = markdown.markdown(text, extensions=['tables', 'fenced_code', 'footnotes', 'pymdownx.arithmatex'],
                                     extension_configs={'pymdownx.arithmatex': {'generic': True}})
        soup = BeautifulSoup(rendered, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (ROOT / source).parent / unquote(parsed.path)
            target = target.resolve()
            if not target.is_relative_to(ROOT):
                raise ValueError('Source link escapes repository: ' + href)
            relative = target.relative_to(ROOT).as_posix()
            if relative not in self.paths:
                raise ValueError(f'Unregistered source link: {source} -> {relative}')
            link['href'] = self.paths[relative] + ('#' + parsed.fragment if parsed.fragment else '')
        for table in soup.find_all('table'):
            wrapper = soup.new_tag('div', attrs={'class': 'table-wrap', 'tabindex': '0', 'role': 'region', 'aria-label': '表格，可横向滚动'})
            table.wrap(wrapper)
        for heading in soup.find_all(['h2', 'h3', 'h4']):
            heading['id'] = heading.get('id') or heading.get_text().strip().lower().replace(' ', '-')
        return str(soup)

    def chapter_links(self, current=''):
        return ''.join(f'<a class="{"active" if c["slug"] == current else ""}" href="{c["sections"][0]["url"] if len(c["sections"]) == 1 else c["url"]}"><span>{c["number"]:02}</span>{ESC(c["title"])}</a>' for c in self.chapters)

    def nav(self, url, bottom=False):
        indices = {p['url']: i for i, p in enumerate(self.sequence)}
        if url not in indices:
            return ''
        i = indices[url]
        previous = self.sequence[i-1] if i else None
        following = self.sequence[i+1] if i+1 < len(self.sequence) else None
        link = lambda p, direction: f'<a class="{direction}" href="{p["url"]}"><small>{"← 上一页" if direction == "previous" else "下一页 →"}</small>{ESC(p["title"])}</a>' if p else ''
        return f'<nav class="reader-nav {"bottom" if bottom else ""}" aria-label="阅读顺序">{link(previous,"previous")}{link(following,"next")}</nav>'

    def page(self, url, title, body, chapter=None, breadcrumbs=None, math=False, reader=True, description='', full_width=False, styles=(), modules=()):
        canonical = CONFIG['url'] + url
        current = chapter['slug'] if chapter else ''
        crumbs = [('/', '首页')] + (breadcrumbs or [])
        breadcrumb = '<span>/</span>'.join(f'<a href="{u}">{ESC(t)}</a>' for u, t in crumbs)
        if url != '/':
            breadcrumb += f'<span>/</span><span>{ESC(title)}</span>'
        css = self.versions['site.css']
        js = self.versions['site.mjs']
        math_scripts = f'<script src="/assets/math-config.js?v={self.versions["math-config.js"]}"></script><script defer src="/assets/mathjax/tex-chtml.js"></script>' if math else ''
        extra_assets = ''.join(f'<link rel="stylesheet" href="/assets/{name}?v={self.versions[name]}">' for name in styles)
        extra_assets += ''.join(f'<script type="module" src="/assets/{name}?v={self.versions[name]}"></script>' for name in modules)
        body_class = ' class="knowledge-tree-page"' if full_width else ''
        show_sidebar = chapter is not None and not full_width
        layout_class = 'layout knowledge-tree-layout' if full_width else 'layout' if show_sidebar else 'layout layout-overview'
        main_class = ' class="knowledge-tree-main"' if full_width else ''
        sidebar = f'<aside class="sidebar"><div class="sidebar-title">章节</div><nav aria-label="章节目录">{self.chapter_links(current)}</nav></aside>' if show_sidebar else ''
        mobile_nav = f'<details class="mobile-nav"><summary>切换章节</summary><nav>{self.chapter_links(current)}</nav></details>' if show_sidebar else ''
        breadcrumb_html = f'<div class="breadcrumb"><div>{breadcrumb}</div></div>' if url != '/' else ''
        text = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{ESC(title)} · Fusion Stacks</title><meta name="description" content="{ESC(description or '曦融兆波聚变知识库：基础原理、装置路线、辅助加热、材料、诊断、仿真与工程。')}">
<meta name="theme-color" content="#123c54"><meta property="og:title" content="{ESC(title)} · Fusion Stacks"><meta property="og:description" content="{ESC(description or CONFIG['title'])}"><meta property="og:url" content="{canonical}"><meta property="og:type" content="article">
<link rel="canonical" href="{canonical}"><link rel="icon" href="/assets/fusion.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css?v={css}"><script type="module" src="/assets/site.mjs?v={js}"></script>{math_scripts}{extra_assets}</head>
<body{body_class}><a class="skip" href="#main">跳转到正文</a><header class="masthead"><div class="topbar"><a class="brand" href="/"><img src="/assets/fusion.svg" alt="" width="43" height="43"><span><strong>Fusion Stacks</strong><small>曦融兆波 · 聚变知识库</small></span></a><nav class="topnav" aria-label="主导航"><a href="/contents/">目录</a><a href="/knowledge-tree/">知识树</a><a href="/references/">文献</a><a href="/comments/">讨论</a></nav></div>
<form class="global-search" action="/search/" role="search"><label class="sr-only" for="global-query">搜索知识库</label><input id="global-query" type="search" name="q" placeholder="搜索关键词、ICRH 或永久标签…" autocomplete="off"><button type="submit">搜索</button></form></header>
{breadcrumb_html}<div class="{layout_class}">{sidebar}
<main id="main"{main_class}>{mobile_nav}{body}{self.nav(url,True) if reader else ''}</main></div>
<footer class="footer"><div><span>Megawave-Fusion · 曦融兆波　/　Fusion Stacks</span><nav aria-label="站点说明"><a href="/about/">关于</a><a href="/contributing/">编写规范</a><a href="/verification/">核验记录</a><a href="/sources/">版本与来源</a><a href="{REPO}">GitHub ↗</a></nav></div></footer></body></html>'''
        target = self.out / ('404.html' if url == '/404.html' else url.strip('/') + '/index.html' if url != '/' else 'index.html')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        self.pages.append(url)

    def status(self, record):
        if record.get('status', 'draft') == 'draft' and record.get('source') in self.checked_sources:
            return '资料与公式已复核（模型辅助） · 待专家审核'
        return {'draft': '草稿 · 待领域审核', 'reviewing': '审核中', 'reviewed': '已审核', 'archived': '已归档'}[record.get('status', 'draft')]

    def tools(self, url, title, source=None, tag=None):
        key = tag or url.strip('/').replace('/', '-') or 'home'
        bib = f'@misc{{fusion-{key},\n  author = {{{{Megawave-Fusion}}}},\n  title = {{{title}}},\n  year = {{2026}},\n  url = {{{CONFIG["url"] + url}}},\n  note = {{Fusion Stacks; revision {self.revision[:12]}}}\n}}'
        search = REPO + '/discussions?discussions_q=' + quote('"' + (tag or title) + '"')
        edit = f'<a class="button" href="{REPO}/edit/main/{quote(source)}">编辑源文</a>' if source else ''
        return f'''<details class="page-tools"><summary>引用与编辑</summary><div class="page-actions"><button type="button" data-copy="url">复制永久链接</button>{edit}<a class="button" href="{search}">讨论本页 ↗</a></div><pre id="citation">{ESC(bib)}</pre><button type="button" data-copy="citation">复制引用</button></details>'''

    def index_record(self, title, url, text, **extra):
        plain = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True)
        self.search.append(dict(title=title, url=url, text=plain, order=len(self.search), **extra))

    def contents(self, expanded=False):
        rows = []
        for chapter in self.chapters:
            if len(chapter['sections']) == 1:
                section = chapter['sections'][0]
                teaser = ''.join(f'<li><a href="{e["url"]}">{ESC(e["title"])}</a></li>' for e in section['entries'])
                rows.append(f'<article class="chapter-row chapter-single"><div class="chapter-summary"><span class="chapter-number">{chapter["number"]:02}</span><a class="chapter-name" href="{section["url"]}">{ESC(chapter["title"])}</a><span class="chapter-size">{len(section["entries"])} 条目</span></div><p class="chapter-description">{ESC(chapter["description"])}</p>{"<ul class=single-entries>" + teaser + "</ul>" if expanded else ""}</article>')
                continue
            sections = []
            for section in chapter['sections']:
                teaser = ' · '.join(f'<a href="{e["url"]}">{ESC(e["title"])}</a>' for e in section['entries'])
                sections.append(f'<li><span class="subnumber">{section["number"]}</span><a href="{section["url"]}">{ESC(section["title"])}</a><span class="count">{len(section["entries"])} 条目</span>{"<div class=entry-teaser>"+teaser+"</div>" if expanded else ""}</li>')
            rows.append(f'<details class="chapter-row" {"open" if expanded else ""}><summary><span class="chapter-number">{chapter["number"]:02}</span><a class="chapter-name" href="{chapter["url"]}">{ESC(chapter["title"])}</a><span class="chapter-size">{len(chapter["sections"])} 专题</span></summary><p class="chapter-description">{ESC(chapter["description"])}</p><ul class="section-list">{"".join(sections)}</ul></details>')
        return '<div class="section-heading"><h2>知识目录</h2><div class="small-controls"><button type="button" data-expand="true">全部展开</button><button type="button" data-expand="false">全部收起</button></div></div><div class="chapter-list">' + ''.join(rows) + '</div>'

    def build(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        shutil.copytree(ROOT / 'site/assets', self.out / 'assets')
        for module, content in self.graph_modules.items():
            (self.out / 'assets' / module).write_text(content)
        vendor = ROOT / 'vendor/mathjax'
        if not (vendor / 'tex-chtml.js').exists():
            raise ValueError('Self-hosted MathJax missing; run scripts/vendor_mathjax.py')
        shutil.copytree(vendor, self.out / 'assets/mathjax')
        (self.out / '.nojekyll').touch()
        total = len(self.entries)
        hero = f'''<section class="hero"><img class="hero-mark" src="/assets/fusion.svg" alt="" width="82" height="82"><p class="eyebrow">Megawave-Fusion · Science, systems &amp; engineering</p><h1>聚变知识库</h1><p class="lead">聚变科学与工程的 Stacks Project。</p><div class="stats"><span><b>{total}</b>知识条目</span><span><b>{len(self.chapters)}</b>章节</span><span><b>{len(self.sections)}</b>专题</span><span><b>{len(self.references)}</b>参考来源</span></div><div class="hero-links"><a class="button primary" href="/sections/foundations/">开始阅读 →</a></div></section><p class="reading-note">覆盖基础物理、加热、装置、材料、诊断与工程。各条目包含原理、推导或方法实例，并就近列出参考文献。<a href="/verification/">查看资料、公式与算例核验记录</a>。</p>'''
        self.page('/', CONFIG['title'], hero + self.contents(), reader=False)
        self.page('/contents/', '完整目录', '<h1>完整目录</h1><p class="lead">按章节浏览，或直接进入带永久标签的知识条目。</p>' + self.contents(True), reader=False)
        for chapter in self.chapters:
            body = f'<p class="eyebrow">Chapter {chapter["number"]:02}</p><h1>{ESC(chapter["title"])}</h1><p>{ESC(chapter["description"])}</p>'
            for section in chapter['sections']:
                if len(chapter['sections']) == 1:
                    body += f'<p><a class="button primary" href="{section["url"]}">连续阅读 →</a></p><ul>'
                else:
                    body += f'<h2><span class="entry-number">{section["number"]}</span><a href="{section["url"]}">{ESC(section["title"])}</a></h2><ul>'
                body += ''.join(f'<li><a href="{e["url"]}">{ESC(e["title"])}</a> <span class="tag">{e["tag"]}</span></li>' for e in section['entries']) + '</ul>'
            self.page(chapter['url'], chapter['title'], body, chapter, reader=len(chapter['sections']) > 1)
        for section in self.sections:
            chapter = section['chapter']
            intro = self.render(section['intro'], section['source'])
            blocks = []
            for entry in section['entries']:
                content = self.render(entry['markdown'], entry['source'])
                entry['html'] = content
                review = f'<span>{self.status(entry)}</span>' if self.status(entry) != self.status(section) else ''
                blocks.append(f'<section class="entry-block" id="{entry["tag"]}"><div class="entry-heading"><h2><span class="entry-number">{entry["number"]}</span><a href="{entry["url"]}">{ESC(entry["title"])}</a></h2><a class="tag" href="{entry["url"]}">{entry["tag"]}</a></div><div class="prose">{content}</div><div class="entry-tools">{review}<a href="{entry["url"]}">条目详情与引用 →</a></div></section>')
                self.index_record(entry['title'], entry['url'], content, tag=entry['tag'], kind='条目',
                                  chapter_slug=chapter['slug'], chapter_title=chapter['title'], section_title=section['title'],
                                  aliases=section['slug'])
            toc = '<details class="page-toc"><summary>本节目录 · ' + str(len(section['entries'])) + ' 个条目</summary><ul>' + ''.join(f'<li><a href="#{e["tag"]}">{ESC(e["title"])}</a></li>' for e in section['entries']) + '</ul></details>' if len(section['entries']) > 1 else ''
            body = f'<p class="eyebrow">Section {section["number"]} · 连续阅读</p><h1>{ESC(section["title"])}</h1><div class="page-meta"><span>{len(section["entries"])} 个条目</span><span class="status">{self.status(section)}</span></div><div class="prose">{intro}</div>' + toc + ''.join(blocks) + self.tools(section['url'], section['title'], section['source'])
            self.page(section['url'], section['title'], body, chapter, [(chapter['url'], chapter['title'])] if len(chapter['sections']) > 1 else [], math=True)
            self.index_record(section['title'], section['url'], intro, kind='专题', chapter_slug=chapter['slug'], chapter_title=chapter['title'], section_title=section['title'], aliases=section['slug'])
        for entry in self.entries:
            section, chapter = entry['section'], entry['section']['chapter']
            body = f'<p class="eyebrow">Entry {entry["number"]} · {ESC(entry["kind"])}</p><h1>{ESC(entry["title"])}</h1><div class="page-meta"><span class="tag">{entry["tag"]}</span><span class="status">{self.status(entry)}</span><a href="{section["url"]}#{entry["tag"]}">在连续正文中阅读</a></div><article class="prose">{entry["html"]}</article>' + self.tools(entry['url'], entry['title'], entry['source'], entry['tag'])
            crumbs = ([(chapter['url'], chapter['title'])] if len(chapter['sections']) > 1 else []) + [(section['url'], section['title'])]
            self.page(entry['url'], entry['title'], body, chapter, crumbs, math=True)
        self.ancillary()
        json_write(self.out / 'search-index.json', self.search)
        json_write(self.out / 'tags.json', {e['tag']: {'title': e['title'], 'source': e['source'], 'url': e['url'], 'status': e['status']} for e in self.entries})
        json_write(self.out / 'navigation.json', [{'url': p['url'], 'title': p['title']} for p in self.sequence])
        json_write(self.out / 'data/knowledge-graph.json', self.graph)
        json_write(self.out / 'data/sources.json', self.references)
        json_write(self.out / 'data/verification.json', self.verification)
        sources = sorted({*self.paths, 'site/knowledge-relations.json'})
        manifest = {p: digest(ROOT / p) for p in sources}
        tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
        build_inputs = {p: digest(ROOT/p) for p in tracked if p and (ROOT/p).is_file() and not p.startswith('docs/')}
        receipt = {'built_at': datetime.now(timezone.utc).isoformat(), 'source_commit': self.revision,
                   'chapters': len(self.chapters), 'sections': len(self.sections), 'entries': len(self.entries),
                   'references': len(self.references), 'source_files': manifest, 'build_inputs': build_inputs,
                   'content_status': 'draft; scoped model-assisted source and formula review; specialist review pending', 'checked_source_count': len(self.checked_sources), 'all_registered_sources_rendered': True}
        json_write(self.out / 'edition.json', receipt)
        (self.out / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{CONFIG["url"]}{url}</loc></url>' for url in self.pages if url != '/404.html') + '</urlset>')
        (self.out / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {CONFIG["url"]}/sitemap.xml\n')
        print(f'Built {len(self.pages)} pages, {total} entries, {len(self.sections)} sections, {len(self.references)} references -> {self.out}')

    def ancillary(self):
        tree_body = '<div id="knowledge-tree" data-url="/data/knowledge-graph.json"></div><noscript><h1>知识树</h1><p>三维神经网络和学习流程图需要 JavaScript。仍可通过<a href="/contents/">完整目录</a>阅读所有条目。</p></noscript>'
        self.page('/knowledge-tree/', '知识树', tree_body, reader=False, full_width=True,
                  styles=('knowledge-tree.css', 'knowledge-3d.css'), modules=('knowledge-tree.mjs',),
                  description='在可旋转的三维神经网络与学习流程图之间切换，逐层探索聚变知识库、章节、专题、永久条目与建议学习路径。')
        self.index_record('知识树 · 三维神经网络与学习流程图', '/knowledge-tree/',
                          '探索全部知识条目、章节、主题关联与建议学习路径。', kind='工具',
                          chapter_slug='', chapter_title='', section_title='知识树')
        for source, url, title in [('README.md','/about/','关于知识库'),('编写说明.md','/contributing/','编写与审核'),('网站维护.md','/maintenance/','网站维护'),('核验记录.md','/verification/','内容核验记录')]:
            text = re.sub(r'^# .+\n', '', (ROOT / source).read_text(), count=1)
            if source == 'README.md':
                text = text.split('\n## ', 1)[0]
            content = self.render(text, source)
            if source == 'README.md':
                content += '<p>从<a href="/contents/">完整目录</a>浏览正文，或通过<a href="/knowledge-tree/">知识树</a>探索条目关系。条目来源、推导和审核状态分别保存；<a href="/contributing/">编写规范</a>说明参与方式。</p>'
            self.page(url, title, '<h1>' + title + '</h1><article class="prose">' + content + '</article>', math=True, reader=False)
            self.index_record(title, url, content, kind='说明', chapter_slug='', chapter_title='', section_title='站点文档')
        options = ''.join(f'<option value="{c["slug"]}">{ESC(c["title"])}</option>' for c in self.chapters)
        body = f'''<h1>搜索知识库</h1><p>支持中文、英文缩写、正文关键词和永久标签。多个关键词以空格分隔。</p><div class="search-controls"><label for="chapter-filter">章节<select id="chapter-filter"><option value="">全部章节</option>{options}</select></label><label for="kind-filter">类型<select id="kind-filter"><option value="">全部类型</option><option>条目</option><option>专题</option><option>文献</option><option>说明</option></select></label></div><p id="search-status" class="search-status" role="status" aria-live="polite">正在载入搜索索引…</p><div id="search-results"></div><button type="button" id="show-more" hidden>显示更多结果</button><noscript><p class="noscript">全文搜索需要 JavaScript。仍可通过<a href="/contents/">完整目录</a>阅读所有内容。</p></noscript>'''
        self.page('/search/', '搜索知识库', body, reader=False)
        body = f'<h1>参考文献与来源</h1><p>共 {len(self.references)} 条机构资料、课程和论文入口。来源核对日期及范围逐条记录；各条目就近注明所用文献的章节与公式位置。</p>'
        for ref in self.references:
            anchor = ref['id']
            title = ref.get('中文标题', ref['title'])
            original = f'<p>{ESC(ref["title"])}</p>' if title != ref['title'] else ''
            body += f'<article class="reference" id="{anchor}"><div class="ref-id">{anchor}</div><h2><a href="{ESC(ref["url"])}">{ESC(title)} ↗</a></h2>{original}<p>{ESC(ref["scope"])}</p><small>入口核对：{ref["checked_on"]} · {ESC(ref["evidence"])}</small></article>'
            self.index_record(title, '/references/#' + anchor, ref['title'] + ' ' + ref['scope'], tag=anchor, kind='文献', chapter_slug='literature', chapter_title='文献资料', section_title='参考来源')
        self.page('/references/', '参考文献与来源', body, reader=False)
        body = f'''<h1>讨论与勘误</h1><p>知识库的讨论保存在 GitHub Discussions。展开条目末尾的“引用与编辑”，可进入“讨论本页”，通过永久标签检索对应讨论。</p><p>欢迎提出原理解释、文献补充、工程经验和勘误。请说明对应条目、适用条件、来源与证据。</p><div class="page-actions"><a class="button primary" href="{REPO}/discussions">进入讨论区 ↗</a><a class="button" href="{REPO}/issues/new">提交勘误 ↗</a></div><p class="reading-note">当前使用 GitHub 原生讨论入口；站内嵌入式评论尚未启用。发表讨论需要登录 GitHub。</p>'''
        self.page('/comments/', '讨论与勘误', body, reader=False)
        body = f'''<h1>版本与来源</h1><p>本阅读版包含 {len(self.sections)} 个专题、{len(self.entries)} 个永久条目和 {len(self.references)} 条来源记录。正文保留中文目录，由同一份源文件生成连续阅读页与条目页；原仓库历史完整保留。</p><dl><dt>源仓库</dt><dd><a href="{REPO}">{CONFIG['repository']}</a></dd><dt>构建所基于的提交</dt><dd><a href="{REPO}/commit/{self.revision}"><code>{self.revision[:12]}</code></a></dd><dt>条目审核状态</dt><dd>模型辅助复核按正文版本保存，领域专家审核状态另行记录。<a href="/verification/">详见核验记录</a>。</dd></dl><h2>可追溯记录</h2><ul><li><a href="/edition.json">版本回执与源文件 SHA-256</a></li><li><a href="/tags.json">永久标签索引</a></li><li><a href="/data/knowledge-graph.json">知识树节点、编者关系与学习路径</a></li><li><a href="/navigation.json">完整阅读顺序</a></li><li><a href="/data/sources.json">结构化参考来源</a></li><li><a href="/data/verification.json">内容复核范围与源文校验值</a></li></ul><h2>构建与署名</h2><p>阅读组织参考 <a href="https://mingchenxia.github.io/Pome/">Pome</a> 与 <a href="https://stacks.math.columbia.edu/">Stacks Project</a> 的章节、标签和交叉引用方式。本站使用针对现有 Markdown 内容编写的静态生成器；保留未来接入 LaTeX/Gerby 的适配空间。</p><p>数学公式由自托管的 MathJax 3.2.2 渲染，<a href="/assets/mathjax/LICENSE">MathJax 许可证</a>随站点提供。网站发布不改变原知识正文的许可：本仓库不默认授予内容开源许可。</p>'''
        self.page('/sources/', '版本与来源', body, reader=False)
        self.page('/404.html', '页面未找到', '<h1>页面未找到</h1><p>可用关键词或永久标签查找条目，也可以返回完整目录。</p><a class="button" href="/contents/">浏览完整目录</a>', reader=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='_site', choices=['_site', 'docs'])
    parser.add_argument('--register-tags', action='store_true')
    args = parser.parse_args()
    Builder(ROOT / args.output, args.register_tags).build()


if __name__ == '__main__':
    main()
