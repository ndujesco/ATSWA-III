import { JSDOM } from 'jsdom'; import fs from 'fs';
const root=process.argv[2], sub=process.argv[3];
for (const n of process.argv.slice(4)) {
  const route=`#/s/${sub}/${n}`;
  const dom=new JSDOM(fs.readFileSync(root+'/index.html','utf8'),{runScripts:'dangerously',url:'http://localhost/'+route,
   beforeParse(w){Object.defineProperty(w.HTMLScriptElement.prototype,'src',{set(v){this.setAttribute('src',v);
    try{w.eval(fs.readFileSync(root+'/'+v,'utf8'));setTimeout(()=>this.dispatchEvent(new w.Event('load')),0);}catch(e){}},
    get(){return this.getAttribute('src');}});}});
  const w=dom.window; const errs=[];
  w.addEventListener('error',e=>errs.push(String(e.error||e.message)));
  await new Promise(r=>setTimeout(r,650)); w.location.hash=route;
  w.dispatchEvent(new w.Event('hashchange')); await new Promise(r=>setTimeout(r,650));
  const t=w.document.getElementById('view').textContent;
  const tex=[...new Set((t.match(/\\[a-zA-Z]{2,}/g)||[]))];
  console.log(`${sub} ch${n}: chars=${t.length} secs=${w.document.querySelectorAll('section.sec').length} eg=${w.document.querySelectorAll('.eg').length} rawTeX=${tex.length?tex.join(','):'none'} jsErr=${errs.length}`);
  dom.window.close();
}
