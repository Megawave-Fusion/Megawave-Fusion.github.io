/**
 * Deterministic, genuine 3D layout for root → chapter → section → permanent Tag.
 *
 * layoutHierarchy3D(data, {collapsed = new Set()} = {}) returns
 * {nodes, edges, bounds:{center:{x,y,z},radius}}. Every node retains its original
 * metadata and has x/y/z (world coordinates), radius, count, nodeType and level.
 * The root is at the origin; chapter/section/Tag shells lie near 115/195/275.
 * IDs are root:fusion, chapter:<slug>, section:<slug>, and unchanged Tag IDs.
 *
 * Full-tree coordinates and bounds are computed BEFORE hiding collapsed
 * descendants. This preserves branch locations and a stable camera extent.
 * Knowledge edges to hidden Tags are removed, not aggregated into false
 * prerequisites. Membership edges point from a visible parent to its child.
 * This imports the existing hierarchy utility for metadata only and does not
 * change either 2D layout or the input data. No renderer or package is required.
 */
import {layoutHierarchy} from './knowledge-core.mjs?v=623eb0b900';

const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5));
const length = vector => Math.hypot(vector.x, vector.y, vector.z);
const multiply = (vector, factor) => ({x: vector.x * factor, y: vector.y * factor, z: vector.z * factor});
const add = (a, b) => ({x: a.x + b.x, y: a.y + b.y, z: a.z + b.z});
const cross = (a, b) => ({x: a.y * b.z - a.z * b.y, y: a.z * b.x - a.x * b.z, z: a.x * b.y - a.y * b.x});
const unit = vector => multiply(vector, 1 / (length(vector) || 1));

function seeded(value) {
  let state = 2166136261;
  for (const character of String(value)) {
    state ^= character.codePointAt(0);
    state = Math.imul(state, 16777619);
  }
  return () => {
    state += 0x6D2B79F5;
    let next = state;
    next = Math.imul(next ^ next >>> 15, next | 1);
    next ^= next + Math.imul(next ^ next >>> 7, next | 61);
    return ((next ^ next >>> 14) >>> 0) / 4294967296;
  };
}

function fibonacciDirection(index, count, phase = 0) {
  const y = 1 - 2 * (index + .5) / Math.max(1, count);
  const radial = Math.sqrt(Math.max(0, 1 - y * y));
  const angle = index * GOLDEN_ANGLE + phase;
  return {x: Math.cos(angle) * radial, y, z: Math.sin(angle) * radial};
}

function tangentFrame(normal) {
  const reference = Math.abs(normal.y) < .85 ? {x: 0, y: 1, z: 0} : {x: 1, y: 0, z: 0};
  const u = unit(cross(normal, reference));
  return {normal, u, v: unit(cross(normal, u))};
}

function inFrame(frame, coordinates) {
  return add(add(multiply(frame.u, coordinates.x), multiply(frame.v, coordinates.y)), multiply(frame.normal, coordinates.z));
}

