"""Render requested timeline stills without saving the .blend.

Run: blender -b project.blend --python render_qc_frames.py -- --out /absolute/qa --frames 300,900
"""

import argparse
import bpy
import sys
from pathlib import Path


args = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
parser = argparse.ArgumentParser()
parser.add_argument("--out", required=True, type=Path)
parser.add_argument("--frames", required=True, help="Comma-separated timeline frame numbers")
options = parser.parse_args(args)

scene = bpy.context.scene
frames = [int(raw.strip()) for raw in options.frames.split(",") if raw.strip()]
if not frames:
    parser.error("--frames needs at least one frame")
if any(frame < scene.frame_start or frame > scene.frame_end for frame in frames):
    parser.error(f"frames must be within {scene.frame_start}..{scene.frame_end}")

options.out.mkdir(parents=True, exist_ok=True)
scene.render.image_settings.media_type = "IMAGE"
scene.render.image_settings.file_format = "PNG"
for frame in frames:
    output = options.out / f"frame-{frame:06d}.png"
    scene.frame_set(frame)
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)
    print(f"QC_FRAME={output}")
