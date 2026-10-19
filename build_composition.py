import json,html
from pathlib import Path
p=Path(__file__).parent
edit=json.loads((p/'edit.json').read_text())
dur=edit['duration'];caps=edit['captions'];chapters=edit['chapters']
speaker=html.escape(edit.get('speaker', 'Speaker'))
role=html.escape(edit.get('role', 'Role'))
def timed(id,start,end,track,cls,text):
 return f'<div id="{id}" class="clip {cls}" data-start="{start:.3f}" data-duration="{end-start:.3f}" data-track-index="{track}">{text}</div>'
parts=[]
parts.append(timed('brand',0,dur,3,'brand','HUMANS <span>OF NEO</span>'))
parts.append(timed('hook',0.1,5.6,4,'hook','Marcom. HR. Tech.<span>Trở lại để dẫn dắt.</span>'))
parts.append(timed('identity',5.7,12.7,4,'identity',f'<span class="eyebrow">HUMANS OF NEO</span><strong>{speaker}</strong><span class="role">{role}</span>'))
for i,c in enumerate(chapters):parts.append(timed('chapter-'+str(i),c['start'],c['end'],5,'chapter',html.escape(c['text'])))
for i,c in enumerate(caps):parts.append(timed('cap-'+str(i),c['start'],c['end'],6,'caption','<span>'+html.escape(c['text'])+'</span>'))
parts.append(timed('endcard',dur-2.0,dur,7,'endmark',f'HUMANS OF NEO <span>{speaker} · {role}</span>'))
style='''@font-face{font-family:"Be Vietnam Pro";src:url("assets/BeVietnamPro-SemiBold.ttf")}*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;overflow:hidden;background:#101C1A}#root{width:1080px;height:1920px;position:relative;font-family:"Be Vietnam Pro";color:#F7F8F2}video{position:absolute;width:1080px;height:1920px;object-fit:cover;inset:0}.clip{position:absolute}.brand{top:100px;left:72px;font-size:30px;letter-spacing:3px;padding:15px 21px;background:#101C1A;border-left:5px solid #A6E5C7}.brand span{color:#A6E5C7}.hook{top:225px;left:72px;max-width:900px;font-size:68px;line-height:1.25;letter-spacing:-2px;text-shadow:0 3px 18px #101C1A}.hook span{display:block;color:#A6E5C7}.identity{left:72px;top:1115px;width:840px;padding:25px 32px;background:#101C1A;border-left:6px solid #A6E5C7}.identity .eyebrow{display:block;font-size:23px;letter-spacing:3px;color:#A6E5C7;margin-bottom:12px}.identity strong{display:block;font-size:65px;line-height:1.2}.identity .role{font-size:34px;display:block;margin-top:12px}.chapter{top:230px;left:72px;max-width:850px;padding:18px 25px;background:#101C1A;color:#A6E5C7;font-size:36px;line-height:1.4;border-left:5px solid #A6E5C7}.caption{top:1410px;left:72px;width:876px;min-height:180px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:52px;line-height:1.4;letter-spacing:-.5px}.caption span{max-width:100%;padding:15px 24px;background:#101C1A;border-radius:12px;box-decoration-break:clone}.endmark{top:345px;left:72px;font-size:29px;letter-spacing:2px;color:#A6E5C7;padding:14px 20px;background:#101C1A}.endmark span{display:block;font-size:23px;color:#F7F8F2;letter-spacing:0;margin-top:7px}'''
script='''const tl=gsap.timeline({paused:true});window.__timelines=window.__timelines||{};'''
script+='tl.from("#brand",{opacity:0,y:-12,duration:.45,ease:"power2.out"},.15);'
script+='tl.from("#hook",{opacity:0,y:18,duration:.45,ease:"power3.out"},.25);'
script+='tl.from("#identity",{opacity:0,x:-18,duration:.4,ease:"sine.out"},5.7);'
for i,c in enumerate(chapters):script+=f'tl.from("#chapter-{i}",{{opacity:0,y:12,duration:.3,ease:"power2.out"}},{c["start"]});'
for i,c in enumerate(caps):script+=f'tl.from("#cap-{i}",{{opacity:0,duration:.08,ease:"none"}},{c["start"]});'
script+=f'tl.from("#endcard",{{opacity:0,y:8,duration:.4,ease:"sine.out"}},{dur-2});window.__timelines["neo-interview"]=tl;'
(p/'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><script src="assets/gsap.min.js"></script><style>{style}</style></head><body><div id="root" data-composition-id="neo-interview" data-width="1080" data-height="1920" data-start="0" data-duration="{dur}" data-fps="30"><video id="interview" class="clip" src="assets/picture.mp4" data-start="0" data-duration="{dur}" data-track-index="0" muted playsinline></video><audio id="dialogue" src="assets/dialogue.wav" data-start="0" data-duration="{dur}" data-track-index="1" data-volume="1"></audio><audio id="music" src="assets/music-final.wav" data-start="0" data-duration="{dur}" data-track-index="2" data-volume="0.36"></audio>{''.join(parts)}</div><script>{script}</script></body></html>''')
# Editable subtitle sidecar.
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(p/'captions.vi.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}' for i,c in enumerate(caps))+'\n')
