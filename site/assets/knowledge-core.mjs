/**
 * Dependency-free knowledge graph utilities. All functions leave input data intact.
 * Nodes use {id,title,chapter,chapterTitle,section,sectionTitle,url,summary,status};
 * edges use {source,target,type:'prerequisite'|'related',reason}. A prerequisite
 * edge points from the concept to learn first to the concept that depends on it.
 *
 * searchNodes(nodes, query) returns original nodes, relevance-ranked (stable ties).
 * getNeighborhood(nodes, edges, id, mode) returns a Set of IDs including the focus;
 * neighbors includes both edge types in either direction; ancestors/descendants
 * traverse prerequisite edges only. An unknown focus produces an empty Set.
 * filterGraph(data, options) intersects query, chapter, path and focus constraints,
 * then keeps only edges whose two endpoints remain. mode='all' ignores focus.
 * Paths have {id,title,description,nodes:[id]}; an unknown selected path is empty.
 * Both layouts return {nodes:[{...node,x,y,level}],width,height}, with x/y at the
 * NODE CENTER. Flow allocates 224×82 cards with 320/112 center spacing and 48px
 * outer padding. Neural level is 0; its bounded, seeded simulation runs once.
 * layoutHierarchy(data,{collapsed,width,height}) adds root/chapter/section nodes
 * and parent-to-child membership edges. Tags retain permanent IDs and nodeType
 * 'tag'; non-leaves use root:/chapter:/section: IDs and count descendant tags.
 * collapsed is a Set of these derived IDs. Hidden leaves' knowledge edges are
 * omitted, never replaced by a misleading prerequisite between parent groups.
 */

const normalized = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();

export function searchNodes(nodes, query = '') {
  const words = normalized(query).split(' ').filter(Boolean);
  if (!words.length) return [...nodes];
  return nodes.map((node, index) => {
    const fields = [
      [normalized(node.id), 140],
      [normalized(node.title), 45],
      [normalized(node.sectionTitle), 26],
      [normalized(node.chapterTitle), 15],
      [normalized(node.section), 12],
      [normalized(node.chapter), 10],
      [normalized(node.summary), 5],
    ];
    let score = 0;
    for (const word of words) {
      let best = 0;
      for (const [text, weight] of fields) {
        if (text.includes(word)) best = Math.max(best, weight + (text === word ? weight : 0));
      }
      if (!best) return null;
      score += best;
    }
    return {node, score, index};
  }).filter(Boolean).sort((a, b) => b.score - a.score || a.index - b.index).map(item => item.node);
}

export function getNeighborhood(nodes, edges, id, mode = 'neighbors') {
  const ids = new Set(nodes.map(node => node.id));
  if (!ids.has(id)) return new Set();
  const result = new Set([id]);
  if (!['neighbors', 'ancestors', 'descendants'].includes(mode)) return result;
  const adjacency = new Map(nodes.map(node => [node.id, new Set()]));
  for (const edge of edges) {
    if (!ids.has(edge.source) || !ids.has(edge.target)) continue;
    if (mode === 'neighbors') {
      adjacency.get(edge.source).add(edge.target);
      adjacency.get(edge.target).add(edge.source);
    } else if (edge.type === 'prerequisite') {
      const [from, to] = mode === 'ancestors' ? [edge.target, edge.source] : [edge.source, edge.target];
      adjacency.get(from).add(to);
    }
  }
  if (mode === 'neighbors') {
    for (const next of adjacency.get(id)) result.add(next);
    return result;
  }
  const queue = [id];
  for (let head = 0; head < queue.length; head++) {
    for (const next of adjacency.get(queue[head])) {
      if (!result.has(next)) {
        result.add(next);
        queue.push(next);
      }
    }
  }
  return result;
}

export function filterGraph(data, {query = '', chapter = '', focus = '', mode = 'all', path = ''} = {}) {
  const searched = new Set(searchNodes(data.nodes, query).map(node => node.id));
  const pathIds = path ? new Set((data.paths ?? []).find(item => item.id === path)?.nodes ?? []) : null;
  const nearby = focus && mode !== 'all' ? getNeighborhood(data.nodes, data.edges, focus, mode) : null;
  const nodes = data.nodes.filter(node => searched.has(node.id)
    && (!chapter || node.chapter === chapter)
    && (!pathIds || pathIds.has(node.id))
    && (!nearby || nearby.has(node.id)));
  const retained = new Set(nodes.map(node => node.id));
  const edges = data.edges.filter(edge => retained.has(edge.source) && retained.has(edge.target));
  return {nodes, edges};
}

