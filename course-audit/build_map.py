from pathlib import Path
import json,re,html,collections
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'course-audit'
D=json.loads((OUT/'inventory.json').read_text())
E=html.escape
BASE=D['source_url']
def anchor(path,title):return f'<a href="{E(path,quote=True)}">{E(title)}</a>'
def local(path,title):return anchor('../'+path,title)
def plain(s):return html.unescape(re.sub('<[^>]+>',' ',s))
def clock(s):
    s=int(float(s or 0));return f'{s//3600:02}:{s//60%60:02}:{s%60:02}'
assets={a['path']:a for a in D['assets']}
resources={p.parent.name:json.loads(p.read_text()) for p in (ROOT/'resources').glob('*/data.json')}
proposals=[
('Finance as decisions across time and uncertainty','Interactive household/company balance sheet and a decision map.'),
('Discounting, compounding, annuities, perpetuities and inflation','Cash-flow timeline with rate, timing and inflation controls; PV changes instantly.'),
('Bond prices, yield curves, duration and immunization','Bond price/yield curve, movable yield-curve points and duration hedge experiment.'),
('Dividend discount models, earnings and growth opportunities','Valuation waterfall showing how payout, reinvestment and growth change value.'),
('No-arbitrage pricing, carry and hedging','Spot/futures comparison with carry costs and a daily margin-account simulation.'),
('Calls, puts, strategies, replication and option pricing','Payoff builder and expandable binomial tree with replicating portfolio.'),
('Expected returns and measures of risk','Return distributions and repeated-path simulations with adjustable assumptions.'),
('Covariance, diversification and efficient portfolios','Two-asset portfolio lab: vary weights and correlation and trace the frontier.'),
('Systematic risk, beta, equilibrium returns and factor pricing','Security market line with beta controls and a factor-exposure diagram.'),
('Project cash flows, NPV, IRR and real options','Project cash-flow builder, NPV profile and staged-investment decision tree.'),
('Market efficiency, evidence and limits of predictability','Information-arrival simulation and an exercise distinguishing backtests from evidence.'),
('Connect valuation, risk and corporate decisions','Integrated decision case and concept map linking all preceding modules.')]
rec_slugs=['present-value-relations','mit15_401f08_rec02','equities-common-stocks','forward-and-futures-contracts','options','portfolio-theory','capital-asset-pricing-model','capital-budgeting']
rec_by_module={2:rec_slugs[0],3:rec_slugs[1],4:rec_slugs[2],5:rec_slugs[3],6:rec_slugs[4],8:rec_slugs[5],9:rec_slugs[6],10:rec_slugs[7]}
ps=next(a for a in D['assets'] if 'Problem_Sets.pdf' in a['path'])
ps_ranges={2:(7,14,42,48),3:(15,33,49,63),4:(34,41,64,72)}
sessions={}
for v in D['videos']:
    sid=str(v['session']) if v['session'] else 'interview'
    if sid not in sessions:sessions[sid]=dict(session=v['session'],youtube_id=v['youtube_id'],archive_url=v['archive_url'],segments=[])
    sessions[sid]['segments'].append(dict(title=v['title'],start=v['start'],end=v['end'],transcript=v['transcript'],captions=v['captions']))
    text=(ROOT/v['captions']).read_text()
    times=re.findall(r'(\d\d):(\d\d):(\d\d)[.,](\d\d\d)',text)
    if times:
        end=max(int(h)*3600+int(m)*60+int(s)+int(ms)/1000 for h,m,s,ms in times)
        sessions[sid]['caption_end_seconds']=end
D['sessions']=list(sessions.values())
missing=[]
for d in resources.values():
    if d.get('file') and not (ROOT/'static_resources'/Path(d['file']).name).exists():missing.append(d['file'])
D['missing_referenced_assets']=missing
D['interpretation']={'schema_change':'video_captions_file/video_transcript_file became language-tagged resource arrays; checked references unchanged','local_video_count':0,'byte_checked_files':142,'byte_matched_files':142,'pdf_files':57,'unique_pdf_hashes':49,'unique_lecture_transcripts':20,'unique_interview_transcripts':1,'topic_video_segments':28,'teaching_sessions':20,'video_playback_verified':False}
for m,(concept,visual) in zip(D['modules'],proposals):
    m['planned_concepts']=concept;m['proposed_visual']=visual
    m['recitation']=None
    if m['number'] in rec_by_module:
        r=resources[rec_by_module[m['number']]];m['recitation']={'title':r['title'],'path':'static_resources/'+Path(r['file']).name}
    if m['number'] in ps_ranges:
        a,b,c,d=ps_ranges[m['number']];m['problem_set']={'path':ps['path'],'question_pdf_pages':[a,b],'solution_pdf_pages':[c,d]}
    m['source_slide_mapping']=re.findall(r'<li>(.*?)</li>',m['source_content'],re.S)
