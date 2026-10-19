"""Inspect and fully decode an existing rendered MP4 without modifying it."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('file', type=Path)
args = parser.parse_args()
p = args.file.resolve(strict=True)
data = json.loads(subprocess.check_output([
    'ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(p)
]))
video = next(s for s in data['streams'] if s['codec_type'] == 'video')
audio = next(s for s in data['streams'] if s['codec_type'] == 'audio')
duration = float(data['format']['duration'])
if not (video['codec_name'] == 'h264' and video['pix_fmt'] == 'yuv420p'
        and video['width'] == 1080 and video['height'] == 1920
        and audio['codec_name'] == 'aac' and 0 < duration < 90):
    raise SystemExit('The file does not meet the expected delivery format.')
subprocess.run([
    'ffmpeg', '-v', 'error', '-xerror', '-i', str(p),
    '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'
], check=True)
checksum = hashlib.sha256()
with p.open('rb') as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b''):
        checksum.update(chunk)
print(json.dumps({
    'file': p.name, 'bytes': p.stat().st_size,
    'duration_seconds': duration, 'width': video['width'], 'height': video['height'],
    'video_codec': video['codec_name'], 'audio_codec': audio['codec_name'],
    'sha256': checksum.hexdigest(), 'full_decode': 'passed'
}, indent=2))
