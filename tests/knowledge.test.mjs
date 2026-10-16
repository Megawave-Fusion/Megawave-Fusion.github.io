import test from 'node:test';
import assert from 'node:assert/strict';
import {searchNodes, getNeighborhood, filterGraph, layoutFlow, layoutNeural, layoutHierarchy} from '../site/assets/knowledge-core.mjs';

const nodes = [
  {id: 'MF000001', title: '等离子体', chapter: 'physics', chapterTitle: '等离子体物理', section: 'basics', sectionTitle: '基本概念', summary: '带电粒子的集体行为'},
  {id: 'MF000002', title: '单粒子回旋运动', chapter: 'physics', chapterTitle: '等离子体物理', section: 'orbits', sectionTitle: '粒子轨道', summary: '洛伦兹力与回旋频率'},
  {id: 'MF000003', title: '波动基础', chapter: 'physics', chapterTitle: '等离子体物理', section: 'waves', sectionTitle: '等离子体波', summary: '介电张量与色散关系'},
  {id: 'MF000004', title: '原理与适用条件', chapter: 'heating', chapterTitle: '辅助加热', section: 'icrh', sectionTitle: '离子回旋加热（ICRH / ICRF）', summary: '少数离子共振吸收'},
  {id: 'MF000005', title: '原理与适用条件', chapter: 'heating', chapterTitle: '辅助加热', section: 'nbi', sectionTitle: '中性束注入（NBI）', summary: '快离子的碰撞慢化'},
  {id: 'MF000006', title: 'RF 保护', chapter: 'engineering', chapterTitle: '工程与控制', section: 'protection', sectionTitle: '射频系统', summary: '反射功率与电弧保护'},
  {id: 'MF000007', title: '独立词条', chapter: 'engineering', chapterTitle: '工程与控制', section: 'misc', sectionTitle: '其他', summary: ''},
];
const edge = (source, target, type = 'prerequisite') => ({source, target, type, reason: ''});
const edges = [
  edge('MF000001', 'MF000002'), edge('MF000001', 'MF000003'),
  edge('MF000002', 'MF000004'), edge('MF000003', 'MF000004'),
  edge('MF000004', 'MF000006', 'related'), edge('MF000005', 'MF000004', 'related'),
];
const data = {nodes, edges, paths: [{id: 'icrh-route', title: 'ICRH 学习路线', nodes: ['MF000001', 'MF000002', 'MF000003', 'MF000004']}]};
const ids = items => items.map(node => node.id);
const sorted = values => [...values].sort();

