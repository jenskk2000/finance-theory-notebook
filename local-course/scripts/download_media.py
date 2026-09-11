"""Acquire official lecture recordings with resumable downloads and sample decoding."""
import concurrent.futures,hashlib,json,re,subprocess,sys,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.tools'))
import imageio_ffmpeg
FFMPEG=imageio_ffmpeg.get_ffmpeg_exe()
OUT=ROOT/'public/media'
INVENTORY=json.loads((ROOT.parent/'course-audit/inventory.json').read_text())
def acquire(session):
    name=f'session-{session["session"]:02d}' if session['session'] else 'interview'
    target=OUT/(name+'.mp4');part=OUT/(name+'.mp4.part')
    url=session['archive_url'].replace('http://www.archive.org/','https://archive.org/')
    result={'name':name,'session':session['session'],'url':url,'path':'/media/'+target.name,'youtube_id':session['youtube_id'],'segments':session['segments']}
    try:
        if not target.exists():
            cmd=['curl','--fail','--location','--retry','3','--retry-delay','2','--connect-timeout','30','--max-time','1800','--continue-at','-','--output',str(part),url]
            p=subprocess.run(cmd,capture_output=True,text=True)
            if p.returncode:raise RuntimeError(p.stderr[-700:])
            part.rename(target)
        probe=subprocess.run([FFMPEG,'-hide_banner','-i',str(target)],capture_output=True,text=True)
        match=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',probe.stderr)
        if not match or 'Video:' not in probe.stderr or 'Audio:' not in probe.stderr:raise RuntimeError('Missing duration or audio/video stream')
        h,m,s=map(float,match.groups());duration=h*3600+m*60+s
        checks=[]
        for pos in [0,duration/2,max(0,duration-5)]:
            check=subprocess.run([FFMPEG,'-v','error','-ss',str(pos),'-i',str(target),'-t','3','-f','null','-'],capture_output=True,text=True)
            checks.append({'at_seconds':round(pos,2),'ok':check.returncode==0 and not check.stderr.strip(),'error':check.stderr.strip()[:300]})
        result.update(bytes=target.stat().st_size,sha256=hashlib.file_digest(target.open('rb'),'sha256').hexdigest(),duration_seconds=duration,caption_end_seconds=session.get('caption_end_seconds'),sample_decode_checks=checks,status='ready' if all(c['ok'] for c in checks) else 'needs-review')
    except Exception as e:result.update(status='error',error=str(e))
    (OUT/(name+'.json')).write_text(json.dumps(result,indent=2))
    print(name,result['status'],result.get('bytes'),flush=True)
    return result
OUT.mkdir(parents=True,exist_ok=True)
ordered=sorted(INVENTORY['sessions'],key=lambda s:s['session'] if s['session'] else 99)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(acquire,ordered))
(OUT/'manifest.json').write_text(json.dumps({'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'validation':'HTTP transfer completion; stream metadata; 3-second decode samples at start, middle, end. Not exhaustive frame decoding.','recordings':results},indent=2))
print('COMPLETE',sum(r['status']=='ready' for r in results),'/',len(results),flush=True)
