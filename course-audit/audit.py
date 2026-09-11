from pathlib import Path
import json, re, hashlib, urllib.request, urllib.parse, concurrent.futures, datetime
from collections import Counter, defaultdict
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'course-audit'
BASE='https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/'
def get(url):
    with urllib.request.urlopen(url,timeout=40) as r: return r.read()
def digest(b): return hashlib.sha256(b).hexdigest()
def save(name,data):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,indent=2,ensure_ascii=False))
def normalize(x):
    if isinstance(x,dict):return {k:normalize(v) for k,v in x.items()}
    if isinstance(x,list):return [normalize(v) for v in x]
    if isinstance(x,str):
        x=re.sub(r'(?:https://ocw.mit.edu)?/courses/15-401-finance-theory-i-fall-2008/', '',x)
        x=re.sub(r'(?:\.\./)+','',x).replace('./static_resources/','').replace('index.html','')
        return x
    return x
live_map=json.loads(get(BASE+'content_map.json'));save('evidence/live-content-map.json',live_map)
local_map=json.loads((ROOT/'content_map.json').read_text())
paths=set()
for v in live_map.values():
    if v and v.endswith('/data.json') and '/courses/15-401-finance-theory-i-fall-2008/' in v:
        paths.add(v.split('/courses/15-401-finance-theory-i-fall-2008/')[1])
paths.add('data.json')
def check(path):
    try:
        raw=get(BASE+path);live=json.loads(raw);save('evidence/live/'+path,live)
        lp=ROOT/path
        local=json.loads(lp.read_text()) if lp.exists() else None
        keys=sorted(k for k in set(live)|set(local or {}) if normalize(live.get(k))!=normalize((local or {}).get(k)))
        return dict(path=path,status='match' if not keys else 'different',different_fields=keys)
    except Exception as e:return dict(path=path,status='error',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: checks=list(pool.map(check,sorted(paths)))
save('evidence/metadata-comparison.json',checks)
print('METADATA',Counter(x['status'] for x in checks),flush=True)
resources={p.parent.name:json.loads(p.read_text()) for p in (ROOT/'resources').glob('*/data.json')}
assets=[]
for p in sorted((ROOT/'static_resources').iterdir()):
    if not p.is_file():continue
    records=[dict(slug=k,title=d.get('title'),uid=d.get('uid'),license=d.get('license')) for k,d in resources.items() if d.get('file') and Path(d['file']).name==p.name]
    a=dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=digest(p.read_bytes()),extension=p.suffix,records=records)
    if p.suffix=='.pdf':
        reader=PdfReader(p);texts=[pg.extract_text() or '' for pg in reader.pages]
        a.update(pages=len(texts),text_characters=sum(map(len,texts)))
        save('extracted/'+p.stem+'.json',dict(source=a['path'],sha256=a['sha256'],pages=[dict(page=i+1,text=t) for i,t in enumerate(texts)]))
    assets.append(a)
print('ASSETS',len(assets),flush=True)
def check_asset(a):
    if a['extension'] not in ('.pdf','.vtt','.srt','.webvtt'):return dict(path=a['path'],status='not-byte-checked')
    try:
        b=get(BASE+Path(a['path']).name)
        return dict(path=a['path'],status='match' if digest(b)==a['sha256'] else 'different',remote_sha256=digest(b),remote_bytes=len(b))
    except Exception as e:return dict(path=a['path'],status='error',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: asset_checks=list(pool.map(check_asset,assets))
save('evidence/asset-comparison.json',asset_checks)
print('BYTE CHECK',Counter(x['status'] for x in asset_checks),flush=True)
def links(s):return re.findall(r'href="[^"]*?/resources/([^/]+)/index.html"',s)
modules=[]
order=re.findall(r'video-lectures-and-slides/([^/]+)/index.html',json.loads((ROOT/'pages/video-lectures-and-slides/data.json').read_text())['content'])
allvideos=[]
for slug,d in resources.items():
    if d.get('resourcetype')!='Video':continue
    vf=d.get('video_files',{});youtube=d.get('video_metadata',{}).get('youtube_id')
    ar=vf.get('archive_url','');ses=re.search(r'ses(\d+)',ar)
    v=dict(slug=slug,title=d['title'],youtube_id=youtube,session=int(ses[1]) if ses else None,start=d.get('start_time'),end=d.get('end_time'),archive_url=ar,youtube_url='https://www.youtube.com/watch?v='+youtube if youtube else None,source_url=BASE+'resources/'+slug+'/',parent=d.get('parent_title'),local_video=False)
    for label,key in [('transcript','video_transcript_file'),('captions','video_captions_file')]:
        ref=vf.get(key);p=ROOT/'static_resources'/Path(ref).name if ref else None
        v[label]=str(p.relative_to(ROOT)) if p and p.exists() else None
    allvideos.append(v)
for i,slug in enumerate(order):
    d=json.loads((ROOT/'pages/video-lectures-and-slides'/slug/'data.json').read_text());r=links(d['content'])
    vids=[v for key in r for v in allvideos if v['slug']==key]
    pdfs=[dict(title=resources[key]['title'],path='static_resources/'+Path(resources[key]['file']).name) for key in r if resources[key].get('file_type')=='application/pdf']
    modules.append(dict(number=i+1,slug=slug,title=d['title'],source_url=BASE+'pages/video-lectures-and-slides/'+slug+'/',local_page='pages/video-lectures-and-slides/'+slug+'/index.html',videos=vids,pdfs=pdfs,source_content=d['content']))
duplicates=defaultdict(list)
for a in assets:duplicates[a['sha256']].append(a['path'])
manifest=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_url=BASE,local_map_count=len(local_map),live_map_count=len(live_map),new_uids=sorted(set(live_map)-set(local_map)),removed_uids=sorted(set(local_map)-set(live_map)),metadata_checks=checks,asset_checks=asset_checks,assets=assets,modules=modules,videos=allvideos,exact_duplicate_groups=[v for v in duplicates.values() if len(v)>1])
save('inventory.json',manifest)
for m in modules:print(m['number'],m['title'],[v['session'] for v in m['videos']],len(m['pdfs']))
print('VIDEOS',len(allvideos),'UNIQUE',len(set(v['youtube_id'] for v in allvideos)),'TRANSCRIPTS',sum(bool(v['transcript']) for v in allvideos))
print('DIFFERENCES',[x for x in checks if x['status']!='match'])
print('DUPLICATES',manifest['exact_duplicate_groups'])
