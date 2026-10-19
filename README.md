# Humans of NEO — HyperFrames interview project

Source code for a vertical interview composition built with HyperFrames. This is a video production project, not a separate web application. Python generates the composition HTML and Vietnamese subtitle sidecar; HyperFrames previews, validates, and renders it.

The public repository intentionally excludes interview footage, audio, transcript text, real edit decisions, subtitles, generated HTML, screenshots, and rendered videos. A fresh clone cannot reconstruct the finished interview without the privately retained project data and media.

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

The finished MP4 and subtitle sidecar are delivered separately through workspace download links. A successful Git push is not proof that either output is downloadable.
