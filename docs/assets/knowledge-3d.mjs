import * as THREE from './vendor/three/three.module.js';

const BACKGROUND = '#071522';
const DEFAULT_YAW = .38;
const DEFAULT_PITCH = .19;
const clamp = (value, low, high) => Math.max(low, Math.min(high, value));
const endpoint = value => typeof value === 'string' ? value : value?.id;
const isBranch = node => node.nodeType !== 'tag' && node.nodeType !== 'entry';

/** A WebGL2 renderer; all graph coordinates remain genuinely three dimensional. */
export class KnowledgeGraph3D {
  constructor(container, {onSelect = () => {}, onViewChange = () => {}} = {}) {
    if (!(container instanceof HTMLElement)) throw new TypeError('A graph container is required.');
    this.container = container;
    this.onSelect = onSelect;
    this.onViewChange = onViewChange;
    this.disposed = false;
    this.failed = false;
    this.width = 0;
    this.height = 0;
    this.yaw = DEFAULT_YAW;
    this.pitch = DEFAULT_PITCH;
    this.distance = 900;
    this.fitDistance = 900;
    this.target = new THREE.Vector3();
    this.fitCenter = new THREE.Vector3();
    this.fitRadius = 315;
    this.autoRotate = false;
    this.allLabels = false;
    this.selectedId = null;
    this.hoveredId = null;
    this.activeIds = null;
    this.pointers = new Map();
    this.nodes = new Map();
    this.edgeRecords = [];
    this.nodeMeshes = [];
    this.graphResources = [];
    this.frame = 0;
    this.lastTime = 0;
    this.dirty = true;
    this.hasGraph = false;
    this.needsInitialFit = true;
    this.labelHover = false;
    this.intersecting = true;
    this.abort = new AbortController();

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('webgl2', {antialias: true, alpha: false, powerPreference: 'high-performance'});
    if (!context) throw new Error('当前浏览器未提供 WebGL 2，无法显示真正的三维知识网络。请使用流程图或启用硬件加速后重试。');
    try {
      this.renderer = new THREE.WebGLRenderer({canvas, context, antialias: true, alpha: false});
    } catch (error) {
      context.getExtension('WEBGL_lose_context')?.loseContext();
      throw error;
    }
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.2;
    this.renderer.setClearColor(BACKGROUND, 1);
    this.canvas = canvas;
    canvas.className = 'kg3d-canvas';
    canvas.tabIndex = 0;
    canvas.setAttribute('aria-label', '三维聚变知识网络。拖动旋转；Shift 或右键拖动平移；滚轮缩放。方向键旋转，加减键缩放，Home 重置。触屏单指旋转，双指平移和缩放。点击球体或名称查看节点。');
    canvas.textContent = '三维知识网络需要支持 WebGL 2 的浏览器；也可切换到学习流程图。';
    this.labels = document.createElement('div');
    this.labels.className = 'kg3d-labels';
    this.labels.setAttribute('aria-label', '三维网络节点名称');
    container.classList.add('kg3d-surface');
    container.append(canvas, this.labels);
    Object.assign(container.dataset, {renderer: 'webgl', webglVersion: '2', threeVersion: THREE.REVISION,
      nodecount: '0', edgecount: '0', autoRotate: 'false', labels: 'false'});

    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(BACKGROUND);
    this.camera = new THREE.PerspectiveCamera(44, 1, .1, 20000);
    this.camera.up.set(0, 1, 0);
    this.scene.add(new THREE.HemisphereLight('#d9f4ff', '#101e35', 1.45));
    const key = new THREE.DirectionalLight('#f0fcff', 2.7);
    key.position.set(-300, 550, 700);
    this.scene.add(key);
    const rim = new THREE.DirectionalLight('#58a9ff', 1.2);
    rim.position.set(350, -150, -450);
    this.scene.add(rim);
    this.graphGroup = new THREE.Group();
    this.scene.add(this.graphGroup);
    this.sphereGeometry = new THREE.SphereGeometry(1, 24, 16);
    this.coneGeometry = new THREE.ConeGeometry(.9, 3.4, 7);
    this.glowTexture = this.makeGlowTexture();
    this.selectionMaterial = new THREE.MeshBasicMaterial({color: '#e9fcff', wireframe: true,
      transparent: true, opacity: .35, depthWrite: false});
    this.selectionShell = new THREE.Mesh(this.sphereGeometry, this.selectionMaterial);
    this.selectionShell.visible = false;
    this.scene.add(this.selectionShell);
    this.raycaster = new THREE.Raycaster();
    this.pointer = new THREE.Vector2();
    this.projected = new THREE.Vector3();
    this.tick = time => this.drawFrame(time);

    this.bindEvents();
    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(container);
    this.intersectionObserver = new IntersectionObserver(entries => {
      this.intersecting = entries[0]?.isIntersecting ?? true;
      if (this.intersecting) this.invalidate(); else this.cancelFrame();
    });
    this.intersectionObserver.observe(container);
    this.motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    this.listen(this.motion, 'change', event => { if (event.matches) this.setAutoRotate(false); });
    this.resize();
  }

