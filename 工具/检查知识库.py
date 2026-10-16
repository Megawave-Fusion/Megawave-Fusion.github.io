"""检查中文目录、独立加热系统、文档链接与来源索引。"""
from pathlib import Path
from urllib.parse import unquote
import json
import re
根目录 = Path(__file__).resolve().parents[1]
错误 = []
忽略目录 = {'.git', '.venv', '.运行环境', '_site', 'docs', '.build', 'vendor', 'node_modules'}
文档 = sorted(p for p in 根目录.rglob('*.md') if not 忽略目录.intersection(p.relative_to(根目录).parts))
引用 = set()
for 文件 in 文档:
    相对路径 = 文件.relative_to(根目录)
    if any(re.match(r'^\d+[-_、.]', 段) for 段 in 相对路径.parts):
        错误.append(f'目录或文件仍含编号：{相对路径}')
    正文 = 文件.read_text(encoding='utf-8')
    if re.search(r'^\s*\d+\.\s', 正文, re.M):
        错误.append(f'正文仍含数字列表：{相对路径}')
    for 目标 in re.findall(r'\[[^\]]*\]\(([^)]+)\)', 正文):
        if 目标.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        路径 = (文件.parent / unquote(目标.split('#')[0].split('?')[0])).resolve()
        if not 路径.is_relative_to(根目录) or not 路径.exists():
            错误.append(f'{相对路径}：链接不存在 {目标}')
        引用.add(路径)
for 名称 in ['离子回旋加热', '电子回旋加热', '中性束注入', '低杂波电流驱动', '电子伯恩斯坦波加热', '螺旋波加热']:
    目录 = 根目录 / '辅助加热' / 名称
    if sorted(p.name for p in 目录.glob('*.md')) != ['README.md']:
        错误.append(f'{名称} 应仅有一个主页面')
for 文件 in 文档:
    if 文件 != 根目录 / 'README.md' and 文件 not in 引用:
        错误.append(f'缺少导航入口：{文件.relative_to(根目录)}')
来源 = json.loads((根目录 / '文献资料/来源索引.json').read_text())
if len({项['id'] for 项 in 来源}) != len(来源):
    错误.append('来源编号重复')
if 错误:
    raise SystemExit('\n'.join(错误))
print(f'通过：{len(文档)} 个 Markdown 文件，六套加热系统各一个主页面，{len(来源)} 条来源。')
print('目录、导航与本地链接检查通过；未进行技术内容审核或外部链接联网检查。')
