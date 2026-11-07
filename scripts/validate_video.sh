#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  printf 'Usage: %s /absolute/export.mp4\n' "$0" >&2
  exit 2
fi

video_path=$1
if [ ! -f "$video_path" ] || [ ! -s "$video_path" ]; then
  printf 'Missing or empty video: %s\n' "$video_path" >&2
  exit 1
fi

if command -v ffprobe >/dev/null 2>&1; then
  dimensions=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$video_path")
  video_codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nw=1:nk=1 "$video_path")
  audio_codec=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nw=1:nk=1 "$video_path")
  duration=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$video_path")
  if [ -z "$dimensions" ] || [ -z "$video_codec" ] || [ -z "$audio_codec" ] || [ -z "$duration" ]; then
    printf 'Could not verify video, audio, dimensions, and duration.\n' >&2
    exit 1
  fi
  printf 'Video: %s | %s | audio %s | %ss\n' "$dimensions" "$video_codec" "$audio_codec" "$duration"
elif command -v mdls >/dev/null 2>&1; then
  width=$(mdls -raw -name kMDItemPixelWidth "$video_path")
  height=$(mdls -raw -name kMDItemPixelHeight "$video_path")
  duration=$(mdls -raw -name kMDItemDurationSeconds "$video_path")
  codecs=$(mdls -name kMDItemCodecs "$video_path")
  audio_rate=$(mdls -raw -name kMDItemAudioBitRate "$video_path")
  case "$width $height $duration $codecs $audio_rate" in
    *'(null)'*) printf 'Spotlight metadata incomplete; verify streams with a media probe.\n' >&2; exit 1 ;;
  esac
  if [ -z "$width" ] || [ -z "$height" ] || [ -z "$duration" ] || [ -z "$audio_rate" ]; then
    printf 'Metadata incomplete; verify streams with a media probe.\n' >&2
    exit 1
  fi
  printf 'Video: %sx%s | %ss | audio %s kbps | codecs: %s\n' "$width" "$height" "$duration" "$audio_rate" "$codecs"
else
  printf 'No ffprobe or mdls found; cannot verify video metadata.\n' >&2
  exit 2
fi