  listen(target, type, callback, options = {}) {
    target.addEventListener(type, callback, {...options, signal: this.abort.signal});
  }

  makeGlowTexture() {
    const image = document.createElement('canvas');
    image.width = image.height = 64;
    const context = image.getContext('2d');
    const gradient = context.createRadialGradient(32, 32, 3, 32, 32, 31);
    gradient.addColorStop(0, 'rgba(255,255,255,.6)');
    gradient.addColorStop(.32, 'rgba(255,255,255,.23)');
    gradient.addColorStop(1, 'rgba(255,255,255,0)');
    context.fillStyle = gradient;
    context.fillRect(0, 0, 64, 64);
    return new THREE.CanvasTexture(image);
  }

  setGraph({nodes = [], edges = [], chapters = [], bounds} = {}) {
    if (this.disposed) return;
    const ids = new Set();
    for (const node of nodes) {
      if (!node.id || ids.has(node.id) || ![node.x, node.y, node.z, node.radius].every(Number.isFinite) || node.radius <= 0) {
        throw new Error('三维节点必须有唯一标识、有限的 x/y/z 坐标与正半径。');
      }
      ids.add(node.id);
    }
    for (const edge of edges) {
      if (!ids.has(endpoint(edge.source)) || !ids.has(endpoint(edge.target))) throw new Error('三维连线包含不可见或不存在的端点。');
    }
    this.clearGraph();
    const chapterColors = new Map(chapters.map(chapter => [chapter.id, chapter.color]));
    for (const node of nodes) {
      const color = new THREE.Color(node.nodeType === 'root' ? '#a2eeef' : node.color || chapterColors.get(node.chapter) || '#55a6c1');
      color.lerp(new THREE.Color('#daefff'), node.nodeType === 'tag' ? .15 : .1);
      const material = new THREE.MeshPhongMaterial({color, emissive: color, emissiveIntensity: .09,
        shininess: 75, specular: '#c0e0ef'});
      const mesh = new THREE.Mesh(this.sphereGeometry, material);
      mesh.position.set(node.x, node.y, node.z);
      mesh.scale.setScalar(node.radius);
      mesh.userData.nodeId = node.id;
      this.graphGroup.add(mesh);
      this.graphResources.push(material);
      this.nodeMeshes.push(mesh);
      let glow;
      if (isBranch(node)) {
        const glowMaterial = new THREE.SpriteMaterial({map: this.glowTexture, color,
          transparent: true, opacity: node.nodeType === 'root' ? .68 : .32,
          depthWrite: false, depthTest: true, blending: THREE.AdditiveBlending});
        glow = new THREE.Sprite(glowMaterial);
        glow.position.copy(mesh.position);
        glow.scale.setScalar(node.radius * 5);
        this.graphGroup.add(glow);
        this.graphResources.push(glowMaterial);
      }
      const label = document.createElement('button');
      label.type = 'button';
      label.className = `kg3d-label kg3d-label--${node.nodeType || 'tag'}`;
      label.dataset.node3d = node.id;
      label.dataset.nodeType = node.nodeType || 'tag';
      label.textContent = node.title;
      label.title = `${node.title} · ${node.id}`;
      label.setAttribute('aria-label', `${node.title}，${isBranch(node) ? '分组节点，查看与展开折叠' : node.id + '，查看条目'}`);
      label.style.setProperty('--node-color', '#' + color.getHexString());
      label.hidden = true;
      this.labels.append(label);
      const width = Math.min(196, 25 + [...node.title].reduce((sum, c) => sum + (c.charCodeAt(0) > 255 ? 12 : 6.5), 0));
      this.nodes.set(node.id, {node, mesh, color, label, glow, labelWidth: width});
    }
    this.buildEdges(edges);
    if (!this.nodes.has(this.hoveredId)) this.hoveredId = null;
    if (bounds && Number.isFinite(bounds.radius) && bounds.radius > 0 &&
        [bounds.center?.x, bounds.center?.y, bounds.center?.z].every(Number.isFinite)) {
      this.fitCenter.set(bounds.center.x, bounds.center.y, bounds.center.z);
      this.fitRadius = bounds.radius;
    } else if (nodes.length) {
      const box = new THREE.Box3();
      for (const node of nodes) {
        box.expandByPoint(new THREE.Vector3(node.x - node.radius, node.y - node.radius, node.z - node.radius));
        box.expandByPoint(new THREE.Vector3(node.x + node.radius, node.y + node.radius, node.z + node.radius));
      }
      const sphere = box.getBoundingSphere(new THREE.Sphere());
      this.fitCenter.copy(sphere.center);
      this.fitRadius = Math.max(sphere.radius, 30);
    }
    this.updateFitDistance();
    if (!this.hasGraph) {
      this.target.copy(this.fitCenter);
      this.distance = this.fitDistance;
      this.needsInitialFit = !this.width || !this.height;
    }
    this.hasGraph = true;
    Object.assign(this.container.dataset, {nodecount: String(nodes.length), edgecount: String(edges.length),
      tagcount: String(nodes.filter(node => !isBranch(node)).length)});
    this.applySelection();
    this.invalidate();
    this.notifyView();
  }