function prerequisiteGraph(nodes, edges) {
  const outgoing = new Map(nodes.map(node => [node.id, new Set()]));
  const incoming = new Map(nodes.map(node => [node.id, new Set()]));
  for (const edge of edges) {
    if (edge.type !== 'prerequisite' || !outgoing.has(edge.source) || !outgoing.has(edge.target)) continue;
    outgoing.get(edge.source).add(edge.target);
    incoming.get(edge.target).add(edge.source);
  }
  return {outgoing, incoming};
}

// Collapse strongly connected components before ranking. A malformed cyclic
// prerequisite group stays on one level; its downstream concepts still advance.
function dependencyLevels(nodes, outgoing) {
  let index = 0;
  const discovered = new Map(), low = new Map(), stack = [], active = new Set();
  const components = [], componentOf = new Map();
  function visit(id) {
    discovered.set(id, index);
    low.set(id, index++);
    stack.push(id);
    active.add(id);
    for (const next of outgoing.get(id)) {
      if (!discovered.has(next)) {
        visit(next);
        low.set(id, Math.min(low.get(id), low.get(next)));
      } else if (active.has(next)) low.set(id, Math.min(low.get(id), discovered.get(next)));
    }
    if (low.get(id) !== discovered.get(id)) return;
    const component = [];
    let next;
    do {
      next = stack.pop();
      active.delete(next);
      componentOf.set(next, components.length);
      component.push(next);
    } while (next !== id);
    components.push(component);
  }
  for (const node of nodes) if (!discovered.has(node.id)) visit(node.id);
  const destinations = components.map(() => new Set());
  const indegree = components.map(() => 0);
  for (const [id, targets] of outgoing) {
    const from = componentOf.get(id);
    for (const target of targets) {
      const to = componentOf.get(target);
      if (from !== to && !destinations[from].has(to)) {
        destinations[from].add(to);
        indegree[to]++;
      }
    }
  }
  const ranks = components.map(() => 0);
  const queue = indegree.flatMap((count, i) => count === 0 ? [i] : []);
  for (let head = 0; head < queue.length; head++) {
    const current = queue[head];
    for (const next of destinations[current]) {
      ranks[next] = Math.max(ranks[next], ranks[current] + 1);
      if (--indegree[next] === 0) queue.push(next);
    }
  }
  return new Map(nodes.map(node => [node.id, ranks[componentOf.get(node.id)]]));
}

export function layoutFlow(nodes, edges) {
  const padding = 48, cardWidth = 224, cardHeight = 82, dx = 320, dy = 112;
  if (!nodes.length) return {nodes: [], width: padding * 2, height: padding * 2};
  const {outgoing, incoming} = prerequisiteGraph(nodes, edges);
  const levels = dependencyLevels(nodes, outgoing);
  const maxLevel = Math.max(...levels.values());
  const columns = Array.from({length: maxLevel + 1}, () => []);
  for (const node of nodes) columns[levels.get(node.id)].push(node);
  const positions = new Map();
  const refresh = () => columns.forEach(column => column.forEach((node, i) => positions.set(node.id, i)));
  refresh();
  // Alternating barycenter sweeps keep branches near their inputs and outputs.
  // Stable original order resolves ties, including disconnected source nodes.
  for (let pass = 0; pass < 4; pass++) {
    const forward = pass % 2 === 0;
    const order = Array.from({length: columns.length}, (_, i) => forward ? i : maxLevel - i);
    for (const level of order) {
      const weights = new Map(columns[level].map(node => {
        const adjacent = [...(forward ? incoming : outgoing).get(node.id)]
          .filter(id => levels.get(id) !== level);
        const average = adjacent.length ? adjacent.reduce((sum, id) => sum + positions.get(id), 0) / adjacent.length : positions.get(node.id);
        return [node.id, average];
      }));
      columns[level].sort((a, b) => weights.get(a.id) - weights.get(b.id) || positions.get(a.id) - positions.get(b.id));
      refresh();
    }
  }
  const maxRows = Math.max(...columns.map(column => column.length));
  const width = padding * 2 + cardWidth + maxLevel * dx;
  const height = padding * 2 + cardHeight + (maxRows - 1) * dy;
  const placed = new Map();
  columns.forEach((column, level) => column.forEach((node, row) => placed.set(node.id, {
    x: padding + cardWidth / 2 + level * dx,
    y: padding + cardHeight / 2 + ((maxRows - column.length) / 2 + row) * dy,
    level,
  })));
  return {nodes: nodes.map(node => ({...node, ...placed.get(node.id)})), width, height};
}

