#!/usr/bin/env python3
"""Check local scientific figures and focused simulation entries, not physics accuracy."""
from pathlib import Path
import json,re
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'site/site.json').read_text());seen=set();pages=0
for chapter in config['chapters']:
    for slug,source in chapter['sections']:
        text=(ROOT/source).read_text();pages+=1
        assert not re.search(r'[\x00-\x09\x0b-\x1f]',text), f'Control character in {source}'
        figures=re.findall(r'!\[([^\]]*)\]\((/assets/diagrams/[^)]+)\)',text)
        assert figures, f'No explanatory figure in {source}'
        for alt,url in figures:
            assert alt.strip(),f'Empty figure description in {source}'
            path=ROOT/'site'/url.lstrip('/');svg=ET.parse(path).getroot()
            ns={'s':'http://www.w3.org/2000/svg'}
            assert svg.attrib.get('viewBox'),f'Nonresponsive SVG: {path}'
            assert svg.find('s:title',ns) is not None,f'Missing SVG title: {path}'
            assert svg.find('s:desc',ns) is not None,f'Missing SVG description: {path}'
            assert not any(n.tag.endswith('script') or any(k.startswith('on') for k in n.attrib) for n in svg.iter()),f'Active figure: {path}'
            seen.add(url)
        if chapter['slug']=='simulation':
            parts=re.split(r'^## (.+)\n',text,flags=re.M)
            for i in range(1,len(parts),2):
                count=len(re.findall(r'[\u4e00-\u9fff]',parts[i+1]))
                assert count<=1500,f'Overloaded simulation Tag: {source}#{parts[i]} ({count} Han characters)'
            if slug in {f'simulation-{s}' for s in ['icrh','ecrh','nbi','lhcd','ebw','helicon']}:
                assert len(parts[1::2])>=5,f'Missing heating simulation processes: {source}'
print(f'{pages} topics have {len(seen)} local, described SVG figures; simulation entry granularity checks passed.')
