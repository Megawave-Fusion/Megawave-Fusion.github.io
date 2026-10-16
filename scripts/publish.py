#!/usr/bin/env python3
"""Publish a validated static edition without force-push or scheduled CI."""
import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'site/site.json').read_text())


def run(*args, capture=False):
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=capture).stdout


def main():
    if run('git', 'branch', '--show-current', capture=True).strip() != 'main':
        raise SystemExit('Publish from main only.')
    if run('git', 'status', '--porcelain', capture=True).strip():
        raise SystemExit('Commit source changes before publishing.')
    remote = run('git', 'remote', 'get-url', 'origin', capture=True).strip()
    if remote not in (f'https://github.com/{CONFIG["repository"]}.git', f'git@github.com:{CONFIG["repository"]}.git'):
        raise SystemExit('Origin does not match the configured publication repository.')
    run('git', 'pull', '--ff-only', 'origin', 'main')
    run(sys.executable, '工具/检查知识库.py')
    run(sys.executable, 'scripts/build.py', '--output', 'docs')
    run(sys.executable, 'scripts/check_site.py', 'docs')
    run('git', 'add', '--', 'docs')
    if run('git', 'diff', '--cached', '--name-only', capture=True).strip():
        run('git', 'commit', '-m', 'Publish validated Fusion Stacks reading edition')
        run('git', 'push', 'origin', 'main')
    result = subprocess.run(['gh','api','--method','POST',f'repos/{CONFIG["repository"]}/pages/builds'], cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        print('Native Pages build request returned:', result.stderr.strip())
    expected = json.loads((ROOT/'docs/edition.json').read_text())
    for attempt in range(24):
        try:
            with urlopen(CONFIG['url'] + '/edition.json?revision=' + expected['source_commit'], timeout=20) as response:
                live = json.load(response)
            if live == expected:
                print('Verified live edition:', CONFIG['url'])
                return
        except Exception as exc:
            if attempt % 4 == 0:
                print('Waiting for Pages delivery:', type(exc).__name__, flush=True)
        time.sleep(10)
    raise SystemExit('Uploaded successfully, but live edition receipt did not match within four minutes; inspect GitHub Pages deployment status.')


if __name__ == '__main__':
    main()