(OUT/'inventory.json').write_text(json.dumps(D,indent=2,ensure_ascii=False))

cards=[]
for m in D['modules']:
    n=m['number'];ses=sorted(set(v['session'] for v in m['videos']))
    body=f'<p>{E(m["planned_concepts"])}</p><p class="proposal"><b>Proposed visual:</b> {E(m["proposed_visual"])}</p>'
    body+='<p>'+local(m['local_page'],'Original topic page')+' · '+anchor(m['source_url'],'MIT online')+'</p>'
    for a in m['pdfs']:body+='<p>'+local(a['path'],a['title'])+f' · {assets[a["path"]]["pages"]} PDF pages</p>'
    if m['recitation']:body+='<p>'+local(m['recitation']['path'],'Recitation: '+m['recitation']['title'])+'</p>'
    if n in ps_ranges:
        a,b,c,d=ps_ranges[n];body+=f'<p>Problem set: '+local(ps['path']+f'#page={a}',f'questions pp. {a}–{b}')+' · '+local(ps['path']+f'#page={c}',f'solutions pp. {c}–{d}')+'</p>'
    body+='<details><summary>Lecture segments, transcripts and slide coverage</summary>'
    for v in m['videos']:
        end=clock(v['end']) if v['end'] else 'end of recording';start=clock(v['start'])
        body+=f'<div class="segment"><b>{E(v["title"])}</b><p>Session {v["session"]} · {start} → {end}</p><p>'+local(v['transcript'],'Transcript PDF')+' · '+local(v['captions'],'Timestamped captions')+' · '+anchor(v['youtube_url']+'&t='+str(int(float(v['start'] or 0))),'Video online')+' · '+anchor(v['source_url'],'MIT segment')+'</p></div>'
    body+='<ul>'+''.join('<li>'+E(plain(s))+'</li>' for s in m['source_slide_mapping'])+'</ul></details>'
    cards.append(f'<article id="module-{n}" data-search="{E((m["title"]+" "+m["planned_concepts"]).lower())}"><span class="eyebrow">MODULE {n:02} · SESSIONS {", ".join(map(str,ses))}</span><h2>{E(m["title"])}</h2>{body}</article>')

aux='<h2>Supporting materials</h2>'
for page in ['syllabus','calendar','readings','recitations','problem-sets','exams','instructor-insights']:
    d=json.loads((ROOT/'pages'/page/'data.json').read_text())
    aux+=f'<details><summary>{E(d["title"])}</summary><p>'+local('pages/'+page+'/index.html','Local page')+' · '+anchor(BASE+'pages/'+page+'/','MIT online')+'</p>'
    for slug in re.findall(r'/resources/([^/]+)/index.html',d.get('content','')):
        r=resources[slug]
        if r.get('file'):aux+='<p>'+local('static_resources/'+Path(r['file']).name,r['title'])+'</p>'
    if page=='readings':aux+='<p>Bibliography is local. The textbook, three additional books and Wall Street Journal content are not included.</p>'
    if page=='instructor-insights':
        v=next(v for v in D['videos'] if not v['session']);aux+='<p>'+local(v['transcript'],'Interview transcript')+' · '+local(v['captions'],'Interview captions')+' · '+anchor(v['youtube_url'],'Interview online')+'</p>'
    aux+='</details>'

rows=[]
transcript_titles={v['transcript']:f'Session {v["session"]}: {v["title"]}' if v['session'] else 'Instructor interview transcript' for v in D['videos']}
for a in D['assets']:
    title=transcript_titles.get(a['path']) or ' / '.join(r['title'] for r in a['records']) or Path(a['path']).name
    rows.append('<tr><td>'+local(a['path'],title)+'</td><td>'+E(a['extension'])+'</td><td>'+str(a.get('pages','—'))+'</td><td>'+E(Path(a['path']).name)+'</td></tr>')
