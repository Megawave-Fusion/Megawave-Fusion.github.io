#!/usr/bin/env python3
"""Verify every generated link, source receipt, tag, and navigation edge."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


def check(site):
    errors = []
    pages = {}
    for path in sorted(site.rglob('*.html')):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        ids = [n['id'] for n in soup.find_all(id=True)]
        if len(ids) != len(set(ids)):
            errors.append(f'Duplicate HTML id: {path.relative_to(site)}')
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
              'source_files': len(receipt['source_files']), 'reading_pages': len(nav), 'result': 'passed'}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '_site'
    check(ROOT / target)
