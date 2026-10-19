import numpy as np,wave
from pathlib import Path
sr=44100;dur=90;mix=np.zeros((sr*dur,2),dtype=np.float64)
# Original restrained instrumental bed: warm pads and sparse bell-like notes.
chords=[[146.832,220,293.665,349.228],[130.813,195.998,261.626,329.628],[174.614,220,261.626,349.228],[130.813,195.998,293.665,391.995]]
for k,start in enumerate(np.arange(0,dur,5)):
 n=min(int(7*sr),len(mix)-int(start*sr));t=np.arange(n)/sr
 env=np.minimum(t/1.5,1)*np.clip((7-t)/2.5,0,1)
 for j,f in enumerate(chords[k%4]):
  tone=(np.sin(2*np.pi*f*t)+.16*np.sin(2*np.pi*f*2*t))*.013*env
  mix[int(start*sr):int(start*sr)+n,0]+=tone*(.8+j*.05)
  mix[int(start*sr):int(start*sr)+n,1]+=tone*(1-j*.05)
 for j in [0,2]:
  st=int((start+1+j*.8)*sr);n=min(sr*3,len(mix)-st)
  if n<=0:continue
  t=np.arange(n)/sr;f=chords[k%4][j]*2
  note=np.sin(2*np.pi*f*t)*np.exp(-t*2)*np.minimum(t/.025,1)*.018
  mix[st:st+n,:]+=note[:,None]
fade=np.minimum(np.arange(len(mix))/sr/2,1)*np.minimum((len(mix)-np.arange(len(mix)))/sr/3,1)
mix*=fade[:,None]
with wave.open(str(Path(__file__).parent/'assets/music-original.wav'),'w') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(mix,-1,1)*32767).astype('<i2').tobytes())