hours=sum(s.get('caption_end_seconds',0) for s in D['sessions'] if s['session'])/3600
body='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Finance Theory I · Course map</title><style>
:root{font-family:system-ui,-apple-system,sans-serif;color:#19332f;background:#f5f3eb;line-height:1.6}*{box-sizing:border-box}body{margin:0}main{max-width:1100px;margin:auto;padding:48px 24px}h1{font-size:clamp(36px,6vw,64px);line-height:1.1;letter-spacing:-2px;margin:16px 0}h2{line-height:1.25;font-size:23px}a{color:#17645d;text-underline-offset:3px}header p{max-width:780px}.eyebrow{font-size:12px;letter-spacing:1.5px;font-weight:700;color:#52665f}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:28px 0}.stat{border-top:2px solid #236459;padding-top:10px}.stat b{font-size:28px;display:block}.notice{background:#e8eddf;padding:20px 24px;border-radius:12px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}article{background:white;padding:26px;border:1px solid #dce1d6;border-radius:14px;scroll-margin-top:24px}.proposal{border-left:3px solid #b08e3d;padding-left:14px;color:#56614a}details{border-top:1px solid #dce1d6;padding:14px 0}summary{cursor:pointer;font-weight:650}.segment{padding:12px 0;border-bottom:1px dashed #dce1d6}.segment p{margin:4px 0}input{font:inherit;border:1px solid #99aaa0;border-radius:8px;padding:12px 16px;width:100%;margin:24px 0}section{margin-top:40px}.table-wrap{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}td,th{text-align:left;padding:10px;border-bottom:1px solid #dce1d6;vertical-align:top}td:last-child{overflow-wrap:anywhere;max-width:300px}footer{margin:40px 0;color:#52665f;font-size:13px}[hidden]{display:none!important}@media(max-width:720px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:1fr 1fr}main{padding:24px 16px}}@media print{details{display:block}.grid{display:block}article{break-inside:avoid;margin-bottom:15px}input{display:none}}
</style><main><header><span class="eyebrow">MIT OPENCOURSEWARE · ANDREW LO · FALL 2008</span><h1>Finance, mapped.</h1><p>A verified source map for a future visual, local course. Original teaching materials are linked below; visual learning activities are proposals, not finished lessons.</p><p>Checked against MIT on 9 September 2026. <a href="REPORT.md">Read the audit and build plan</a> · <a href="inventory.json">Full source inventory</a></p></header><div class="stats"><div class="stat"><b>12</b>topic modules</div><div class="stat"><b>20</b>lecture recordings</div><div class="stat"><b>49</b>distinct PDFs</div><div class="stat"><b>142 / 142</b>PDF & caption files match MIT</div></div>
<div class="notice"><b>Ready for a local rebuild.</b> All lecture transcripts, 12 lecture decks, 8 recitation decks, practice materials and interview text are present. Videos and referenced books are not stored locally. Multiple topic segments reuse a recording and its transcript; the map preserves their time ranges.</div>
<label for="search"><input id="search" type="search" placeholder="Filter modules: options, bonds, risk…" aria-label="Filter modules"></label><div class="grid">'''+''.join(cards)+'</div><p id="empty" hidden>No matching modules.</p><section>'+aux+'''</section><section><h2>What the modern course should feel like</h2><p>Predict an outcome → manipulate a visual model → read or watch the source explanation → solve an original problem → receive a hint or worked feedback → revisit the idea later.</p><p>Every AI explanation should point to the original PDF page or lecture timestamp. Preserve the 2008 context; label newly researched examples separately. Keep every original source reachable from its module.</p></section><section><details><summary>All 146 local course assets</summary><p>57 PDF files reduce to 49 unique PDFs. Caption variants are retained here; no originals were deleted. Page counts are physical PDF pages.</p><div class="table-wrap"><table><thead><tr><th>Material</th><th>Type</th><th>Pages</th><th>Original filename</th></tr></thead><tbody>'''+''.join(rows)+'''</tbody></table></div></details></section><footer>Source: MIT OpenCourseWare, 15.401 Finance Theory I. Original resource metadata identifies CC BY-NC-SA 4.0; individual credits remain in the original files. This map and proposed learning design are independent additions. File matching does not establish teaching quality, OCR accuracy or working video playback.</footer></main><script>const input=document.querySelector('#search');input.addEventListener('input',()=>{let count=0;document.querySelectorAll('article').forEach(el=>{el.hidden=!el.dataset.search.includes(input.value.toLowerCase().trim());if(!el.hidden)count++});document.querySelector('#empty').hidden=count>0});</script></html>'''
(OUT/'index.html').write_text(body)
print('HTML created; caption-derived lecture hours',round(hours,2),'missing references',missing)
print('Distinct PDF pages',sum(next(a['pages'] for a in D['assets'] if a['sha256']==h) for h in {a['sha256'] for a in D['assets'] if a['extension']=='.pdf'}))
