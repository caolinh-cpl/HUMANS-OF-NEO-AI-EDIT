import json,subprocess
from pathlib import Path
p=Path(__file__).parent
e=json.loads((p/'edit.json').read_text());clips=e['clips'];inputs=[];fil=[];cumulative=0
if len(clips)<2:
 raise SystemExit('Add at least two verified source clips to your local edit.json before preparing media.')
for i,c in enumerate(clips):
 d=c['out']-c['in'];extra=.12 if i<len(clips)-1 else 0
 inputs+=['-ss',str(c['in']),'-t',str(d+extra),'-i',str(p/f'assets/source-{c["source"]}.mp4')]
 fil.append(f'[{i}:v]setpts=PTS-STARTPTS,format=yuv420p,settb=AVTB,fps=30[v{i}]')
 fil.append(f'[{i}:a]atrim=duration={d},asetpts=PTS-STARTPTS,aresample=48000[a{i}]')
 if i:
  before='v0' if i==1 else f'x{i-1}'
  fil.append(f'[{before}][v{i}]xfade=transition=fade:duration=0.12:offset={cumulative},fps=30[x{i}]')
 cumulative+=d
fil.append(''.join(f'[a{i}]' for i in range(len(clips)))+f'concat=n={len(clips)}:v=0:a=1,highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=11[aout]')
cmd=['ffmpeg','-v','warning','-y','-filter_complex_threads','2']+inputs+['-filter_complex',';'.join(fil),'-map',f'[x{len(clips)-1}]','-an','-c:v','libx264','-preset','fast','-crf','17','-g','30','-keyint_min','30','-pix_fmt','yuv420p','-t',str(e['duration']),'-movflags','+faststart',str(p/'assets/picture.mp4'),'-map','[aout]','-vn','-c:a','pcm_s16le','-ar','48000','-t',str(e['duration']),str(p/'assets/dialogue.wav')]
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(p/'assets/music-original.wav'),'-t',str(e['duration']),'-af',f'afade=t=out:st={e["duration"]-3}:d=3',str(p/'assets/music-final.wav')],check=True)
