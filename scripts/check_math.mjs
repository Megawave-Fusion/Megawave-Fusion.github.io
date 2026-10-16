// Render every unique formula extracted from generated HTML with the vendored MathJax.
// Input JSON is produced by scripts/extract_math.py; this checks TeX, not physics.
import {createRequire} from 'node:module';
import {readFileSync,writeFileSync} from 'node:fs';
const require=createRequire(import.meta.url);
const {init}=require('../vendor/mathjax/node-main.js');
const math=await init({loader:{load:['input/tex','output/chtml']},tex:{packages:['base','ams','autoload','noundefined','newcommand']},startup:{typeset:false}});
const rows=JSON.parse(readFileSync('.build/reviews/math-input.json','utf8'));
const errors=[];
for(const row of rows){
 try{
  const node=await math.tex2chtmlPromise(row.tex,{display:row.display});
  const html=math.startup.adaptor.outerHTML(node);
  if(html.includes('mjx-merror') || html.includes('mjx-mtext') && /color: red/.test(html)) errors.push({...row,render:html.slice(0,1000)});
 }catch(error){errors.push({...row,error:String(error)})}
}
const report={formulas:rows.length,result:errors.length?'failed':'passed',errors,scope:'TeX syntax and MathJax conversion only; not correctness of physics'};
writeFileSync('.build/reviews/math-render.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({formulas:rows.length,errors:errors.length}));
if(errors.length)process.exitCode=1;