export function layoutHierarchy3D(data, {collapsed = new Set()} = {}) {
  const hierarchy = layoutHierarchy(data);
  const parents = new Map();
  const children = new Map(hierarchy.nodes.map(node => [node.id, []]));
  const byId = new Map(hierarchy.nodes.map(node => [node.id, node]));
  for (const edge of hierarchy.edges) {
    if (edge.type !== 'membership') continue;
    parents.set(edge.target, edge.source);
    children.get(edge.source).push(byId.get(edge.target));
  }
  const root = hierarchy.nodes.find(node => node.nodeType === 'root');
  const coordinates = new Map([[root.id, {x: 0, y: 0, z: 0}]]);
  const chapters = children.get(root.id);
  chapters.forEach((chapter, chapterIndex) => {
    const chapterRandom = seeded(chapter.id);
    const direction = fibonacciDirection(chapterIndex, chapters.length, .43);
    const frame = tangentFrame(direction);
    coordinates.set(chapter.id, multiply(direction, 115 + (chapterRandom() - .5) * 8));
    const sections = children.get(chapter.id);
    const sectionPhase = chapterRandom() * Math.PI * 2;
    sections.forEach((section, sectionIndex) => {
      const next = seeded(section.id);
      // Each topic takes a separate branch around its chapter's spatial axis.
      // A six-topic chapter receives a wider cone than a single-topic chapter.
      const cone = sections.length > 1 ? Math.min(.58, .16 + sections.length * .035) : .045;
      const angle = sectionPhase + sectionIndex / Math.max(1, sections.length) * Math.PI * 2;
      const lateral = add(multiply(frame.u, Math.cos(angle) * cone), multiply(frame.v, Math.sin(angle) * cone));
      const sectionDirection = unit(add(direction, lateral));
      coordinates.set(section.id, multiply(sectionDirection, 195 + (next() - .5) * 10));
      const local = tangentFrame(sectionDirection);
      const tags = children.get(section.id);
      const clusterRadius = Math.max(18, Math.min(46, 14 * Math.cbrt(tags.length)));
      const clusterPhase = next() * Math.PI * 2;
      const clusterCenter = multiply(sectionDirection, 275 + (next() - .5) * 12);
      tags.forEach((tag, tagIndex) => {
        const tagRandom = seeded(tag.id);
        const direction = fibonacciDirection(tagIndex, tags.length, clusterPhase);
        // Volumetric rather than planar clusters: all three local axes vary.
        const radial = clusterRadius * (.64 + .36 * Math.cbrt(tagRandom()));
        const offset = inFrame(local, {x: direction.x * radial, y: direction.y * radial, z: direction.z * radial * .78});
        coordinates.set(tag.id, add(clusterCenter, offset));
      });
    });
  });
  const radii = {root: 22, chapter: 14, section: 9, tag: 4};
  const nodes = hierarchy.nodes.map(node => ({...node, ...coordinates.get(node.id),
    radius: radii[node.nodeType], count: node.nodeType === 'tag' ? 1 : node.count}));

  // Resolve occasional intersections of neighboring topic clusters in 3D.
  // The root stays fixed. Running on the full inventory keeps folding stable.
  const mobility = {root: 0, chapter: .2, section: .6, tag: 1};
  for (let pass = 0; pass < 64; pass++) {
    let moved = false;
    for (let i = 0; i < nodes.length; i++) for (let j = i + 1; j < nodes.length; j++) {
      const a = nodes[i], b = nodes[j];
      let dx = b.x - a.x, dy = b.y - a.y, dz = b.z - a.z;
      const minimum = a.radius + b.radius + 3;
      const distance = Math.hypot(dx, dy, dz);
      if (distance >= minimum - .00001) continue;
      if (distance < .00001) {
        const direction = fibonacciDirection(i, nodes.length, j * GOLDEN_ANGLE);
        dx = direction.x; dy = direction.y; dz = direction.z;
      }
      const shift = (minimum - distance) / Math.hypot(dx, dy, dz);
      const total = mobility[a.nodeType] + mobility[b.nodeType];
      if (!total) continue;
      const aShare = mobility[a.nodeType] / total, bShare = mobility[b.nodeType] / total;
      a.x -= dx * shift * aShare; a.y -= dy * shift * aShare; a.z -= dz * shift * aShare;
      b.x += dx * shift * bShare; b.y += dy * shift * bShare; b.z += dz * shift * bShare;
      moved = true;
    }
    if (!moved) break;
  }
  const bounds = {center: {x: 0, y: 0, z: 0}, radius: Math.max(...nodes.map(node => length(node) + node.radius)) + 2};
  const visible = nodes.filter(node => {
    let parent = parents.get(node.id);
    while (parent) {
      if (collapsed.has(parent)) return false;
      parent = parents.get(parent);
    }
    return true;
  });
  const ids = new Set(visible.map(node => node.id));
  const edges = hierarchy.edges.filter(edge => ids.has(edge.source) && ids.has(edge.target));
  return {nodes: visible, edges, bounds};
}
