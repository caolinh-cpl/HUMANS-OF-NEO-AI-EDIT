---
name: humans-of-neo-edit
description: Continue or revise Humans of NEO interview videos from uploaded footage, an existing MP4, or a private HyperFrames project archive. Preserve authentic dialogue, apply the saved NEO identity, render with HyperFrames, and verify the actual delivery route.
---

# Humans of NEO editing workflow

## Start from the existing project

Read the repository's AGENTS.md, README.md, DESIGN.md, and package.json. Use the existing checkout; cloud tasks are already isolated and do not need another Git worktree. Apply the available HyperFrames authoring and CLI skills before modifying compositions.

Inspect the user's new message and uploaded assets before choosing an operation. A new upload is source material, not permission to publish it. Follow the user's requested changes, preserving other editorial choices where possible. Communicate in Vietnamese when the user does; use plain language and avoid developer-only setup instructions unless necessary. When the user requests step-by-step guidance, wait after each step.

## Series defaults

- Humans of NEO: modern, youthful, authentic interviews with a restrained technology/community identity.
- Default delivery: portrait 9:16, under 90 seconds, suitable for Reels, TikTok, and Shorts.
- Existing episode: Đào Tiến Dũng — Head of Tech. The brief concerns his journey through Marcom, HR, and Tech and his return to lead Tech. Verify claims against the actual source; the brief is not a source of invented dialogue.
- Use the supplied footage and original spoken audio. Remove unnecessary pauses, filler, repetition, and dead space while preserving context, personality, and meaning.
- Choose a strong opening and a coherent personal journey with a meaningful ending. Adapt to the strongest interview content rather than forcing a script.
- Vietnamese subtitles must follow reliable source transcription. Normalize spelling and confirmed names; never invent or silently guess uncertain quotes. Use multilingual models, not English-only models, for Vietnamese.
- Follow DESIGN.md: Be Vietnam Pro; ink #101C1A, warm white #F7F8F2, mint #A6E5C7. Readable mobile typography, modest motion, subtle transitions, quiet instrumental music. Keep the face clear and avoid aggressive crops of low-resolution footage.
- No invented footage, unsupported facts, synthetic replacement dialogue, or distracting effects.

## Identify what can actually be edited

Inspect current files, Git state, media streams, duration, dimensions, and source quality. Do not assume GitHub contains the uploaded workspace media or complete private edit.

- Private HyperFrames archive: inspect and restore index.html, edit.json, prepared picture, dialogue, and music without overwriting newer work. Inspect archive paths and sizes before extraction. Real media, transcripts, and caption data must stay ignored and local.
- New raw footage: obtain a reliable transcript and timing before selecting excerpts. Check installed tools and authorized model sources first. Never disable TLS or artifact integrity checks.
- Finished MP4 only: existing subtitles and graphics are burned in. Simple trims and a delivery transcode can use that file; clean changes to its existing captions/graphics require the original editable project or source footage. Explain that specific limitation without claiming the edit is impossible.
- Source-only GitHub checkout: edit.example.json is a schema example, not the real edit. Do not substitute placeholder captions and claim it reproduces the interview.

Ask only for missing assets that prevent the requested change. Complete useful independent work first. Do not ask the user to repeat the whole series brief.

## Implement and validate

Keep a recoverable original and use versioned outputs for revisions. Do not rebuild the entire edit for a download/transcode problem.

With private inputs restored, use the README commands: npm ci, npm run setup, npm run build, npm run check, npm run render. Chrome may need HYPERFRAMES_BROWSER_PATH set to the verified installed browser. Use the pinned HyperFrames CLI. Start from the repository's existing generators rather than creating a second unrelated application.

For composition changes, run HyperFrames validation and inspect representative opening, name card, caption, transition, and ending frames. Check the final runtime is below 90 seconds. Do not claim playback just because a file or process exists.

For the original 1080p delivery, verify the existing file with verify_render.py. This script expects 1080x1920; do not report its expected resolution mismatch as corruption of a valid 720p copy.

When a smaller delivery is needed, transcode the existing finished render with FFmpeg: 720x1280, 30 fps, H.264/yuv420p, approximately 2400 kbps video with constrained maximum bitrate, AAC 128 kbps, and faststart. Preserve the complete rendered picture, burned-in subtitles, and existing audio. Verify actual size below 30,000,000 bytes, inspect streams with ffprobe, and run a full FFmpeg decode with -xerror. Never assume a requested bitrate guarantees the size limit.

## Privacy and public GitHub delivery

The repository is public: caolinh-cpl/HUMANS-OF-NEO-AI-EDIT. Keep raw footage, separate interview audio, transcripts, private edit.json, generated interview HTML, private archives, credentials, and environment secrets out of commits.

The user explicitly approved publishing the finished episode's 720p MP4 at outputs/Humans-of-NEO-Dao-Tien-Dung-720p.mp4. That narrow exception is recorded in .gitignore. It does not authorize publishing every future upload, private archive, subtitle sidecar, or unrelated video. When the user explicitly requests publishing a new finished version, make its public visibility clear, stage only the authorized files, and proceed within that instruction.

Inspect the staged paths and diff before committing. Preserve existing changes, avoid force pushes, and verify the remote commit after a push.

## Delivery is a separate acceptance check

In this conversation, workspace preview and downloads returned "Unable to load file" and "Could not download artifact", including for ZIP files. Changing permissions and copying files did not establish a working handoff. Local paths and sandbox links are not proof that the user can download a file. The UI Outputs menu did not offer a video attachment registration action. Do not invent one.

Google Drive appeared connected in the user's settings, but no callable Drive upload tool was exposed in this agent session. Check current tool availability instead of assuming the connection is usable or repeatedly asking the user to reconnect. Do not request OAuth tokens, passwords, or private keys in chat.

The verified delivery route for the approved episode was a normal GitHub file download:
https://github.com/caolinh-cpl/HUMANS-OF-NEO-AI-EDIT/raw/refs/heads/main/outputs/Humans-of-NEO-Dao-Tien-Dung-720p.mp4

After an authorized publication, fetch the actual HTTPS download URL into a temporary file. Require HTTP 200, matching byte count, and matching SHA-256 against the intended output. Only then report that this download route was verified. A successful Git push alone is insufficient. Do not upload private media to a public host or create a public tunnel as a workaround.

If no authorized delivery route exists, explain the exact missing capability once and offer a concrete available alternative. Do not repeatedly rerender, change codecs, install tools, or shift the user through unsupported UI steps.

## Finish

Report the requested changes, actual duration/resolution/file size, verification results, and a verified delivery link when available. Explain any remaining limitation precisely. Keep instructions brief and usable for a nontechnical user.
