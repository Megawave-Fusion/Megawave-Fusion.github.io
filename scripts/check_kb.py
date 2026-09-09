"""Check local Markdown targets, navigation coverage, and source IDs; no network needed."""
from pathlib import Path
import json
import re
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
errors = []
files = sorted(ROOT.rglob('*.md'))
for path in files:
    text = path.read_text(encoding='utf-8')
    if not text.strip():
        errors.append(f'Empty Markdown: {path.relative_to(ROOT)}')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        target = unquote(target.split('#')[0].split('?')[0])
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            errors.append(f'{path.relative_to(ROOT)}: invalid target {target}')
for system in ['icrh', 'ecrh', 'nbi', 'lhcd', 'ebw', 'helicon']:
    base = ROOT / '03-heating-current-drive' / system
    for name in ['README', '01-principles', '02-hardware', '03-design-calculation', '04-control-protection', '05-testing-acceptance', '06-literature-cases']:
        if not (base / f'{name}.md').exists():
            errors.append(f'Missing system page: {system}/{name}')
sources = json.loads((ROOT / 'references/sources.json').read_text())
ids = [s['id'] for s in sources]
if len(ids) != len(set(ids)):
    errors.append('Duplicate source IDs')
catalog = (ROOT / 'CATALOG.md').read_text()
for path in files:
    rel = path.relative_to(ROOT).as_posix()
    if rel != 'CATALOG.md' and not rel.startswith('.github/') and f']({rel})' not in catalog:
        errors.append(f'Missing catalog entry: {rel}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(files)} Markdown files; 6 independent systems; {len(sources)} sources; local links and catalog coverage valid.')
print('Scope: structural checks only; external URLs, engineering claims and peer review are not validated by this script.')