test('search normalizes case and full-width permanent tags', () => {
  assert.deepEqual(ids(searchNodes(nodes, 'ｍｆ０００００４')), ['MF000004']);
  assert.deepEqual(ids(searchNodes(nodes, 'ＩＣＲＨ')), ['MF000004']);
});
test('context separates repeated titles and combines words across fields', () => {
  assert.deepEqual(ids(searchNodes(nodes, '原理 ICRH')), ['MF000004']);
  assert.deepEqual(ids(searchNodes(nodes, '原理 NBI')), ['MF000005']);
  assert.deepEqual(ids(searchNodes(nodes, '辅助加热 少数离子')), ['MF000004']);
  assert.deepEqual(ids(searchNodes(nodes, '无关查询词')), []);
});
test('title matches outrank incidental summaries without losing stable ties', () => {
  const candidates = [{id: 'a', title: '其他', summary: '回旋运动'}, {id: 'b', title: '回旋运动'}, {id: 'c', title: '回旋运动'}];
  assert.deepEqual(ids(searchNodes(candidates, '回旋运动')), ['b', 'c', 'a']);
  assert.deepEqual(searchNodes(nodes, '  '), nodes);
});
test('ancestors and descendants recurse beyond one hop and exclude related links', () => {
  assert.deepEqual(sorted(getNeighborhood(nodes, edges, 'MF000004', 'ancestors')), ['MF000001', 'MF000002', 'MF000003', 'MF000004']);
  assert.deepEqual(sorted(getNeighborhood(nodes, edges, 'MF000001', 'descendants')), ['MF000001', 'MF000002', 'MF000003', 'MF000004']);
  assert.deepEqual(sorted(getNeighborhood(nodes, edges, 'MF000006', 'ancestors')), ['MF000006']);
});
test('neighbors includes both relation types but remains one hop', () => {
  assert.deepEqual(sorted(getNeighborhood(nodes, edges, 'MF000004')), ['MF000002', 'MF000003', 'MF000004', 'MF000005', 'MF000006']);
  assert.equal(getNeighborhood(nodes, edges, 'missing').size, 0);
  assert.deepEqual(sorted(getNeighborhood(nodes, edges, 'MF000007')), ['MF000007']);
});
test('chapter, path, focus, and query filters intersect and never leave dangling edges', () => {
  const filtered = filterGraph(data, {path: 'icrh-route', chapter: 'physics', focus: 'MF000004', mode: 'ancestors', query: '等离子体'});
  assert.deepEqual(ids(filtered.nodes), ['MF000001', 'MF000002', 'MF000003']);
  assert.equal(filtered.edges.length, 2);
  const retained = new Set(ids(filtered.nodes));
  assert.ok(filtered.edges.every(item => retained.has(item.source) && retained.has(item.target)));
  assert.deepEqual(filterGraph(data, {path: 'missing'}), {nodes: [], edges: []});
  assert.deepEqual(filterGraph(data, {focus: 'missing', mode: 'ancestors'}), {nodes: [], edges: []});
});
test('all mode preserves the graph despite a focus and filters invalid endpoints', () => {
  assert.deepEqual(filterGraph(data, {focus: 'MF000001', mode: 'all'}), {nodes, edges});
  assert.deepEqual(filterGraph({...data, edges: [...edges, edge('missing', 'MF000001')]}).edges, edges);
});
test('flow ranks a diamond after all prerequisite branches and ignores related direction', () => {
  const result = layoutFlow(nodes, [...edges, edge('MF000004', 'MF000001', 'related')]);
  const byId = new Map(result.nodes.map(node => [node.id, node]));
  assert.equal(byId.get('MF000001').level, 0);
  assert.equal(byId.get('MF000002').level, 1);
  assert.equal(byId.get('MF000003').level, 1);
  assert.equal(byId.get('MF000004').level, 2);
  for (const item of edges.filter(item => item.type === 'prerequisite')) {
    assert.ok(byId.get(item.target).x > byId.get(item.source).x);
  }
  for (let i = 0; i < result.nodes.length; i++) for (let j = i + 1; j < result.nodes.length; j++) {
    const a = result.nodes[i], b = result.nodes[j];
    assert.ok(Math.abs(a.x - b.x) >= 224 || Math.abs(a.y - b.y) >= 82, `${a.id} and ${b.id} overlap`);
  }
  for (const node of result.nodes) {
    assert.ok(node.x - 112 >= 0 && node.x + 112 <= result.width);
    assert.ok(node.y - 41 >= 0 && node.y + 41 <= result.height);
  }
});
test('cycle protection preserves downstream levels and terminates recursive focus', () => {
  const cyclicEdges = [...edges, edge('MF000003', 'MF000001')];
  const result = layoutFlow(nodes, cyclicEdges);
  const byId = new Map(result.nodes.map(node => [node.id, node]));
  assert.equal(byId.get('MF000001').level, byId.get('MF000003').level);
  assert.ok(byId.get('MF000004').level > byId.get('MF000001').level);
  assert.deepEqual(sorted(getNeighborhood(nodes, cyclicEdges, 'MF000004', 'ancestors')), ['MF000001', 'MF000002', 'MF000003', 'MF000004']);
});
test('empty, singleton, disconnected and invalid-edge flow layouts stay finite', () => {
  for (const items of [[], nodes.slice(0, 1), nodes]) {
    const result = layoutFlow(items, [edge('missing', 'MF000001')]);
    assert.equal(result.nodes.length, items.length);
    assert.ok(result.width > 0 && result.height > 0);
    assert.ok(result.nodes.every(node => [node.x, node.y, node.level].every(Number.isFinite)));
    assert.ok(result.nodes.every(node => node.level === 0));
  }
});
test('neural layout is deterministic, bounded, finite and does not mutate its inputs', () => {
  const before = JSON.stringify(data);
  const first = layoutNeural(nodes, edges, {width: 1000, height: 700});
  assert.deepEqual(first, layoutNeural(nodes, edges, {width: 1000, height: 700}));
  assert.equal(JSON.stringify(data), before);
  assert.deepEqual(ids(first.nodes), ids(nodes));
  assert.ok(first.nodes.every(node => Number.isFinite(node.x) && Number.isFinite(node.y) && node.x >= 0 && node.x <= 1000 && node.y >= 0 && node.y <= 700));
  const coordinates = new Set(first.nodes.map(node => `${node.x},${node.y}`));
  assert.equal(coordinates.size, nodes.length);
});
test('neural layout safely handles no nodes, one node, tiny canvas and invalid dimensions', () => {
  assert.deepEqual(layoutNeural([], []), {nodes: [], width: 1200, height: 800});
  assert.equal(layoutNeural(nodes.slice(0, 1), []).nodes[0].x, 600);
  for (const options of [{width: 2, height: 3}, {width: NaN, height: -5, iterations: Infinity}, {iterations: 0}]) {
    const result = layoutNeural(nodes, edges, options);
    assert.ok(result.nodes.every(node => Number.isFinite(node.x) && Number.isFinite(node.y) && node.x >= 0 && node.x <= result.width && node.y >= 0 && node.y <= result.height));
  }
});
test('neural layout supports the complete 144-node edition including cycles', () => {
  const many = Array.from({length: 144}, (_, i) => ({id: `MF${String(i).padStart(6, '0')}`, title: `条目 ${i}`, chapter: `chapter-${i % 10}`}));
  const links = many.map((node, i) => edge(node.id, many[(i + 1) % many.length].id));
  const result = layoutNeural(many, links);
  assert.equal(result.nodes.length, 144);
  assert.ok(result.nodes.every(node => Number.isFinite(node.x) && Number.isFinite(node.y)));
});