function hash(value) {
  let result = 2166136261;
  for (const character of String(value)) {
    result ^= character.codePointAt(0);
    result = Math.imul(result, 16777619);
  }
  return result >>> 0;
}

function random(seed) {
  let state = seed;
  return () => {
    state += 0x6D2B79F5;
    let value = state;
    value = Math.imul(value ^ value >>> 15, value | 1);
    value ^= value + Math.imul(value ^ value >>> 7, value | 61);
    return ((value ^ value >>> 14) >>> 0) / 4294967296;
  };
}

export function layoutNeural(nodes, edges, {width = 1200, height = 800, iterations = 150} = {}) {
  width = Number.isFinite(width) && width > 0 ? width : 1200;
  height = Number.isFinite(height) && height > 0 ? height : 800;
  iterations = Number.isFinite(iterations) ? Math.max(0, Math.min(240, Math.floor(iterations))) : 150;
  if (!nodes.length) return {nodes: [], width, height};
  if (nodes.length === 1) return {nodes: [{...nodes[0], x: width / 2, y: height / 2, level: 0}], width, height};
  const chapters = [...new Set(nodes.map(node => node.chapter ?? ''))].sort();
  const anchors = new Map(chapters.map((chapter, i) => {
    const angle = i / chapters.length * Math.PI * 2 - Math.PI / 2;
    const factor = chapters.length > 1 ? 1 : 0;
    return [chapter, {x: width / 2 + Math.cos(angle) * width * .30 * factor, y: height / 2 + Math.sin(angle) * height * .29 * factor}];
  }));
  const paddingX = Math.min(42, width / 4), paddingY = Math.min(42, height / 4);
  const particles = [...nodes].sort((a, b) => String(a.id).localeCompare(String(b.id))).map(node => {
    const anchor = anchors.get(node.chapter ?? '');
    const next = random(hash(node.id));
    const angle = next() * Math.PI * 2;
    const radius = (24 + next() * 84) * Math.min(1, Math.min(width, height) / 300);
    return {id: node.id, x: anchor.x + Math.cos(angle) * radius, y: anchor.y + Math.sin(angle) * radius, vx: 0, vy: 0, anchor};
  });
  const byId = new Map(particles.map(particle => [particle.id, particle]));
  const links = edges.filter(edge => edge.source !== edge.target && byId.has(edge.source) && byId.has(edge.target))
    .map(edge => ({source: byId.get(edge.source), target: byId.get(edge.target), strength: edge.type === 'prerequisite' ? .024 : .012}));
  const scale = Math.min(1, Math.min(width, height) / 500);
  for (let step = 0; step < iterations; step++) {
    const cooling = .15 + .85 * (1 - step / Math.max(1, iterations));
    for (const particle of particles) {
      particle.vx += (particle.anchor.x - particle.x) * .008 * cooling;
      particle.vy += (particle.anchor.y - particle.y) * .008 * cooling;
      particle.vx += (width / 2 - particle.x) * .0008 * cooling;
      particle.vy += (height / 2 - particle.y) * .0008 * cooling;
    }
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i], b = particles[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        if (Math.abs(dx) + Math.abs(dy) < .001) { dx = .01 * (i + 1); dy = .01 * (j + 1); }
        const distance2 = dx * dx + dy * dy;
        const distance = Math.sqrt(distance2);
        const repulsion = Math.min(6, 1350 * scale * scale / Math.max(64, distance2)) * cooling;
        const fx = dx / distance * repulsion, fy = dy / distance * repulsion;
        a.vx -= fx; a.vy -= fy;
        b.vx += fx; b.vy += fy;
      }
    }
    for (const {source, target, strength} of links) {
      const dx = target.x - source.x, dy = target.y - source.y;
      const distance = Math.max(.01, Math.hypot(dx, dy));
      const force = (distance - 96 * scale) * strength * cooling;
      const fx = dx / distance * force, fy = dy / distance * force;
      source.vx += fx; source.vy += fy;
      target.vx -= fx; target.vy -= fy;
    }
    for (const particle of particles) {
      particle.vx *= .68; particle.vy *= .68;
      const speed = Math.hypot(particle.vx, particle.vy);
      if (speed > 12) { particle.vx *= 12 / speed; particle.vy *= 12 / speed; }
      particle.x = Math.max(paddingX, Math.min(width - paddingX, particle.x + particle.vx));
      particle.y = Math.max(paddingY, Math.min(height - paddingY, particle.y + particle.vy));
    }
  }
  return {nodes: nodes.map(node => {
    const particle = byId.get(node.id);
    return {...node, x: Math.max(paddingX, Math.min(width - paddingX, particle.x)), y: Math.max(paddingY, Math.min(height - paddingY, particle.y)), level: 0};
  }), width, height};
}

