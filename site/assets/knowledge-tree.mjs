import {searchNodes, getNeighborhood, filterGraph, layoutFlow, layoutHierarchy} from './knowledge-core.mjs';

const root = document.querySelector('#knowledge-tree');
const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const NS = 'http://www.w3.org/2000/svg';
const iconNeural = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="m5 6 7 6 7-7M12 12l7 7M12 12l-8 6"/><circle cx="5" cy="6" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="12" cy="12" r="3"/><circle cx="19" cy="19" r="2"/><circle cx="4" cy="18" r="2"/></svg>';
const iconFlow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="2" y="8" width="6" height="8" rx="1"/><rect x="16" y="2" width="6" height="7" rx="1"/><rect x="16" y="15" width="6" height="7" rx="1"/><path d="M8 12h4V5h4M12 12v7h4"/></svg>';

async function start() {
  const response = await fetch(root.dataset.url || '/data/knowledge-graph.json');
  if (!response.ok) throw new Error('data unavailable');
  const data = await response.json();
  const byId = new Map(data.nodes.map(n => [n.id,n]));
  const chapters = new Map(data.chapters.map(c => [c.id,c]));
  const sections = new Map(data.sections.map(s => [s.id,s]));
  const params = new URLSearchParams(location.search);
  const state = {view:params.get('view') === 'flow' ? 'flow' : 'neural', selected:byId.has(params.get('tag')) ? params.get('tag') : '', chapter:chapters.has(params.get('chapter')) ? params.get('chapter') : '', path:data.paths.some(p=>p.id===params.get('path')) ? params.get('path') : '', mode:['ancestors','descendants','neighbors'].includes(params.get('mode')) ? params.get('mode') : 'all', labels:false, related:true, collapsed:new Set()};
  if (!state.selected) state.mode='all';
  if(state.view==='flow'&&!state.selected&&!state.chapter&&!state.path&&params.get('all')!=='1')state.path='icrh';
  let selectedGroup = '', visible, positions = new Map(), nodeElements = new Map(), edgeElements = [], viewport = {x:0,y:0,k:1}, graphSize = {width:1400,height:1100};
  let lastSize = {width:0,height:0};
  root.classList.add('kt');
  root.innerHTML = `<div class="kt-head"><div><p class="kt-eyebrow">KNOWLEDGE ATLAS / FUSION STACKS</p><h1>聚变知识树</h1><p class="kt-description">知识库 → 章节 → 专题 → Tag。逐层展开知识，在具体条目之间发现关联。</p></div><div class="kt-total"><b>${data.nodes.length}</b>永久 Tag · 四层知识网络</div></div>
    <div class="kt-controls"><div class="kt-controls-top"><div class="kt-switch" role="group" aria-label="知识树视图"><button type="button" data-view="neural">${iconNeural}神经网络</button><button type="button" data-view="flow">${iconFlow}学习流程</button></div><div class="kt-options"><label><input type="checkbox" id="kt-labels">全部标题</label><label><input type="checkbox" id="kt-related" checked>相关连线</label><button type="button" id="kt-reset">重置</button></div></div>
    <div class="kt-filter-row"><label class="kt-field kt-search-wrap">定位知识点<input type="search" id="kt-search" placeholder="搜索标题、ICRH 或 MF000016" autocomplete="off" aria-controls="kt-results" aria-expanded="false"><div class="kt-search-results" id="kt-results" hidden></div></label><label class="kt-field">章节<select id="kt-chapter"><option value="">全部章节</option>${data.chapters.map(c=>`<option value="${esc(c.id)}">${esc(c.title)}</option>`).join('')}</select></label><label class="kt-field">学习路线<select id="kt-path"><option value="">自由探索</option>${data.paths.map(p=>`<option value="${esc(p.id)}">${esc(p.title)}</option>`).join('')}</select></label></div><div class="kt-depth" id="kt-depth" role="group" aria-label="展开层级"><span>展开到</span><button type="button" data-depth="0">知识库</button><button type="button" data-depth="1">章节</button><button type="button" data-depth="2">专题</button><button type="button" data-depth="3" aria-pressed="true">Tag</button><small>点击大节点可单独展开 / 收起</small></div><div class="kt-route-note" id="kt-route-note"></div></div>
    <div class="kt-workspace" id="kt-workspace"><div class="kt-stage" id="kt-stage"><div class="kt-stage-header"><div><div class="kt-stage-kicker" id="kt-stage-title"></div><div class="kt-stage-count" id="kt-count" role="status" aria-live="polite"></div></div><span class="kt-badge" id="kt-badge"></span><button type="button" class="kt-mobile-jump" id="kt-jump">节点详情 ↓</button></div><svg class="kt-canvas" id="kt-canvas" tabindex="0" role="group" aria-label="可交互知识树。拖动平移，滚轮缩放；Tab选择节点，回车查看详情，方向键平移，加减键缩放。"><defs><marker id="kt-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#71a6b5"/></marker></defs><g id="kt-world"><g id="kt-edges"></g><g id="kt-nodes"></g></g></svg><p class="kt-empty" id="kt-empty" hidden>当前筛选没有节点。请切换章节或重置视图。</p><div class="kt-help">滚轮 / 双指缩放 · 拖动平移 · 点击节点探索</div><span class="kt-zoom-level" id="kt-zoom-level"></span><div class="kt-zoom" role="group" aria-label="画布控制"><button type="button" id="kt-minus" aria-label="缩小">−</button><button type="button" id="kt-plus" aria-label="放大">+</button><button type="button" class="kt-fit" id="kt-fit">适应画布</button><button type="button" id="kt-fullscreen" aria-label="全屏知识树">⛶</button></div></div><aside class="kt-inspector" id="kt-inspector" aria-label="节点详情" tabindex="-1"></aside></div>
    <div class="kt-legend"><span class="kt-legend-item"><i class="kt-legend-line arrow"></i>建议先学 → 后续知识</span><span class="kt-legend-item"><i class="kt-legend-line dashed"></i>主题相关</span><span class="kt-legend-item"><i class="kt-legend-line member"></i>层级归属</span><span>总节点 → 大章节 → 中专题 → 小 Tag</span></div><div class="kt-chapter-legend" aria-label="章节颜色">${data.chapters.map(c=>`<button type="button" data-legend="${esc(c.id)}"><i class="kt-swatch" style="--color:${esc(c.color)}"></i>${esc(c.title)}</button>`).join('')}</div><p class="kt-footnote">${esc(data.note || '学习关系由编者整理，是阅读建议，不是严格或完整的先修条件；没有连线不表示知识无关。')} 神经网络按四级组织展开；流程图按 Tag 之间的学习关系分层。功能参考<a href="https://wuli.wiki/apps/tree2/brain.html" target="_blank" rel="noopener">小时百科知识树</a>，布局与实现为本站独立编写。<a href="/contents/">查看文字目录 →</a></p>`;
  const $ = id => root.querySelector('#'+id);
  const svg=$('kt-canvas'), world=$('kt-world'), stage=$('kt-stage'), panel=$('kt-inspector'), results=$('kt-results');
  const color = n => chapters.get(n.chapter || n.id)?.color || '#70aebc';
  const degree = new Map(data.nodes.map(n=>[n.id,0]));
  data.edges.forEach(e=>{degree.set(e.source,(degree.get(e.source)||0)+1);degree.set(e.target,(degree.get(e.target)||0)+1);});

  function updateURL() {
    const url = new URL(location.href); url.search='';
    url.searchParams.set('view',state.view);
    if(state.selected) url.searchParams.set('tag',state.selected);
    if(state.chapter) url.searchParams.set('chapter',state.chapter);
    if(state.path) url.searchParams.set('path',state.path);
    if(state.mode!=='all') url.searchParams.set('mode',state.mode);
    if(state.view==='flow'&&!state.path&&!state.chapter&&!state.selected)url.searchParams.set('all','1');
    history.replaceState(null,'',url);
  }
  function syncControls() {
    root.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.view===state.view));
    $('kt-chapter').value=state.chapter; $('kt-path').value=state.path;
    $('kt-labels').checked=state.labels; $('kt-related').checked=state.related;
    $('kt-labels').disabled=state.view==='flow';
    const depth=state.collapsed.size===0?'3':state.collapsed.has('root:'+data.root.id)?'0':data.chapters.every(c=>state.collapsed.has('chapter:'+c.id))?'1':data.sections.every(s=>state.collapsed.has('section:'+s.id))?'2':'';
    root.querySelectorAll('[data-depth]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.depth===depth)));
    root.querySelectorAll('[data-legend]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.legend===state.chapter));
    stage.dataset.view=state.view;
    $('kt-depth').hidden=state.view!=='neural';
    $('kt-stage-title').textContent=state.view==='neural'?'NEURAL VIEW / 知识连接':'FLOW VIEW / 学习方向';
    $('kt-badge').textContent=state.view==='neural'?'ROOT → CHAPTER → TOPIC → TAG':'先学 → 后学';
    const path=data.paths.find(p=>p.id===state.path);
    $('kt-route-note').textContent=path?path.description:state.mode!=='all'&&state.selected?`${{'ancestors':'前置知识','descendants':'后续学习','neighbors':'直接关联'}[state.mode]} · ${byId.get(state.selected).title}`:state.view==='flow'&&!state.selected?'全图概览：建议选择一条学习路线，或搜索 Tag，查看可读的局部流程。':'';
    updateURL();
  }
  function svgElement(tag,attrs={},text='') {
    const element=document.createElementNS(NS,tag);
    for(const [key,value] of Object.entries(attrs)) element.setAttribute(key,value);
    if(text) element.textContent=text;
    return element;
  }
  function wrapTitle(text, limit=14) {
    const chars=Array.from(text); const lines=[];
    for(let i=0;i<chars.length && lines.length<2;i+=limit) lines.push(chars.slice(i,i+limit).join(''));
    if(chars.length>limit*2) lines[1]=lines[1].slice(0,-1)+'…';
    return lines;
  }
  function addNode(n) {
    const branch=!!n.nodeType&&n.nodeType!=='tag',flow=state.view==='flow';
    const group=svgElement('g',{'class':`kt-node ${branch?'is-'+n.nodeType:flow?'kt-flow-node':''}`,'data-node':n.id,transform:`translate(${n.x} ${n.y})`,tabindex:'0',role:'button','aria-label':branch?`${n.title}，${{root:'知识库总',chapter:'章节大',section:'专题中'}[n.nodeType]}节点，${n.count}个Tag，点击展开或收起`:`${n.id} ${n.title}，${n.sectionTitle}`});
    group.append(svgElement('title',{},branch?`${n.title} · ${n.count} 个 Tag`:`${n.id} · ${n.title}\n${n.sectionTitle}`));
    if(branch)group.setAttribute('aria-expanded',String(!state.collapsed.has(n.id)));
    if(flow){
      group.append(svgElement('rect',{x:-112,y:-41,width:224,height:82,rx:6}));
      group.append(svgElement('path',{d:'M-109 -31v62',stroke:color(n),'stroke-width':3,'stroke-linecap':'round'}));
      group.append(svgElement('text',{x:-96,y:-23,class:'kt-card-tag'},n.id));
      const lines=wrapTitle(n.title,stage.clientWidth<460?10:14);
      lines.forEach((line,i)=>group.append(svgElement('text',{x:-96,y:lines.length===1?1:-3+i*17,class:'kt-card-title'},line)));
      group.append(svgElement('text',{x:-96,y:31,class:'kt-card-chapter'},n.chapterTitle));
    } else {
      const radius=branch?({root:43,chapter:26,section:16}[n.nodeType]):Math.min(10,5+Math.sqrt(degree.get(n.id)||0)); n.radius=radius;
      group.append(svgElement('circle',{r:radius+7,fill:color(n),stroke:color(n),class:'kt-node-ring'}));
      group.append(svgElement('circle',{r:radius,fill:branch?'#163c4c':color(n),stroke:color(n),class:'kt-node-core'}));
      if(branch) group.append(svgElement('text',{y:5,fill:'#d4e9ea','text-anchor':'middle','font-size':n.nodeType==='section'?11:14,'font-family':'ui-monospace,monospace'},n.nodeType==='root'?'FUSION':String(n.count)));
      group.append(svgElement('text',{y:radius+24,class:'kt-node-label'},n.title.length>16?n.title.slice(0,15)+'…':n.title));
      group.append(svgElement('text',{y:radius+39,class:'kt-node-tag'},branch?(state.collapsed.has(n.id)?'展开 +':'收起 −'):n.id));
    }
    group.addEventListener('click',()=>{
      if(suppressClick) return;
      if(branch){selectedGroup=n.id;state.selected='';state.mode='all';toggleGroup(n.id);}
      else selectNode(n.id,false);
    });
    group.addEventListener('keydown',event=>{
      if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();group.dispatchEvent(new MouseEvent('click',{bubbles:true}));}
    });
    $('kt-nodes').append(group); nodeElements.set(n.id,group);
  }
  function edgePath(edge) {
    const a=positions.get(edge.source), b=positions.get(edge.target); if(!a||!b)return '';
    if(state.view==='flow'){
      if(edge.type==='related') return `M${a.x},${a.y+41} Q${(a.x+b.x)/2},${Math.max(a.y,b.y)+100} ${b.x},${b.y+41}`;
      if(state.path&&Math.abs(a.y-b.y)>50){const y1=a.y+41,y2=b.y-41,mid=(y1+y2)/2;return `M${a.x},${y1} C${a.x},${mid} ${b.x},${mid} ${b.x},${y2}`;}
      const direction=b.x>=a.x?1:-1,x1=a.x+112*direction,x2=b.x-112*direction;
      const bend=Math.max(45,(x2-x1)*.5);
      return `M${x1},${a.y} C${x1+bend*direction},${a.y} ${x2-bend*direction},${b.y} ${x2},${b.y}`;
    }
    const dx=b.x-a.x,dy=b.y-a.y,d=Math.max(1,Math.hypot(dx,dy));
    const ra=a.radius||8,rb=(b.radius||8)+4;
    const x1=a.x+dx/d*ra,y1=a.y+dy/d*ra,x2=b.x-dx/d*rb,y2=b.y-dy/d*rb;
    return `M${x1},${y1} Q${(x1+x2)/2-dy*.07},${(y1+y2)/2+dx*.07} ${x2},${y2}`;
  }
  function updateEdges(){edgeElements.forEach(({edge,element})=>element.setAttribute('d',edgePath(edge)));}
  function renderGraph() {
    syncControls();
    visible=filterGraph(data,{chapter:state.chapter,focus:state.selected,mode:state.mode,path:state.path});
    let edges=visible.edges.filter(e=>state.related||e.type!=='related');
    const selectedChapters=new Set(visible.nodes.map(n=>n.chapter)),selectedSections=new Set(visible.nodes.map(n=>n.section));
    let layout;
    if(state.view==='flow'&&state.path){
      const order=data.paths.find(p=>p.id===state.path).nodes;
      const columns=stage.clientWidth<460?2:3;
      const ordered=order.map(id=>visible.nodes.find(n=>n.id===id)).filter(Boolean);
      layout={nodes:ordered.map((n,i)=>{const row=Math.floor(i/columns),column=row%2?columns-1-i%columns:i%columns;return {...n,x:136+column*300,y:90+row*160,level:i};}),width:columns*300-28,height:Math.ceil(ordered.length/columns)*160+20};
    } else layout=state.view==='flow'?layoutFlow(visible.nodes,edges):layoutHierarchy({...data,chapters:data.chapters.filter(c=>selectedChapters.has(c.id)),sections:data.sections.filter(s=>selectedSections.has(s.id)),nodes:visible.nodes,edges},{collapsed:state.collapsed,width:1400,height:1100});
    positions=new Map(layout.nodes.map(n=>[n.id,{...n}])); graphSize={width:layout.width,height:layout.height};
    if(state.view==='neural')edges=layout.edges;
    nodeElements.clear(); edgeElements=[];$('kt-nodes').replaceChildren();$('kt-edges').replaceChildren();
    for(const n of positions.values())addNode(n);
    edges.forEach(edge=>{const element=svgElement('path',{class:'kt-edge '+edge.type,d:edgePath(edge)});if(edge.type==='prerequisite')element.setAttribute('marker-end','url(#kt-arrow)');$('kt-edges').append(element);edgeElements.push({edge,element});});
    const tags=[...positions.values()].filter(n=>!n.nodeType||n.nodeType==='tag').length;
    const groups=positions.size-tags;
    $('kt-count').textContent=`${tags} / ${data.nodes.length} 个 Tag${groups?' · '+groups+' 个上层节点':''} · ${edges.filter(e=>e.type!=='membership').length} 条知识关系`;
    $('kt-empty').hidden=!!positions.size;
    refreshSelection(); fit(); renderPanel();
  }
  function refreshSelection(){
    const neighborhood=state.selected&&state.mode==='all'?getNeighborhood(data.nodes,data.edges,state.selected,'neighbors'):null;
    for(const [id,g] of nodeElements){
      const n=positions.get(id),branch=!!n.nodeType&&n.nodeType!=='tag',chosen=id===state.selected||id===selectedGroup;
      g.classList.toggle('is-selected',chosen);
      g.classList.toggle('is-muted',!!neighborhood&&!neighborhood.has(id)&&!(branch&&(n.nodeType==='root'||n.chapter===byId.get(state.selected)?.chapter)));
      g.setAttribute('aria-pressed',String(chosen));
      if(state.view==='neural'){
        const show=n.nodeType==='root'||n.nodeType==='chapter'||chosen||state.labels||(n.nodeType==='section'&&viewport.k>=.8)||(!branch&&viewport.k>=1.5&&neighborhood?.has(id));
        g.querySelector('.kt-node-label').style.display=show?'':'none';
        g.querySelector('.kt-node-tag').style.display=chosen||state.labels||(branch&&viewport.k>=.8)?'':'none';
      }
    }
    edgeElements.forEach(({edge,element})=>{const connected=edge.source===state.selected||edge.target===state.selected;element.classList.toggle('is-active',!!state.selected&&connected);element.classList.toggle('is-muted',!!neighborhood&&!connected);});
  }
  function selectNode(id,reveal=true){
    if(!byId.has(id))return;
    const prior=state.mode;state.selected=id;selectedGroup='';
    if(reveal){state.chapter='';state.path='';state.mode='all';state.collapsed.delete('root:'+data.root.id);state.collapsed.delete('chapter:'+byId.get(id).chapter);state.collapsed.delete('section:'+byId.get(id).section);}
    $('kt-search').value='';results.hidden=true;$('kt-search').setAttribute('aria-expanded','false');
    if(reveal||prior!=='all')renderGraph();else{refreshSelection();renderPanel();syncControls();}
    if(reveal)centerOn(id,state.view==='flow'?.95:1.2);
  }
  function toggleGroup(id){
    const restoreFocus=document.activeElement?.dataset.node===id;
    if(state.collapsed.has(id))state.collapsed.delete(id);else state.collapsed.add(id);
    root.querySelectorAll('[data-depth]').forEach(b=>b.setAttribute('aria-pressed','false'));
    renderGraph();
    if(restoreFocus)nodeElements.get(id)?.focus({preventScroll:true});
  }
  function relationList(title,edges,direction){
    if(!edges.length)return '';
    return `<section class="kt-relations"><h3>${title} · ${edges.length}</h3>${edges.map(e=>{const n=byId.get(direction==='incoming'?e.source:direction==='outgoing'?e.target:e.source===state.selected?e.target:e.source);return `<button type="button" class="kt-relation" data-select="${n.id}">${esc(n.title)}<small>${n.id} · ${esc(n.sectionTitle)}</small><span class="kt-reason">${esc(e.reason)}</span></button>`;}).join('')}</section>`;
  }
  function renderPanel(){
    if(selectedGroup){
      const [type,key]=selectedGroup.split(':'),c=type==='root'?data.root:type==='chapter'?chapters.get(key):sections.get(key);
      const members=data.nodes.filter(n=>type==='root'||(type==='chapter'?n.chapter===key:n.section===key)),collapsed=state.collapsed.has(selectedGroup);
      panel.innerHTML=`<div class="kt-panel-kicker">${{root:'ROOT / 知识库总节点',chapter:'CHAPTER / 章节大节点',section:'TOPIC / 专题中节点'}[type]}</div><span class="kt-tag">${members.length} 个永久 Tag</span><h2>${esc(c.title)}</h2><p>${esc(c.description||'知识按章节、专题和永久条目逐层组织。层级归属连线不表示先修关系。')}</p><div class="kt-panel-actions"><button type="button" data-toggle-group="${selectedGroup}">${collapsed?'展开下一级':'收起下级节点'}</button>${type==='chapter'?`<button type="button" data-chapter-only="${key}">只看本章</button>`:''}</div><a class="kt-open" href="${esc(c.url)}">进入${{root:'知识库',chapter:'章节',section:'专题'}[type]} →</a><section class="kt-relations"><h3>所属 Tag</h3>${members.map(n=>`<button type="button" class="kt-relation" data-select="${n.id}">${esc(n.title)}<small>${n.id} · ${esc(n.sectionTitle)}</small></button>`).join('')}</section>`;
      return;
    }
    const n=byId.get(state.selected);
    if(!n){panel.innerHTML=`<div class="kt-panel-kicker">START EXPLORING</div><h2>知识，连成一张网。</h2><p>从知识库总节点，逐层展开章节、专题，直到最小的 Tag。点击任意上层节点可以展开或收起分支。</p><p>点击小节点，查看它的永久 Tag、正文与学习关联。</p><div class="kt-path-buttons">${data.paths.map(p=>`<button type="button" class="kt-path-button" data-route="${p.id}">${esc(p.title)}<small>${p.nodes.length} 个 Tag · 查看学习路线 →</small></button>`).join('')}</div><section class="kt-relations"><h3>怎么读这张图</h3><p>实线箭头从建议先学的条目指向后续条目。虚线表示主题关联，不代表先后顺序。</p><p>流程图按学习关系分层；神经网络同时呈现层级与跨章节连接。</p></section>`;return;}
    const incoming=data.edges.filter(e=>e.type==='prerequisite'&&e.target===n.id),outgoing=data.edges.filter(e=>e.type==='prerequisite'&&e.source===n.id),related=data.edges.filter(e=>e.type==='related'&&(e.source===n.id||e.target===n.id));
    panel.innerHTML=`<div class="kt-panel-kicker">TAG / 最小知识节点</div><span class="kt-tag">${n.id}</span><h2>${esc(n.title)}</h2><div class="kt-chapter-line"><i class="kt-swatch" style="--color:${esc(color(n))}"></i>${esc(n.sectionTitle)}</div><p>${esc(n.summary)}</p><div class="kt-review-status">${esc(n.statusLabel||{'draft':'草稿 · 待领域审核','reviewing':'审核中','reviewed':'已审核','archived':'已归档'}[n.status])}</div><a class="kt-open" href="${esc(n.url)}">阅读这个 Tag 的正文 ↗</a><div class="kt-panel-actions">${[['neighbors','直接关联'],['ancestors','前置知识'],['descendants','后续学习'],['all','显示全图']].map(([mode,label])=>`<button type="button" data-mode="${mode}" aria-pressed="${state.mode===mode}">${label}</button>`).join('')}</div>${relationList('建议先学',incoming,'incoming')}${relationList('后续知识',outgoing,'outgoing')}${relationList('主题相关',related,'related')}${!incoming.length&&!outgoing.length&&!related.length?'<p>该 Tag 的学习关系尚未编排，可直接进入正文。</p>':''}`;
  }
  function transform(){world.setAttribute('transform',`translate(${viewport.x} ${viewport.y}) scale(${viewport.k})`);$('kt-zoom-level').textContent=Math.round(viewport.k*100)+'%';refreshSelection();}
  function size(){return {width:stage.clientWidth,height:stage.clientHeight};}
  function fit(){
    const s=size();lastSize=s;
    const points=[...positions.values()],flow=state.view==='flow';
    const left=points.length?Math.min(...points.map(n=>n.x-(flow?124:75))):0;
    const right=points.length?Math.max(...points.map(n=>n.x+(flow?124:75))):graphSize.width;
    const top=points.length?Math.min(...points.map(n=>n.y-(flow?55:55))):0;
    const bottom=points.length?Math.max(...points.map(n=>n.y+(flow?55:75))):graphSize.height;
    const k=Math.max(.035,Math.min(1.2,(s.width-35)/(right-left),(s.height-100)/(bottom-top)));
    viewport={x:s.width/2-(left+right)/2*k,y:s.height/2-(top+bottom)/2*k+10,k};transform();
  }
  function centerOn(id,scale){const p=positions.get(id);if(!p)return;const s=size();viewport={x:s.width/2-p.x*scale,y:s.height/2-p.y*scale,k:scale};transform();}
  function zoom(factor,x,y){const s=size();x??=s.width/2;y??=s.height/2;const k=Math.max(.035,Math.min(4,viewport.k*factor)),ratio=k/viewport.k;viewport={x:x-(x-viewport.x)*ratio,y:y-(y-viewport.y)*ratio,k};transform();}
  function route(id){state.path=id;state.chapter='';state.mode='all';state.selected='';selectedGroup='';state.collapsed.clear();renderGraph();}
  root.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>{state.view=b.dataset.view;if(state.view==='flow'){selectedGroup='';if(!state.selected&&!state.chapter&&!state.path)state.path='icrh';}renderGraph();if(state.selected&&state.mode==='all')centerOn(state.selected,state.view==='flow'?.95:1.2);}));
  $('kt-chapter').addEventListener('change',event=>{state.chapter=event.target.value;state.path='';state.mode='all';state.selected='';selectedGroup='';state.collapsed.clear();renderGraph();});
  $('kt-path').addEventListener('change',event=>route(event.target.value));
  root.querySelectorAll('[data-legend]').forEach(b=>b.addEventListener('click',()=>{state.chapter=state.chapter===b.dataset.legend?'':b.dataset.legend;state.path='';state.mode='all';state.selected='';selectedGroup='';state.collapsed.clear();renderGraph();}));
  root.querySelectorAll('[data-depth]').forEach(b=>b.addEventListener('click',()=>{state.collapsed.clear();selectedGroup='';state.selected='';state.mode='all';const depth=Number(b.dataset.depth);if(depth===0)state.collapsed.add('root:'+data.root.id);if(depth===1)data.chapters.forEach(c=>state.collapsed.add('chapter:'+c.id));if(depth===2)data.sections.forEach(s=>state.collapsed.add('section:'+s.id));root.querySelectorAll('[data-depth]').forEach(button=>button.setAttribute('aria-pressed',String(button===b)));renderGraph();}));
  $('kt-labels').addEventListener('change',e=>{state.labels=e.target.checked;refreshSelection();});
  $('kt-related').addEventListener('change',e=>{state.related=e.target.checked;renderGraph();});
  $('kt-reset').addEventListener('click',()=>{state.selected='';state.chapter='';state.path='';state.mode='all';state.labels=false;state.related=true;state.collapsed.clear();selectedGroup='';$('kt-search').value='';results.hidden=true;$('kt-search').setAttribute('aria-expanded','false');renderGraph();});
  panel.addEventListener('click',event=>{
    const b=event.target.closest('button');if(!b)return;
    if(b.dataset.select)selectNode(b.dataset.select);
    if(b.dataset.route)route(b.dataset.route);
    if(b.dataset.mode){state.mode=b.dataset.mode;state.chapter='';state.path='';state.collapsed.clear();renderGraph();}
    if(b.dataset.toggleGroup)toggleGroup(b.dataset.toggleGroup);
    if(b.dataset.chapterOnly){state.chapter=b.dataset.chapterOnly;state.path='';state.mode='all';state.collapsed.delete('chapter:'+state.chapter);renderGraph();}
  });
  $('kt-jump').addEventListener('click',()=>{panel.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'nearest'});panel.focus({preventScroll:true});});
  $('kt-search').addEventListener('input',()=>{
    const q=$('kt-search').value.trim(),matches=q?searchNodes(data.nodes,q):[];
    results.hidden=!q;$('kt-search').setAttribute('aria-expanded',String(!!q));
    results.innerHTML=matches.length?matches.slice(0,30).map(n=>`<button type="button" data-result="${n.id}">${esc(n.title)}<small>${n.id} · ${esc(n.sectionTitle)}</small></button>`).join(''):`<div class="kt-search-empty">没有找到匹配的 Tag，试试标题、ICRH 或永久编号。</div>`;
    if(matches.length>30)results.insertAdjacentHTML('beforeend',`<div class="kt-search-empty">共 ${matches.length} 个匹配，显示前 30 个，请继续输入以缩小范围。</div>`);
  });
  results.addEventListener('click',e=>{const b=e.target.closest('[data-result]');if(b)selectNode(b.dataset.result);});
  $('kt-search').addEventListener('keydown',e=>{if(e.key==='ArrowDown'&&!results.hidden){e.preventDefault();results.querySelector('button')?.focus();}if(e.key==='Enter'&&!results.hidden){e.preventDefault();const b=results.querySelector('button');if(b)selectNode(b.dataset.result);}if(e.key==='Escape'){results.hidden=true;$('kt-search').setAttribute('aria-expanded','false');}});
  results.addEventListener('keydown',e=>{const buttons=[...results.querySelectorAll('button')],i=buttons.indexOf(document.activeElement);if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();buttons[(i+(e.key==='ArrowDown'?1:-1)+buttons.length)%buttons.length]?.focus();}if(e.key==='Escape'){results.hidden=true;$('kt-search').setAttribute('aria-expanded','false');$('kt-search').focus();}});
  document.addEventListener('click',e=>{if(!e.target.closest('.kt-search-wrap')){results.hidden=true;$('kt-search').setAttribute('aria-expanded','false');}});
  $('kt-plus').addEventListener('click',()=>zoom(1.35));$('kt-minus').addEventListener('click',()=>zoom(1/1.35));$('kt-fit').addEventListener('click',fit);
  let previousOverflow='';
  function expanded(value){
    const workspace=$('kt-workspace');
    if(value){previousOverflow=document.body.style.overflow;document.body.style.overflow='hidden';}else document.body.style.overflow=previousOverflow;
    workspace.classList.toggle('is-expanded',value);$('kt-fullscreen').setAttribute('aria-label',value?'退出全屏':'全屏知识树');fit();
  }
  $('kt-fullscreen').addEventListener('click',async()=>{
    if($('kt-workspace').classList.contains('is-expanded')){expanded(false);return;}
    try{if(document.fullscreenElement)await document.exitFullscreen();else if(document.fullscreenEnabled)await $('kt-workspace').requestFullscreen();else expanded(true);}catch{expanded(true);}
  });
  document.addEventListener('keydown',event=>{if(event.key==='Escape'&&$('kt-workspace').classList.contains('is-expanded'))expanded(false);});
  document.addEventListener('fullscreenchange',()=>{$('kt-fullscreen').setAttribute('aria-label',document.fullscreenElement?'退出全屏':'全屏知识树');fit();});
  svg.addEventListener('wheel',event=>{event.preventDefault();const r=svg.getBoundingClientRect();zoom(Math.exp(-Math.max(-100,Math.min(100,event.deltaY))*.006),event.clientX-r.left,event.clientY-r.top);},{passive:false});
  const pointers=new Map();let gesture=null,suppressClick=false;
  const local=e=>{const r=svg.getBoundingClientRect();return {x:e.clientX-r.left,y:e.clientY-r.top};};
  function beginGesture(event){
    const points=[...pointers.values()];
    if(points.length>=2){const a=points[0],b=points[1];gesture={type:'pinch',distance:Math.hypot(a.x-b.x,a.y-b.y),mid:{x:(a.x+b.x)/2,y:(a.y+b.y)/2},viewport:{...viewport}};}
    else if(points.length){const target=event?.target.closest?.('[data-node]'),node=target&&positions.get(target.dataset.node);gesture={type:node&&state.view==='neural'?'node':'pan',node,origin:{...points[0]},viewport:{...viewport},point:node?{x:node.x,y:node.y}:null};}
  }
  svg.addEventListener('pointerdown',event=>{if(event.button!==0&&event.pointerType!=='touch')return;pointers.set(event.pointerId,local(event));suppressClick=false;beginGesture(event);});
  svg.addEventListener('pointermove',event=>{
    if(!pointers.has(event.pointerId)||!gesture)return;pointers.set(event.pointerId,local(event));const points=[...pointers.values()];
    if(gesture.type==='pinch'&&points.length>=2){const a=points[0],b=points[1],mid={x:(a.x+b.x)/2,y:(a.y+b.y)/2},k=Math.max(.035,Math.min(4,gesture.viewport.k*Math.hypot(a.x-b.x,a.y-b.y)/Math.max(1,gesture.distance))),ratio=k/gesture.viewport.k;viewport={x:mid.x-(gesture.mid.x-gesture.viewport.x)*ratio,y:mid.y-(gesture.mid.y-gesture.viewport.y)*ratio,k};suppressClick=true;transform();return;}
    const p=points[0],dx=p.x-gesture.origin.x,dy=p.y-gesture.origin.y;if(Math.hypot(dx,dy)>4){suppressClick=true;if(!svg.hasPointerCapture(event.pointerId))svg.setPointerCapture(event.pointerId);}
    if(gesture.type==='node'){gesture.node.x=gesture.point.x+dx/viewport.k;gesture.node.y=gesture.point.y+dy/viewport.k;nodeElements.get(gesture.node.id).setAttribute('transform',`translate(${gesture.node.x} ${gesture.node.y})`);updateEdges();}
    else{viewport.x=gesture.viewport.x+dx;viewport.y=gesture.viewport.y+dy;transform();}
  });
  function endPointer(event){pointers.delete(event.pointerId);if(svg.hasPointerCapture(event.pointerId))svg.releasePointerCapture(event.pointerId);if(pointers.size)beginGesture();else gesture=null;setTimeout(()=>{if(!pointers.size)suppressClick=false;},0);}
  svg.addEventListener('pointerup',endPointer);svg.addEventListener('pointercancel',endPointer);
  svg.addEventListener('keydown',event=>{if(event.key==='+'||event.key==='='){event.preventDefault();zoom(1.3);}if(event.key==='-'){event.preventDefault();zoom(1/1.3);}if(event.key==='0'){event.preventDefault();fit();}const offsets={ArrowLeft:[40,0],ArrowRight:[-40,0],ArrowUp:[0,40],ArrowDown:[0,-40]};if(offsets[event.key]){event.preventDefault();viewport.x+=offsets[event.key][0];viewport.y+=offsets[event.key][1];transform();}});
  new ResizeObserver(()=>{const s=size();if(s.width!==lastSize.width||s.height!==lastSize.height){if(state.view==='flow'&&state.path&&(s.width<460)!==(lastSize.width<460))renderGraph();else fit();}}).observe(stage);
  renderGraph();
  if(state.selected&&state.mode==='all')centerOn(state.selected,state.view==='flow'?.95:1.2);
}
if(root) start().catch(()=>{root.innerHTML='<div class="empty"><h1>知识树暂时未能加载</h1><p>请刷新后重试，也可以先使用<a href="/contents/">完整文字目录</a>。</p><button type="button" id="kt-retry">重新加载</button></div>';root.querySelector('#kt-retry').addEventListener('click',()=>location.reload());});
