"""Read-only VSE inventory. Run: blender -b project.blend --python inspect_blend.py"""

import bpy
import json
from pathlib import Path


scene = bpy.context.scene
editor = scene.sequence_editor
strips = [] if editor is None else list(editor.strips)


def media_path(strip):
    if strip.type == "MOVIE":
        return bpy.path.abspath(strip.filepath)
    if strip.type == "SOUND":
        return bpy.path.abspath(strip.sound.filepath) if strip.sound else None
    if strip.type == "IMAGE" and strip.elements:
        return bpy.path.abspath(str(Path(strip.directory) / strip.elements[0].filename))
    return None


items = []
for strip in sorted(strips, key=lambda s: (s.frame_final_start, s.channel)):
    path = media_path(strip)
    items.append(
        {
            "name": strip.name,
            "type": strip.type,
            "channel": strip.channel,
            "start": strip.frame_final_start,
            "end_exclusive": strip.frame_final_end,
            "source": path,
            "source_exists": Path(path).is_file() if path else None,
        }
    )

report = {
    "blend": bpy.data.filepath,
    "fps": scene.render.fps / scene.render.fps_base,
    "resolution": [scene.render.resolution_x, scene.render.resolution_y],
    "frame_range": [scene.frame_start, scene.frame_end],
    "markers": [{"frame": m.frame, "name": m.name} for m in scene.timeline_markers],
    "missing_sources": [x["source"] for x in items if x["source_exists"] is False],
    "strips": items,
}
print("VSE_INSPECT_JSON=" + json.dumps(report, ensure_ascii=False))
