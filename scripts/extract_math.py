#!/usr/bin/env python3
"""Extract homepage and continuous-section math for the MathJax check."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
root=Path(__file__).resolve().parents[1]
rows={}
for p in [root/'_site/index.html', *(root/'_site/sections').glob('*/index.html')]:
 soup=BeautifulSoup(p.read_text(),'html.parser')
 for elem in soup.select('.arithmatex'):
  raw=elem.get_text()
  if not (raw.startswith('\\(') and raw.endswith('\\)') or raw.startswith('\\[') and raw.endswith('\\]')):raise ValueError((p,raw))
  tex=raw[2:-2];display=raw.startswith('\\[')
  rows.setdefault((tex,display),dict(tex=tex,display=display,page=p.relative_to(root/'_site').as_posix()))
p=root/'.build/reviews/math-input.json';p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(list(rows.values()),ensure_ascii=False,indent=2)+'\n')
print(f'Extracted {len(rows)} unique inline/display formulas')
