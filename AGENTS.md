# Project instructions

This is a HyperFrames video project. Use the existing checkout; cloud tasks are already isolated. Do not create a Git worktree unless the user requests it.

Keep interview media, audio, transcript text, real edit.json, generated index.html, captions, rendered videos, credentials, and environment files out of public commits. Do not force-add ignored files or publish private assets through Git LFS or releases. Stage public source files explicitly and inspect the staged diff before committing.

Use the HyperFrames skills when modifying compositions. Preserve the original speaker's dialogue, context, and tone. Never invent quotes or supporting footage.

Run npm ci and npm run setup to prepare dependencies. npm run build reads ignored local edit.json. npm run check validates the generated composition with its private local media. Do not claim a fresh public clone can render the interview without those privately supplied inputs.

Verify finished media with python3 verify_render.py <file>. Keep downloadable MP4 and subtitle outputs separate from the repository. A successful push does not verify a download link.
