import {searchEntries, normalize} from './search-core.mjs';
const figureLinks = document.querySelectorAll('.figure-link');
if (figureLinks.length && typeof HTMLDialogElement !== 'undefined') {
  const viewer = document.createElement('dialog');viewer.className = 'figure-viewer';
  const bar = document.createElement('div');bar.className = 'figure-viewer-bar';
  const title = document.createElement('p');title.id = 'figure-viewer-title';
  const close = document.createElement('button');close.type = 'button';close.textContent = '关闭图示 ×';
  const viewport = document.createElement('div');viewport.className = 'figure-viewport';
  const image = document.createElement('img');viewport.append(image);bar.append(title,close);
  viewer.append(bar,viewport);viewer.setAttribute('aria-labelledby',title.id);document.body.append(viewer);
  close.addEventListener('click',()=>viewer.close());
  viewer.addEventListener('click',event=>{if(event.target===viewer)viewer.close();});
  for (const link of figureLinks) link.addEventListener('click',event=>{
    if(event.ctrlKey || event.metaKey || event.shiftKey || event.altKey)return;
    event.preventDefault();
    const source=link.querySelector('img');image.src=link.href;image.alt=source.alt;
    title.textContent=source.alt;viewer.showModal();viewport.scrollTop=viewport.scrollLeft=0;
  });
}
for (const button of document.querySelectorAll('[data-expand]')) {
  button.addEventListener('click', () => {
    for (const row of document.querySelectorAll('details.chapter-row')) row.open = button.dataset.expand === 'true';
  });
}
for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const value = button.dataset.copy === 'url' ? document.querySelector('link[rel=canonical]').href :
      document.getElementById(button.dataset.copy).textContent;
    try {await navigator.clipboard.writeText(value);button.textContent='已复制';}
    catch {button.textContent='复制未成功，请手动选择';}
  });
}
document.addEventListener('keydown', event => {
  if (event.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) {
    event.preventDefault();document.querySelector('#global-query').focus();
  }
});
const results = document.querySelector('#search-results');
if (results) {
  const form = document.querySelector('.global-search');
  const query = document.querySelector('#global-query');
  const chapter = document.querySelector('#chapter-filter');
  const kind = document.querySelector('#kind-filter');
  const status = document.querySelector('#search-status');
  const more = document.querySelector('#show-more');
  const params = new URLSearchParams(location.search);
  query.value=params.get('q') || '';chapter.value=params.get('chapter') || '';kind.value=params.get('kind') || '';
  let entries = [], matches = [], visible=0;
  function snippet(text, q) {
    const needle=normalize(q).split(/\s+/).find(Boolean) || '';
    const at=normalize(text).indexOf(needle);
    const start=Math.max(0,at-45);
    return (start?'…':'')+text.slice(start,start+190)+(text.length>start+190?'…':'');
  }
  function append() {
    const subset=matches.slice(visible,visible+30);visible+=subset.length;
    for(const entry of subset) {
      const article=document.createElement('article');article.className='search-result';
      const meta=document.createElement('div');meta.className='result-tags';
      if(entry.tag){const tag=document.createElement('span');tag.className='tag';tag.textContent=entry.tag;meta.append(tag);}
      const context=document.createElement('span');context.textContent=`${entry.chapter_title || '站点文档'} / ${entry.section_title || entry.kind}`;meta.append(context);
      const title=document.createElement('h2');const link=document.createElement('a');link.href=entry.url;link.textContent=entry.title;title.append(link);
      const excerpt=document.createElement('p');excerpt.textContent=snippet(entry.text,query.value);
      article.append(meta,title,excerpt);results.append(article);
    }
    more.hidden=visible>=matches.length;
  }
  function render() {
    const qs=new URLSearchParams();if(query.value.trim())qs.set('q',query.value.trim());if(chapter.value)qs.set('chapter',chapter.value);if(kind.value)qs.set('kind',kind.value);
    history.replaceState(null,'',location.pathname+(qs.size?'?'+qs.toString():''));
    matches=searchEntries(entries,query.value,chapter.value,kind.value);visible=0;results.replaceChildren();
    status.textContent=`${query.value.trim()?'“'+query.value.trim()+'”：':''}找到 ${matches.length} 个结果`;
    if(!matches.length){const empty=document.createElement('p');empty.className='empty';empty.textContent='没有匹配的内容。可尝试中文名称、ICRH 等缩写，或完整的永久标签。';results.append(empty);}
    append();
  }
  try {
    const response=await fetch('/search-index.json');if(!response.ok)throw new Error(`HTTP ${response.status}`);
    entries=await response.json();render();
    form.addEventListener('submit',event=>{event.preventDefault();render();});
    let timer;query.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(render,180);});
    chapter.addEventListener('change',render);kind.addEventListener('change',render);more.addEventListener('click',append);
  } catch(error) {status.textContent='搜索索引暂时无法读取，请刷新页面或使用完整目录。';more.hidden=true;console.error(error);}
}