const hierarchical = {
  root: {id: 'fusion', title: '聚变知识树', url: '/'},
  chapters: Array.from({length: 10}, (_, i) => ({id: `chapter-${i}`, title: `章节 ${i}`})),
  sections: Array.from({length: 21}, (_, i) => ({id: `section-${i}`, title: `专题 ${i}`, chapter: `chapter-${i % 10}`})),
  nodes: Array.from({length: 144}, (_, i) => ({id: `MF${String(i).padStart(6, '0')}`, title: `条目 ${i}`, section: `section-${i % 21}`, chapter: `chapter-${i % 21 % 10}`})),
  edges: [edge('MF000000', 'MF000001'), edge('MF000001', 'MF000002', 'related')],
};
test('hierarchy has four levels and preserves the exact 144 permanent tag leaves', () => {
  const result = layoutHierarchy(hierarchical);
  assert.equal(result.nodes.length, 176);
  assert.deepEqual(sorted(result.nodes.filter(node => node.nodeType === 'tag').map(node => node.id)), sorted(ids(hierarchical.nodes)));
  assert.equal(result.nodes.filter(node => node.nodeType === 'root').length, 1);
  assert.equal(result.nodes.filter(node => node.nodeType === 'chapter').length, 10);
  assert.equal(result.nodes.filter(node => node.nodeType === 'section').length, 21);
  assert.equal(result.nodes.find(node => node.id === 'root:fusion').count, 144);
  assert.equal(result.edges.filter(item => item.type === 'membership').length, 175);
  assert.equal(result.edges.filter(item => item.type === 'prerequisite').length, 1);
  assert.ok(result.nodes.every(node => Number.isFinite(node.x) && Number.isFinite(node.y) && node.x >= 0 && node.x <= result.width && node.y >= 0 && node.y <= result.height));
  assert.deepEqual(layoutHierarchy(hierarchical), result);
});
test('collapsing a section hides only its tags and never aggregates knowledge edges', () => {
  const complete = layoutHierarchy(hierarchical);
  const result = layoutHierarchy(hierarchical, {collapsed: new Set(['section:section-0'])});
  assert.ok(result.nodes.some(node => node.id === 'section:section-0'));
  assert.ok(!result.nodes.some(node => node.id === 'MF000000'));
  assert.ok(!result.edges.some(item => item.type === 'prerequisite'));
  assert.ok(result.edges.some(item => item.type === 'related'));
  const retained = new Set(ids(result.nodes));
  assert.ok(result.edges.every(item => retained.has(item.source) && retained.has(item.target)));
  for (const node of result.nodes) {
    const previous = complete.nodes.find(item => item.id === node.id);
    assert.equal(node.x, previous.x);
    assert.equal(node.y, previous.y);
  }
});
test('collapsing root or a chapter removes all descendants while retaining the parent', () => {
  const root = layoutHierarchy(hierarchical, {collapsed: new Set(['root:fusion'])});
  assert.deepEqual(ids(root.nodes), ['root:fusion']);
  assert.deepEqual(root.edges, []);
  const chapter = layoutHierarchy(hierarchical, {collapsed: new Set(['chapter:chapter-0'])});
  assert.ok(chapter.nodes.some(node => node.id === 'chapter:chapter-0'));
  assert.ok(!chapter.nodes.some(node => node.chapter === 'chapter-0' && node.nodeType !== 'chapter'));
});
test('hierarchy safely handles empty and partial metadata without losing leaves', () => {
  assert.equal(layoutHierarchy({nodes: [], edges: []}).nodes.length, 1);
  const result = layoutHierarchy({nodes: [{id: 'ONLY', title: '单条目'}], edges: []});
  assert.equal(result.nodes.length, 4);
  assert.deepEqual(ids(result.nodes.filter(node => node.nodeType === 'tag')), ['ONLY']);
  assert.ok(result.nodes.every(node => Number.isFinite(node.x) && Number.isFinite(node.y)));
});
