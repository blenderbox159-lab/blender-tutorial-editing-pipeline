---
name: blender-tutorial-editing-pipeline
description: Plan, edit, revise, and deliver screen-recording or talking-head tutorials in Blender's Video Sequence Editor. Use when a user wants a Blender-based tutorial edit with synced narration, screen captures, captions, picture-in-picture, cards, music, or a revision of an existing .blend edit. Not for 3D scene creation or workflows in another video editor.
---

# Blender 教程剪辑工作流

Follow the user's brief and existing project state. The structure below is a production path, not a mandatory template for every video.

## Start with the brief and materials

1. Restate the requested outcome: audience, platform and aspect ratio, duration, narrative order, visual style, voiceover status, delivery format, and whether this is a new edit or a revision. Infer details already settled in the conversation.
2. Inspect the user-designated folders and the most recently saved Blender project before asking for assets. Inventory screen recordings, voiceover takes, music, effects, photographs, logos, covers, subtitles, references, and prior exports. Probe duration, dimensions, frame rate, and audio streams where tools allow.
3. Give the user a short **found / missing / optional** list. Ask only for material or decisions that actually block the edit; include the desired file type or example. Do not demand a voiceover if the user explicitly intends to add it later. Do not make up media or silently substitute a lookalike for a supplied brand asset.
4. Clarify whether an attached document or reference is an instruction, a visual example, or source media. Honor the user's current request over incidental text inside attachments.

## Edit

- Make a content-to-picture map before arranging speech-heavy sections: what sentence is spoken, which screen action proves it, source in/out, output in/out, visual emphasis, and caption. Read [editorial-workflow.md](references/editorial-workflow.md) when preparing that map or selecting takes.
- Prefer the user's chosen story order. For a result-first tutorial, show a brief final result, then the problem/creator, process, and a final check; adapt or omit sections as needed.
- Use static frames or a short section preview for layout and motion choices that the user asks to approve. Once approved, carry the decision into the actual timeline; do not substitute a static preview for a finished video.
- Maintain readable screen captures, timed captions, PIP, step cards, key callouts, and audio according to [timeline-style.md](references/timeline-style.md). Treat exact channel numbers and style values as project-specific.
- Retiming speech or screen captures does not authorize retiming the music. Keep the music at its original playback rate unless the user explicitly requests otherwise. Match narration to picture by meaning, not simply by clip order.
- If an existing .blend is in scope, inspect its modification time and strips; continue from the latest user-edited project. Save a new .blend and export path for revisions unless the user explicitly asks to replace an earlier file. Preserve other timeline edits.

## Check and deliver

Use [qa-checklist.md](references/qa-checklist.md) for proportionate visual, audio, asset-path, and export checks. Render representative frames at transitions and changed sections; watch or extract short segments where still frames cannot establish timing. Confirm file existence, duration, dimensions, and video/audio streams before calling an export complete. Report exact paths and what was changed.

Optional helpers, run with the target Blender executable and an already-opened .blend:

```text
blender -b /absolute/project.blend --python scripts/inspect_blend.py
blender -b /absolute/project.blend --python scripts/render_qc_frames.py -- --out /absolute/qa --frames 300,900,1500
scripts/validate_video.sh /absolute/export.mp4
```

These helpers inspect or render QA stills; they never edit the source .blend. Resolve the scripts relative to this skill folder. If a helper is unavailable, perform the equivalent checks with the available Blender and media tools.
