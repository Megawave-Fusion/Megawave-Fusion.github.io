// Animated toroidal geometry, not an equilibrium or a particle simulation.
const canvas = document.querySelector('#plasma-canvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  const motion = document.querySelector('#plasma-motion');
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  let paused = preference.matches, frame = 0, last = 0, phase = 0, width = 0, height = 0;
  let tilt = -.58, turn = -.25, pointerX = 0, pointerY = 0;
  const project = (u, v, r = .32) => {
    const radius = 1 + r * Math.cos(v);
    const x = radius * Math.cos(u), y = radius * Math.sin(u), z = r * Math.sin(v);
    const a = turn + pointerX * .2, t = tilt + pointerY * .12;
    const X = x * Math.cos(a) - y * Math.sin(a), Y = x * Math.sin(a) + y * Math.cos(a);
    const Z = Y * Math.sin(t) + z * Math.cos(t);
    const depth = Y * Math.cos(t) - z * Math.sin(t);
    const scale = Math.min(width / 3.1, height / 2.35);
    return [width / 2 + X * scale, height / 2 + Z * scale, depth];
  };
  const curve = (fn, color, lineWidth = 1, samples = 150) => {
    ctx.beginPath();
    for (let i = 0; i <= samples; i++) {
      const p = fn(i / samples * Math.PI * 2);
      if (i) ctx.lineTo(p[0], p[1]); else ctx.moveTo(p[0], p[1]);
    }
    ctx.strokeStyle = color; ctx.lineWidth = lineWidth; ctx.stroke();
  };
  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.save();
    ctx.strokeStyle = '#47718420'; ctx.lineWidth = .7;
    for (let i = 0; i < width; i += 28) {ctx.beginPath();ctx.moveTo(i, 0);ctx.lineTo(i, height);ctx.stroke();}
    for (let i = 0; i < height; i += 28) {ctx.beginPath();ctx.moveTo(0, i);ctx.lineTo(width, i);ctx.stroke();}
    ctx.globalCompositeOperation = 'screen';
    for (let i = 0; i < 24; i++) {
      const u = i * Math.PI / 12;
      curve(v => project(u, v, .38), '#69c5dc27', .8, 55);
    }
    for (let i = 0; i < 9; i++) {
      const v = i * Math.PI * 2 / 9;
      curve(u => project(u, v), '#a0bbdc20', .8);
    }
    ctx.shadowBlur = 12; ctx.shadowColor = '#e684c4';
    for (let i = 0; i < 6; i++) {
      curve(u => project(u, 4 * u + i * Math.PI / 3 + phase * .4, .27),
        i % 2 ? '#ff8bcf79' : '#79eff2a0', 1.2, 210);
    }
    ctx.shadowBlur = 7;
    for (let i = 0; i < 17; i++) {
      const u = phase * .5 + i * Math.PI * 2 / 17;
      const p = project(u, 4 * u + phase * .4, .27);
      ctx.fillStyle = '#d5ffff'; ctx.beginPath();ctx.arc(p[0], p[1], i % 4 ? 1.3 : 2, 0, Math.PI * 2);ctx.fill();
    }
    ctx.restore();
  }
  function tick(now) {
    frame = 0;
    if (paused || document.hidden) return;
    if (now - last > 32) {phase += Math.min(now - last, 80) * .0008;last = now;draw();}
    frame = requestAnimationFrame(tick);
  }
  function update() {
    motion.textContent = paused ? '播放动画' : '暂停动画';
    cancelAnimationFrame(frame);frame = 0;
    if (!paused && !document.hidden) {last = performance.now();frame = requestAnimationFrame(tick);}
    else draw();
  }
  if (ctx) {
    new ResizeObserver(() => {
      const box = canvas.getBoundingClientRect();width = box.width;height = box.height;
      const dpr = Math.min(devicePixelRatio || 1, 1.5);
      canvas.width = Math.round(width * dpr);canvas.height = Math.round(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);draw();
    }).observe(canvas);
    canvas.parentElement.classList.add('ready');motion.hidden = false;
    motion.addEventListener('click', () => {paused = !paused;update();});
    canvas.addEventListener('pointermove', event => {
      const rect = canvas.getBoundingClientRect();
      pointerX = (event.clientX - rect.left) / rect.width - .5;
      pointerY = (event.clientY - rect.top) / rect.height - .5;
      if (paused) draw();
    });
    canvas.addEventListener('pointerleave', () => {pointerX = pointerY = 0;if (paused) draw();});
    preference.addEventListener('change', event => {paused = event.matches;update();});
    document.addEventListener('visibilitychange', update);update();
  }
}
