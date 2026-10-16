#!/usr/bin/env python3
"""Vendor a fixed upstream MathJax release from the official npm registry."""
import hashlib
import io
import json
from pathlib import Path
import tarfile
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
VERSION = '3.2.2'


def main():
    dest = ROOT / 'vendor/mathjax'
    if (dest / 'tex-chtml.js').exists():
        print('MathJax already vendored; no download needed.')
        return
    metadata = json.load(urlopen(f'https://registry.npmjs.org/mathjax/{VERSION}', timeout=30))
    archive = urlopen(metadata['dist']['tarball'], timeout=60).read()
    if hashlib.sha1(archive).hexdigest() != metadata['dist']['shasum']:
        raise ValueError('MathJax package checksum mismatch')
    dest.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as tar:
        for member in tar.getmembers():
            name = member.name
            if not member.isfile():
                continue
            if name.startswith('package/es5/'):
                relative = name[len('package/es5/'):]
            elif name == 'package/LICENSE':
                relative = 'LICENSE'
            else:
                continue
            path = (dest / relative).resolve()
            if not path.is_relative_to(dest.resolve()):
                raise ValueError('Archive path escapes vendor folder')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(tar.extractfile(member).read())
    (dest / 'upstream.json').write_text(json.dumps({'package': 'mathjax', 'version': VERSION,
        'tarball': metadata['dist']['tarball'], 'sha256': hashlib.sha256(archive).hexdigest()}, indent=2) + '\n')
    print(f'Vendored MathJax {VERSION}: {len(list(dest.rglob("*")))} paths')


if __name__ == '__main__':
    main()
