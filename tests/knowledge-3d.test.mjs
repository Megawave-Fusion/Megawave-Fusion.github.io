import test from 'node:test';
import assert from 'node:assert/strict';
import {layoutHierarchy3D} from '../site/assets/knowledge-3d-layout.mjs';

const data = {
  root: {id: 'fusion', title: '聚变知识库', nodeType: 'root', url: '/'},
  chapters: Array.from({length: 10}, (_, i) => ({id: `chapter-${i}`, title: `章节 ${i}`, color: '#227799', url: `/chapters/chapter-${i}/`, nodeType: 'chapter'})),
  sections: Array.from({length: 21}, (_, i) => ({id: `section-${i}`, title: `专题 ${i}`, chapter: `chapter-${i < 6 ? 0 : 1 + (i - 6) % 9}`, nodeType: 'section', url: `/sections/section-${i}/`})),
  nodes: Array.from({length: 144}, (_, i) => ({id: `MF${String(i).padStart(6, '0')}`, title: `条目 ${i}`, section: `section-${i % 21}`, chapter: `chapter-${i % 21 < 6 ? 0 : 1 + (i % 21 - 6) % 9}`, url: `/tag/MF${String(i).padStart(6, '0')}/`, summary: `摘要 ${i}`, status: 'reviewed'})),
  edges: [{source: 'MF000000', target: 'MF000001', type: 'prerequisite', reason: '先读基础'}, {source: 'MF000001', target: 'MF000002', type: 'related', reason: '内容相关'}],
};
const ids = nodes => nodes.map(node => node.id).sort();
const distance = (a, b) => Math.hypot(a.x - b.x, a.y - b.y, a.z - b.z);
const subtract = (a, b) => ({x: a.x - b.x, y: a.y - b.y, z: a.z - b.z});
function tetrahedronDeterminant(a, b, c, d) {
  const u = subtract(b, a), v = subtract(c, a), w = subtract(d, a);
  return u.x * (v.y * w.z - v.z * w.y) - u.y * (v.x * w.z - v.z * w.x) + u.z * (v.x * w.y - v.y * w.x);
}

test('3D hierarchy contains 176 nodes with the exact permanent Tag IDs and metadata', () => {
  const graph = layoutHierarchy3D(data);
  assert.equal(graph.nodes.length, 176);
  assert.equal(graph.edges.filter(edge => edge.type === 'membership').length, 175);
  const leaves = graph.nodes.filter(node => node.nodeType === 'tag');
  assert.deepEqual(ids(leaves), ids(data.nodes));
  for (const node of leaves) {
    const original = data.nodes.find(entry => entry.id === node.id);
    for (const key of Object.keys(original)) assert.deepEqual(node[key], original[key]);
    assert.equal(node.count, 1);
    assert.equal(node.radius, 4);
  }
  assert.equal(graph.nodes.find(node => node.id === 'root:fusion').count, 144);
});
test('chapter positions are genuinely volumetric, not a tilted 2D drawing', () => {
  const graph = layoutHierarchy3D(data);
  const chapters = graph.nodes.filter(node => node.nodeType === 'chapter');
  const volume = Math.abs(tetrahedronDeterminant(...chapters.slice(0, 4))) / 6;
  assert.ok(volume > 10000, `Tetrahedron volume is only ${volume}`);
  for (const axis of ['x', 'y', 'z']) {
    assert.ok(Math.min(...chapters.map(node => node[axis])) < -50);
    assert.ok(Math.max(...chapters.map(node => node[axis])) > 50);
  }
  const cluster = graph.nodes.filter(node => node.nodeType === 'tag' && node.section === 'section-0');
  assert.ok(Math.abs(tetrahedronDeterminant(...cluster.slice(0, 4))) > 100);
});
test('all spheres have finite coordinates, separate shells and correct bounding sphere', () => {
  const graph = layoutHierarchy3D(data);
  const root = graph.nodes.find(node => node.nodeType === 'root');
  assert.deepEqual([root.x, root.y, root.z], [0, 0, 0]);
  assert.ok(graph.bounds.radius > 280 && graph.bounds.radius < 350);
  const shells = {root: [0, 0], chapter: [100, 130], section: [180, 215], tag: [230, 330]};
  for (const node of graph.nodes) {
    assert.ok([node.x, node.y, node.z, node.radius].every(Number.isFinite));
    const radial = distance(node, graph.bounds.center);
    assert.ok(radial + node.radius <= graph.bounds.radius);
    const [minimum, maximum] = shells[node.nodeType];
    assert.ok(radial >= minimum && radial <= maximum, `${node.id} is outside its layer: ${radial}`);
  }
  for (let i = 0; i < graph.nodes.length; i++) for (let j = i + 1; j < graph.nodes.length; j++) {
    const a = graph.nodes[i], b = graph.nodes[j];
    assert.ok(distance(a, b) >= a.radius + b.radius, `${a.id} intersects ${b.id}`);
  }
});
test('collapsing sections removes only descendants and never redirects knowledge edges', () => {
  const full = layoutHierarchy3D(data);
  const folded = layoutHierarchy3D(data, {collapsed: new Set(['section:section-0'])});
  assert.ok(folded.nodes.some(node => node.id === 'section:section-0'));
  assert.ok(!folded.nodes.some(node => node.id === 'MF000000'));
  assert.ok(!folded.edges.some(edge => edge.type === 'prerequisite'));
  assert.ok(folded.edges.some(edge => edge.type === 'related'));
  assert.deepEqual(folded.bounds, full.bounds);
  const visible = new Set(ids(folded.nodes));
  assert.ok(folded.edges.every(edge => visible.has(edge.source) && visible.has(edge.target)));
  for (const node of folded.nodes) assert.deepEqual(node, full.nodes.find(entry => entry.id === node.id));
});
test('chapter and root folding hides all nested descendants', () => {
  const chapter = layoutHierarchy3D(data, {collapsed: new Set(['chapter:chapter-0'])});
  assert.ok(chapter.nodes.some(node => node.id === 'chapter:chapter-0'));
  assert.ok(!chapter.nodes.some(node => node.chapter === 'chapter-0' && node.nodeType !== 'chapter'));
  const root = layoutHierarchy3D(data, {collapsed: new Set(['root:fusion'])});
  assert.deepEqual(ids(root.nodes), ['root:fusion']);
  assert.deepEqual(root.edges, []);
});
test('3D layout is deterministic and preserves the input object', () => {
  const before = JSON.stringify(data);
  assert.deepEqual(layoutHierarchy3D(data), layoutHierarchy3D(data));
  assert.equal(JSON.stringify(data), before);
});
test('empty and partial data still produce finite bounds and preserve existing tags', () => {
  const empty = layoutHierarchy3D({nodes: [], edges: []});
  assert.equal(empty.nodes.length, 1);
  assert.ok(empty.bounds.radius >= empty.nodes[0].radius);
  const single = layoutHierarchy3D({nodes: [{id: 'MF000001', title: '唯一条目', url: '/tag/MF000001/'}], edges: []});
  assert.equal(single.nodes.length, 4);
  assert.deepEqual(ids(single.nodes.filter(node => node.nodeType === 'tag')), ['MF000001']);
  assert.ok(single.nodes.every(node => [node.x, node.y, node.z].every(Number.isFinite)));
});
