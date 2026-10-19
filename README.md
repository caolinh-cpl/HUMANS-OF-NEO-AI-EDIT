# Humans of NEO — HyperFrames interview project

Source code for a vertical interview composition built with HyperFrames. This is a video production project, not a separate web application. Python generates the composition HTML and Vietnamese subtitle sidecar; HyperFrames previews, validates, and renders it.

The public repository excludes raw interview footage, separate audio, transcript text, real edit decisions, subtitle sidecars, generated HTML, and screenshots. The user-approved finished 720p MP4 is included under `outputs/` for download. A fresh clone cannot reconstruct the finished interview without the privately retained project data and media.

## Requirements

- Node.js 22 or newer and npm
- Python 3.12 or newer
- FFmpeg and ffprobe on PATH
- Chrome or Chromium for HyperFrames
- NumPy only when regenerating the optional original music bed

## Install

```bash
npm ci
npm run setup
```

The CLI is pinned to HyperFrames 0.8.174; GSAP is pinned in the lockfile. `setup` copies GSAP into an ignored local asset file. The bundled Be Vietnam Pro font is licensed under the included SIL Open Font License.

## Restore the private edit locally

Use the existing checkout; cloud tasks are already isolated and do not require a Git worktree.

1. Copy `edit.example.json` to ignored `edit.json`.
2. Fill in `speaker`, `role`, the verified caption cues, chapter cues, and source cut decisions locally. Do not commit those private values.
3. Restore these private prepared assets into `assets/`:
   - `picture.mp4`: pre-edited, silent interview picture
   - `dialogue.wav`: original interview dialogue aligned with that picture
   - `music-final.wav`: aligned background music
4. Set `duration` to the prepared media duration, strictly below 90 seconds.

```bash
npm run build
npm run check
npm run dev
npm run render
```

`build` writes ignored `index.html` and `captions.vi.srt`. `render` writes an ignored MP4 under `renders/`. If Chrome discovery needs help, set `HYPERFRAMES_BROWSER_PATH` to the installed Chrome/Chromium executable before rendering.

### Data format

`captions` and `chapters` contain objects with `start`, `end` (seconds on the edited timeline), and `text`. Caption text must come from verified source speech. The example intentionally contains no dialogue.

`clips` contains objects with `source` (numeric source identifier), `in`, and `out` (source seconds). Those decisions are needed only to regenerate prepared media. For that workflow, privately restore `assets/source-<source>.mp4`, install the music dependency in a virtual environment, and run:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python music.py
python3 prepare_edit.py
npm run build
```

`prepare_edit.py` expects at least two excerpts, adds short picture dissolves, preserves the original dialogue, and normalizes its level. All selected cuts must preserve the speaker's context and meaning.

## Verify a rendered file

```bash
python3 verify_render.py renders/humans-of-neo.mp4
```

This inspects the container and streams and decodes the entire file. It checks portrait H.264 video, AAC audio, and a runtime below 90 seconds. Verification does not establish whether a browser download link works.

## File map

- `build_composition.py`: HTML, graphics, animation, and subtitle generator
- `prepare_edit.py`: picture assembly and original dialogue preparation
- `music.py`: optional original instrumental music generator
- `verify_render.py`: media integrity verification
- `edit.example.json`: public data schema example without interview content
- `DESIGN.md`: visual identity and editorial rules
- `hyperframes.json`, `meta.json`, `package.json`, `package-lock.json`: project configuration
- `setup.mjs`: local GSAP asset setup
- `assets/`: redistributable font and its license

## Privacy and delivery

Stage files explicitly. Never force-add ignored files or publish private media/transcripts through releases, Git LFS, or repository history. Environment files, keys, dependency caches, render artifacts, and interview data are ignored.

The user has approved publishing the finished 720p MP4 in this public repository. Only that exact MP4 is exempted from the media ignore rules. The subtitle sidecar and original 1080p render remain outside Git.

## Download the finished video

[Download Humans of NEO — 720p MP4](https://github.com/caolinh-cpl/HUMANS-OF-NEO-AI-EDIT/raw/refs/heads/main/outputs/Humans-of-NEO-Dao-Tien-Dung-720p.mp4)

76 seconds; 720 × 1280; 30 fps; H.264 video; AAC audio; burned-in Vietnamese subtitles. File size: 24,208,093 bytes.

SHA-256: `36c90bf76ebab2d530a73da75766beebec3525971fd3881111c8e2c67ce5a548`.