export function layoutHierarchy(data, {collapsed = new Set(), width = 1400, height = 1100} = {}) {
  width = Number.isFinite(width) && width > 0 ? width : 1400;
  height = Number.isFinite(height) && height > 0 ? height : 1100;
  const leaves = data.nodes ?? [];
  const root = data.root ?? {id: 'fusion', title: '聚变知识树', url: '/'};
  const rootId = `root:${root.id ?? 'fusion'}`;
  const chapters = new Map((data.chapters ?? []).map(chapter => [chapter.id, {...chapter}]));
  const sections = new Map((data.sections ?? []).map(section => [section.id, {...section}]));
  // Missing metadata does not silently delete leaf nodes in a partial dataset.
  for (const node of leaves) {
    const chapter = node.chapter ?? 'uncategorized';
    const section = node.section ?? `uncategorized-${chapter}`;
    if (!chapters.has(chapter)) chapters.set(chapter, {id: chapter, title: node.chapterTitle ?? chapter});
    if (!sections.has(section)) sections.set(section, {id: section, title: node.sectionTitle ?? section, chapter});
  }
  for (const section of sections.values()) {
    const chapter = section.chapter ?? 'uncategorized';
    if (!chapters.has(chapter)) chapters.set(chapter, {id: chapter, title: chapter});
  }
  const tagsBySection = new Map([...sections.keys()].map(id => [id, []]));
  for (const node of leaves) tagsBySection.get(node.section ?? `uncategorized-${node.chapter ?? 'uncategorized'}`).push(node);
  const sectionsByChapter = new Map([...chapters.keys()].map(id => [id, []]));
  for (const section of sections.values()) sectionsByChapter.get(section.chapter ?? 'uncategorized').push(section);
  const countChapter = chapter => sectionsByChapter.get(chapter.id).reduce((sum, section) => sum + tagsBySection.get(section.id).length, 0);
  const chartChapters = [...chapters.values()];
  const center = {x: width / 2, y: height / 2};
  const scale = Math.min(1, Math.min(width, height) / 900);
  const radius = Math.max(1, Math.min(width / 2 - 105 * scale, height / 2 - 80 * scale));
  const chapterRadius = radius * .35;
  const sectionRadius = radius * .62;
  const outerInner = radius * .79;
  const outerDepth = radius * .21;
  const polar = (angle, distance) => ({x: center.x + Math.cos(angle) * distance, y: center.y + Math.sin(angle) * distance});
  const nodes = [{...root, id: rootId, nodeType: 'root', chapter: '', count: leaves.length, level: 0, radius: 42 * scale, ...center}];
  const membership = [], parents = new Map();
  const connect = (parent, child) => {
    parents.set(child, parent);
    membership.push({source: parent, target: child, type: 'membership', reason: '所属分类'});
  };
  const weights = chartChapters.map(chapter => 3 + Math.max(Math.sqrt(countChapter(chapter)), sectionsByChapter.get(chapter.id).length * 1.5));
  const totalWeight = weights.reduce((sum, weight) => sum + weight, 0) || 1;
  let start = -Math.PI / 2;
  chartChapters.forEach((chapter, chapterIndex) => {
    const span = weights[chapterIndex] / totalWeight * Math.PI * 2;
    const middle = start + span / 2;
    const chapterId = `chapter:${chapter.id}`;
    nodes.push({...chapter, id: chapterId, nodeType: 'chapter', chapter: chapter.id, count: countChapter(chapter), level: 1, radius: 26 * scale,
      ...polar(middle, chapterRadius)});
    connect(rootId, chapterId);
    const children = sectionsByChapter.get(chapter.id);
    const sectionWeights = children.map(section => 2 + Math.sqrt(tagsBySection.get(section.id).length));
    const sectionWeightTotal = sectionWeights.reduce((sum, weight) => sum + weight, 0) || 1;
    const chapterGap = Math.min(.055, span * .07);
    let sectionStart = start + chapterGap;
    children.forEach((section, sectionIndex) => {
      const sectionSpan = (span - chapterGap * 2) * sectionWeights[sectionIndex] / sectionWeightTotal;
      const sectionMiddle = sectionStart + sectionSpan / 2;
      const sectionId = `section:${section.id}`;
      const tags = tagsBySection.get(section.id);
      const seeded = random(hash(section.id));
      nodes.push({...section, id: sectionId, nodeType: 'section', chapter: chapter.id, section: section.id, count: tags.length, level: 2, radius: 15 * scale,
        ...polar(sectionMiddle, sectionRadius + (seeded() - .5) * 14 * scale)});
      connect(chapterId, sectionId);
      // Multiple radial bands give large topics enough space without widening
      // other branches; deterministic slight jitter makes the tree less rigid.
      const bands = Math.max(1, Math.min(4, Math.ceil(tags.length / Math.max(5, sectionSpan * outerInner / (29 * scale)))));
      const slots = Math.ceil(tags.length / bands);
      const leafGap = Math.min(.025, sectionSpan * .05);
      tags.forEach((tag, tagIndex) => {
        const band = tagIndex % bands;
        const slot = Math.floor(tagIndex / bands);
        const next = random(hash(tag.id));
        const jitter = (next() - .5) * Math.min(.022, sectionSpan / Math.max(1, slots) * .18);
        const fraction = slots === 1 ? .5 : (slot + .5 + (band % 2 ? .16 : -.16)) / slots;
        const angle = sectionStart + leafGap + fraction * (sectionSpan - leafGap * 2) + jitter;
        const depth = bands === 1 ? .55 + (next() - .5) * .45 : band / (bands - 1);
        nodes.push({...tag, nodeType: 'tag', level: 3, radius: 5.5 * scale,
          ...polar(angle, outerInner + depth * outerDepth + (next() - .5) * 8 * scale)});
        connect(sectionId, tag.id);
      });
      sectionStart += sectionSpan;
    });
    start += span;
  });
  // Limited local separation prevents small-sector circles from overlapping.
  // It operates on the full tree so collapsing a branch keeps other positions.
  const mobility = [0, .2, .6, 1];
  for (let pass = 0; pass < 16; pass++) {
    let moved = false;
    for (let i = 0; i < nodes.length; i++) for (let j = i + 1; j < nodes.length; j++) {
      const a = nodes[i], b = nodes[j];
      let dx = b.x - a.x, dy = b.y - a.y;
      const minimum = a.radius + b.radius + 8 * scale;
      const distance = Math.hypot(dx, dy);
      if (distance >= minimum) continue;
      if (distance < .0001) { dx = .01 * (i + 1); dy = .01 * (j + 1); }
      const actual = Math.hypot(dx, dy);
      const shift = (minimum - distance) / actual;
      const total = mobility[a.level] + mobility[b.level];
      if (!total) continue;
      const moveA = mobility[a.level] / total, moveB = mobility[b.level] / total;
      a.x -= dx * shift * moveA; a.y -= dy * shift * moveA;
      b.x += dx * shift * moveB; b.y += dy * shift * moveB;
      moved = true;
    }
    if (!moved) break;
  }
  const visible = nodes.filter(node => {
    let parent = parents.get(node.id);
    while (parent) {
      if (collapsed.has(parent)) return false;
      parent = parents.get(parent);
    }
    return true;
  });
  const ids = new Set(visible.map(node => node.id));
  const edges = [...membership, ...(data.edges ?? [])].filter(edge => ids.has(edge.source) && ids.has(edge.target));
  return {nodes: visible, edges, width, height};
}
