#!/usr/bin/env python3
"""Check current Tag structure and, when present, the versioned review ledger.

Use --require-review to additionally require a complete independent review.
Structural coverage never promotes a draft or creates review evidence.
"""
import argparse
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
def sha(data):
    return hashlib.sha256(data).hexdigest()
def body(text, heading):
    return text.split('\n## ' + heading + '\n', 1)[1].split('\n## ', 1)[0]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-review', action='store_true')
    args = parser.parse_args()
    tags = json.loads((ROOT / 'site/tags.json').read_text())
    verification = json.loads((ROOT / 'site/verification.json').read_text())
    config = json.loads((ROOT / 'site/site.json').read_text())
    references = {r['url'] for r in json.loads((ROOT / '文献资料/来源索引.json').read_text())}
    headings = {source + '#' + heading
                for chapter in config['chapters'] for _, source in chapter['sections']
                for heading in re.findall(r'^## (.+)$', (ROOT / source).read_text(), re.M)}
    assert headings == set(tags), 'Current headings differ from the permanent Tag registry'
    assert {r['tag'] for r in tags.values()} == {f'MF{i:06d}' for i in range(1, 164)}, 'Permanent identities changed'
    for key, record in tags.items():
        source, heading = key.split('#', 1)
        chunk = body((ROOT / source).read_text(), heading)
        assert re.search(r'^### .+', chunk, re.M), f'{record["tag"]}: missing developed subsection'
        urls = set(re.findall(r'\]\((https?://[^)]+)\)', chunk))
        assert urls & references, f'{record["tag"]}: no indexed source cited in the entry'
    update = verification.get('tag_depth_update')
    if update is None:
        assert not args.require_review, 'Independent review ledger is pending'
        print(f'{len(tags)} Tag entries cover the current headings, developed subsections and indexed sources; independent review pending')
        return
    rows = update['tags']
    assert len(rows) == len(tags) == 163, 'Expected one review record for each existing Tag'
    assert len({r['tag'] for r in rows}) == len(rows), 'Duplicate Tag record'
    assert {r['key'] for r in rows} == set(tags), 'Coverage differs from the permanent Tag registry'
    for row in rows:
        tag = row['tag']
        assert tags[row['key']]['tag'] == tag, f'{tag}: permanent identity changed'
        source, heading = row['key'].split('#', 1)
        raw = (ROOT / source).read_bytes()
        chunk = body(raw.decode(), heading)
        digest = sha(raw)
        assert row['source_sha256'] == verification['source_sha256'][source] == digest, f'{tag}: stale source review'
        assert row['tag_body_sha256'] == sha(chunk.encode()), f'{tag}: stale Tag review'
        assert row['baseline_tag_body_sha256'] != row['tag_body_sha256'], f'{tag}: no content update'
        assert re.search(r'^### ', chunk, re.M), f'{tag}: missing derivation/case subdivision'
        assert row['derivation'] and row['example'], f'{tag}: missing derivation or worked example record'
        assert row['references'] and set(row['references']) <= references, f'{tag}: unindexed reference'
        review = row['independent_review']
        assert review['checked_source_sha256'] == digest, f'{tag}: independent review is stale'
        assert review['status'] == 'passed' and review['finding'], f'{tag}: independent review incomplete'
        assert review['reviewer'] != row['author'], f'{tag}: author cannot cross-review own text'
    for group, run in update['numerical_checks'].items():
        assert run['all_passed'], f'{group}: numerical check failed'
        assert run['count'] > 0, f'{group}: no numerical checks'
    print(f'{len(rows)}/{len(tags)} Tag records match the current text, references and independent reviews')

if __name__ == '__main__':
    main()
