# Blender 教程交付检查

Before rendering the full export:

- The source .blend is the user's latest relevant save; the new edit has a distinct name and output path unless replacement was requested.
- Every media path resolves. The changed strips have correct start/end frames and their animation fades reach zero at the intended boundaries.
- Compare a few frames before, during, and after each changed sequence. Inspect captions and PIP in the real timeline composite, not only in a standalone graphic.
- Listen to each narration edit, speed transition, BGM loop, whoosh/click, and beginning/end. Check that BGM remains at its intended native rate and below the voice.
- Watch the complete changed sections to catch motion errors a static frame cannot reveal. For large revisions, also watch the start, middle, and ending of the full output.

After rendering:

- Confirm nonzero output size, expected duration and dimensions, video stream, and audio stream.
- Spot-check the output file at the changed timestamps to verify the rendered result matches Blender previews.
- Deliver the .blend and video paths, note the source version used and any material limitation. Provide captions or other requested sidecars if applicable.

The bundled helpers report metadata and still frames. They cannot judge spoken meaning or whether a transition feels natural; those require watching/listening.