  buildEdges(edges) {
    const groups = new Map();
    let arrowCount = 0;
    for (const edge of edges) {
      const source = endpoint(edge.source), target = endpoint(edge.target);
      const a = this.nodes.get(source), b = this.nodes.get(target);
      const kind = edge.type || 'related';
      if (!groups.has(kind)) groups.set(kind, {positions: [], colors: [], records: []});
      const group = groups.get(kind);
      const direction = b.mesh.position.clone().sub(a.mesh.position).normalize();
      const start = a.mesh.position.clone().addScaledVector(direction, a.node.radius);
      const end = b.mesh.position.clone().addScaledVector(direction, -b.node.radius);
      const color = kind === 'membership' ? a.color.clone().lerp(b.color, .5) : new THREE.Color(kind === 'prerequisite' ? '#68b8d2' : '#8791b1');
      const record = {source, target, type: kind, color, offset: group.positions.length / 3, start, end,
        arrowIndex: kind === 'prerequisite' ? arrowCount++ : -1};
      group.positions.push(start.x, start.y, start.z, end.x, end.y, end.z);
      group.colors.push(color.r, color.g, color.b, color.r, color.g, color.b);
      group.records.push(record);
      this.edgeRecords.push(record);
    }
    for (const [kind, group] of groups) {
      const geometry = new THREE.BufferGeometry();
      geometry.setAttribute('position', new THREE.Float32BufferAttribute(group.positions, 3));
      const colors = new THREE.Float32BufferAttribute(group.colors, 3);
      geometry.setAttribute('color', colors);
      const LineMaterial = kind === 'related' ? THREE.LineDashedMaterial : THREE.LineBasicMaterial;
      const material = new LineMaterial({vertexColors: true, transparent: true,
        opacity: kind === 'membership' ? .52 : kind === 'prerequisite' ? .36 : .19,
        depthTest: true, depthWrite: false,
        ...(kind === 'related' ? {dashSize: 4.5, gapSize: 4} : {})});
      const lines = new THREE.LineSegments(geometry, material);
      if (kind === 'related') lines.computeLineDistances();
      this.graphGroup.add(lines);
      this.graphResources.push(geometry, material);
      for (const record of group.records) record.attribute = colors;
    }
    if (arrowCount) {
      const material = new THREE.MeshBasicMaterial({color: '#ffffff', transparent: true, opacity: .67, depthWrite: false});
      this.arrowMesh = new THREE.InstancedMesh(this.coneGeometry, material, arrowCount);
      const object = new THREE.Object3D();
      for (const edge of this.edgeRecords) if (edge.arrowIndex >= 0) {
        object.position.copy(edge.start).lerp(edge.end, .8);
        object.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), edge.end.clone().sub(edge.start).normalize());
        object.updateMatrix();
        this.arrowMesh.setMatrixAt(edge.arrowIndex, object.matrix);
        this.arrowMesh.setColorAt(edge.arrowIndex, edge.color);
      }
      this.arrowMesh.instanceMatrix.needsUpdate = true;
      this.graphResources.push(material);
      this.graphGroup.add(this.arrowMesh);
    }
  }

  setSelection({id = null, activeIds = null} = {}) {
    if (this.disposed) return;
    this.selectedId = id;
    this.activeIds = activeIds === null ? null : new Set(activeIds);
    this.applySelection();
    this.invalidate();
  }

  applySelection() {
    const active = id => !this.activeIds || this.activeIds.has(id) || id === this.selectedId;
    for (const [id, record] of this.nodes) {
      const selected = id === this.selectedId, hover = id === this.hoveredId, muted = !active(id);
      record.mesh.material.color.copy(record.color).multiplyScalar(muted ? .23 : 1);
      record.mesh.material.emissiveIntensity = muted ? .025 : selected ? .48 : hover ? .28 : .09;
      record.label.classList.toggle('is-selected', selected);
      record.label.classList.toggle('is-hovered', hover);
      record.label.classList.toggle('is-muted', muted);
      record.label.setAttribute('aria-pressed', String(selected));
      if (record.glow) record.glow.material.opacity = muted ? .06 : selected ? .7 : record.node.nodeType === 'root' ? .65 : .32;
    }
    for (const edge of this.edgeRecords) {
      const connected = edge.source === this.selectedId || edge.target === this.selectedId;
      const strength = !active(edge.source) || !active(edge.target) ? .14 : connected ? 1.7 : 1;
      const color = edge.color.clone().multiplyScalar(strength);
      edge.attribute.setXYZ(edge.offset, color.r, color.g, color.b);
      edge.attribute.setXYZ(edge.offset + 1, color.r, color.g, color.b);
      edge.attribute.needsUpdate = true;
      if (edge.arrowIndex >= 0) this.arrowMesh.setColorAt(edge.arrowIndex, color);
    }
    if (this.arrowMesh?.instanceColor) this.arrowMesh.instanceColor.needsUpdate = true;
    const selected = this.nodes.get(this.selectedId);
    this.selectionShell.visible = Boolean(selected);
    if (selected) {
      this.selectionShell.position.copy(selected.mesh.position);
      this.selectionShell.scale.setScalar(selected.node.radius * 1.2);
    }
    this.container.dataset.selected = this.selectedId || '';
    this.container.dataset.hovered = this.hoveredId || '';
  }

  setLabels(value) {
    this.allLabels = Boolean(value);
    this.container.dataset.labels = String(this.allLabels);
    this.invalidate();
  }

  setAutoRotate(value) {
    this.autoRotate = Boolean(value);
    this.container.dataset.autoRotate = String(this.autoRotate);
    this.lastTime = 0;
    this.invalidate();
    this.notifyView();
  }

  updateFitDistance() {
    const vertical = THREE.MathUtils.degToRad(this.camera.fov) / 2;
    const horizontal = Math.atan(Math.tan(vertical) * this.camera.aspect);
    this.fitDistance = this.fitRadius / Math.sin(Math.min(vertical, horizontal)) * 1.12;
  }

  resetView() {
    this.yaw = DEFAULT_YAW;
    this.pitch = DEFAULT_PITCH;
    this.target.copy(this.fitCenter);
    this.distance = this.fitDistance;
    this.invalidate();
    this.notifyView();
  }

  zoom(factor) {
    if (!Number.isFinite(factor) || factor <= 0) return;
    this.distance = clamp(this.distance / factor, Math.max(18, this.fitDistance * .09), this.fitDistance * 7);
    this.invalidate();
    this.notifyView();
  }

  focusNode(id) {
    const record = this.nodes.get(id);
    if (!record) return;
    this.target.copy(record.mesh.position);
    this.distance = Math.max(record.node.radius * 12, this.fitRadius * .42);
    this.invalidate();
    this.notifyView();
  }

  resize() {
    if (this.disposed) return;
    const previousZoom = this.fitDistance / this.distance;
    const {width, height} = this.container.getBoundingClientRect();
    this.width = Math.floor(width);
    this.height = Math.floor(height);
    if (this.width < 1 || this.height < 1) { this.cancelFrame(); return; }
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.setSize(this.width, this.height, false);
    this.camera.aspect = this.width / this.height;
    this.camera.updateProjectionMatrix();
    this.updateFitDistance();
    if (this.needsInitialFit) {
      this.target.copy(this.fitCenter);
      this.distance = this.fitDistance;
      if (this.hasGraph) this.needsInitialFit = false;
    } else this.distance = this.fitDistance / previousZoom;
    this.invalidate();
    this.notifyView();
  }

  canRender() {
    return !this.disposed && !this.failed && this.intersecting && !document.hidden &&
      this.width > 0 && this.height > 0 && this.container.isConnected;
  }

  invalidate() {
    this.dirty = true;
    if (!this.frame && this.canRender()) this.frame = requestAnimationFrame(this.tick);
  }

  cancelFrame() {
    if (this.frame) cancelAnimationFrame(this.frame);
    this.frame = 0;
    this.lastTime = 0;
  }

  updateCamera() {
    const horizontal = this.distance * Math.cos(this.pitch);
    this.camera.position.set(this.target.x + horizontal * Math.sin(this.yaw),
      this.target.y + this.distance * Math.sin(this.pitch), this.target.z + horizontal * Math.cos(this.yaw));
    this.camera.near = Math.max(.05, this.distance / 1500);
    this.camera.far = Math.max(this.fitDistance * 20, this.distance * 3 + this.fitRadius * 4);
    this.camera.lookAt(this.target);
    this.camera.updateProjectionMatrix();
    this.camera.updateMatrixWorld();
  }

  drawFrame(time) {
    this.frame = 0;
    if (!this.canRender()) return;
    const rotating = this.autoRotate && !this.pointers.size && !this.labelHover;
    if (rotating) this.yaw += (this.lastTime ? Math.min((time - this.lastTime) / 1000, .05) : 0) * .085;
    this.lastTime = time;
    if (this.dirty || rotating) {
      this.updateCamera();
      this.renderer.render(this.scene, this.camera);
      this.positionLabels();
      Object.assign(this.container.dataset, {yaw: this.yaw.toFixed(5), pitch: this.pitch.toFixed(5),
        zoom: (this.fitDistance / this.distance).toFixed(5), cameraDistance: this.distance.toFixed(3),
        drawcalls: String(this.renderer.info.render.calls), triangles: String(this.renderer.info.render.triangles)});
      this.dirty = false;
    }
    if (rotating) this.frame = requestAnimationFrame(this.tick);
  }

  positionLabels() {
    const candidates = [];
    const focal = this.height / (2 * Math.tan(THREE.MathUtils.degToRad(this.camera.fov) / 2));
    for (const [id, record] of this.nodes) {
      const {node, label, mesh} = record;
      const priority = id === this.selectedId ? 0 : id === this.hoveredId ? 1 : node.nodeType === 'root' ? 2 : node.nodeType === 'chapter' ? 3 : node.nodeType === 'section' ? 4 : 5;
      if (!this.allLabels && priority > 3) { label.hidden = true; continue; }
      this.projected.copy(mesh.position).project(this.camera);
      if (Math.abs(this.projected.x) > 1.05 || Math.abs(this.projected.y) > 1.05 || this.projected.z < -1 || this.projected.z > 1) {
        label.hidden = true; continue;
      }
      const distance = mesh.position.distanceTo(this.camera.position);
      const radius = node.radius * focal / Math.max(1, distance);
      const x = (this.projected.x + 1) * this.width / 2;
      const y = (1 - this.projected.y) * this.height / 2 + radius + 6;
      candidates.push({record, priority, distance, radius, x, y, depth: this.projected.z});
    }
    candidates.sort((a, b) => a.priority - b.priority || a.distance - b.distance);
    const occupied = [];
    for (const item of candidates) {
      const {record, priority, x, y, depth} = item;
      const box = {left: x - record.labelWidth / 2, right: x + record.labelWidth / 2, top: y, bottom: y + 24};
      const collision = occupied.some(other => box.left < other.right + 5 && box.right > other.left - 5 && box.top < other.bottom + 3 && box.bottom > other.top - 3);
      const clipped = box.bottom > this.height || box.top < 0 || box.right < 0 || box.left > this.width;
      // The selected/hovered label remains legible; other labels avoid overlap.
      if (clipped || (collision && priority > 1)) { record.label.hidden = true; continue; }
      occupied.push(box);
      record.label.hidden = false;
      record.label.style.left = `${x.toFixed(1)}px`;
      record.label.style.top = `${y.toFixed(1)}px`;
      record.label.style.zIndex = String(priority < 2 ? 3000 : Math.round((1 - depth) * 1000));
    }
    this.container.dataset.visiblelabels = String(occupied.length);
  }

  pick(clientX, clientY) {
    if (!this.width || !this.height || !this.nodeMeshes.length) return null;
    const rect = this.canvas.getBoundingClientRect();
    this.pointer.set((clientX - rect.left) / rect.width * 2 - 1, 1 - (clientY - rect.top) / rect.height * 2);
    this.updateCamera();
    this.scene.updateMatrixWorld(true);
    this.raycaster.setFromCamera(this.pointer, this.camera);
    return this.raycaster.intersectObjects(this.nodeMeshes, false)[0]?.object.userData.nodeId || null;
  }

  setHover(id) {
    if (this.hoveredId === id) return;
    this.hoveredId = id;
    this.canvas.classList.toggle('is-over-node', Boolean(id));
    this.applySelection();
    this.invalidate();
  }

  pan(dx, dy) {
    this.updateCamera();
    const unit = 2 * this.distance * Math.tan(THREE.MathUtils.degToRad(this.camera.fov) / 2) / Math.max(1, this.height);
    this.target.addScaledVector(new THREE.Vector3(1, 0, 0).applyQuaternion(this.camera.quaternion), -dx * unit);
    this.target.addScaledVector(new THREE.Vector3(0, 1, 0).applyQuaternion(this.camera.quaternion), dy * unit);
  }

  bindEvents() {
    this.listen(this.canvas, 'contextmenu', event => event.preventDefault());
    this.listen(this.canvas, 'pointerdown', event => {
      if (![0, 1, 2].includes(event.button)) return;
      event.preventDefault();
      this.canvas.focus({preventScroll: true});
      if (!this.pointers.size) { this.gestureMoved = false; this.hadMultiple = false; }
      this.pointers.set(event.pointerId, {x: event.clientX, y: event.clientY,
        startX: event.clientX, startY: event.clientY, button: event.button, shift: event.shiftKey});
      if (this.pointers.size > 1) { this.gestureMoved = true; this.hadMultiple = true; }
      this.canvas.setPointerCapture(event.pointerId);
      this.canvas.classList.add('is-dragging');
    });
    this.listen(this.canvas, 'pointermove', event => {
      const previous = this.pointers.get(event.pointerId);
      if (!previous) {
        if (event.pointerType !== 'touch') this.setHover(this.pick(event.clientX, event.clientY));
        return;
      }
      event.preventDefault();
      const before = [...this.pointers.values()].map(point => ({...point}));
      const dx = event.clientX - previous.x, dy = event.clientY - previous.y;
      previous.x = event.clientX; previous.y = event.clientY;
      if (Math.hypot(event.clientX - previous.startX, event.clientY - previous.startY) > 5) this.gestureMoved = true;
      if (this.pointers.size > 1) {
        const after = [...this.pointers.values()];
        const oldDistance = Math.hypot(before[0].x - before[1].x, before[0].y - before[1].y);
        const newDistance = Math.hypot(after[0].x - after[1].x, after[0].y - after[1].y);
        if (oldDistance > 1 && newDistance > 1) this.zoom(newDistance / oldDistance);
        this.pan((after[0].x + after[1].x - before[0].x - before[1].x) / 2,
          (after[0].y + after[1].y - before[0].y - before[1].y) / 2);
      } else if (this.gestureMoved) {
        if (previous.button !== 0 || previous.shift || event.shiftKey) this.pan(dx, dy);
        else { this.yaw -= dx * .006; this.pitch = clamp(this.pitch + dy * .005, -1.43, 1.43); }
      }
      this.invalidate();
    });
    const finish = event => {
      const point = this.pointers.get(event.pointerId);
      if (!point) return;
      const click = event.type === 'pointerup' && point.button === 0 && !this.gestureMoved && !this.hadMultiple;
      this.pointers.delete(event.pointerId);
      if (this.canvas.hasPointerCapture(event.pointerId)) this.canvas.releasePointerCapture(event.pointerId);
      if (!this.pointers.size) this.canvas.classList.remove('is-dragging');
      else for (const remaining of this.pointers.values()) { remaining.startX = remaining.x; remaining.startY = remaining.y; }
      if (click) {
        const id = this.pick(event.clientX, event.clientY);
        if (id) this.onSelect(id);
      }
      this.invalidate();
    };
    this.listen(this.canvas, 'pointerup', finish);
    this.listen(this.canvas, 'pointercancel', finish);
    this.listen(this.canvas, 'lostpointercapture', finish);
    this.listen(this.canvas, 'pointerleave', () => { if (!this.pointers.size) this.setHover(null); });
    this.listen(this.canvas, 'wheel', event => {
      event.preventDefault();
      const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? this.height : 1);
      this.zoom(Math.exp(-clamp(delta * .0012, -.7, .7)));
    }, {passive: false});
    this.listen(this.canvas, 'keydown', event => {
      const moves = {ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1]};
      if (moves[event.key]) {
        event.preventDefault();
        const [x, y] = moves[event.key];
        if (event.shiftKey) this.pan(x * 24, y * 24);
        else { this.yaw += x * .09; this.pitch = clamp(this.pitch + y * .08, -1.43, 1.43); }
        this.invalidate();
      } else if (['+', '=', '-', '_', 'Home', '0'].includes(event.key)) {
        event.preventDefault();
        if (event.key === 'Home' || event.key === '0') this.resetView();
        else this.zoom(event.key === '+' || event.key === '=' ? 1.15 : 1 / 1.15);
      }
    });
    this.listen(this.labels, 'click', event => {
      const label = event.target.closest('[data-node3d]');
      if (!label) return;
      event.stopPropagation();
      this.onSelect(label.dataset.node3d);
    });
    this.listen(this.labels, 'pointerover', event => {
      const label = event.target.closest('[data-node3d]');
      if (label) { this.labelHover = true; this.setHover(label.dataset.node3d); }
    });
    this.listen(this.labels, 'pointerout', event => {
      if (event.relatedTarget?.closest?.('[data-node3d]')) return;
      this.labelHover = false;
      this.setHover(null);
      this.invalidate();
    });
    this.listen(this.labels, 'focusin', event => { if (event.target.dataset.node3d) this.setHover(event.target.dataset.node3d); });
    this.listen(this.labels, 'focusout', () => this.setHover(null));
    this.listen(document, 'visibilitychange', () => { if (document.hidden) this.cancelFrame(); else this.invalidate(); });
    this.listen(this.canvas, 'webglcontextlost', event => {
      event.preventDefault();
      this.failed = true;
      this.cancelFrame();
      this.container.dataset.renderer = 'lost';
      this.labels.hidden = true;
      const error = document.createElement('p');
      error.className = 'kg3d-error';
      error.setAttribute('role', 'alert');
      error.textContent = '三维图形上下文已中断。请切换到流程图，或刷新页面重新加载 WebGL。';
      this.container.append(error);
      this.container.dispatchEvent(new CustomEvent('knowledge3derror', {bubbles: true,
        detail: {message: error.textContent}}));
    });
  }

  notifyView() {
    if (this.disposed) return;
    const zoom = this.fitDistance / this.distance;
    this.onViewChange({zoom, autoRotate: this.autoRotate});
  }

  clearGraph() {
    for (const resource of this.graphResources) resource.dispose();
    this.graphResources = [];
    if (this.arrowMesh) this.arrowMesh.dispose();
    this.arrowMesh = null;
    this.graphGroup.clear();
    this.nodes.clear();
    this.nodeMeshes = [];
    this.edgeRecords = [];
    this.labels.replaceChildren();
    this.labelHover = false;
  }

  dispose() {
    if (this.disposed) return;
    this.disposed = true;
    this.cancelFrame();
    this.abort.abort();
    this.resizeObserver.disconnect();
    this.intersectionObserver.disconnect();
    this.clearGraph();
    this.sphereGeometry.dispose();
    this.coneGeometry.dispose();
    this.glowTexture.dispose();
    this.selectionMaterial.dispose();
    this.renderer.dispose();
    this.renderer.forceContextLoss();
    this.canvas.remove();
    this.labels.remove();
    this.container.querySelectorAll('.kg3d-error').forEach(node => node.remove());
    this.container.classList.remove('kg3d-surface');
    this.container.dataset.renderer = 'disposed';
  }
}
