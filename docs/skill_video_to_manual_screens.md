# Skill: Extract Manual Images From Screencast

## Purpose

Turn a screencast video into clean, cropped still images for documentation and user manuals.

## Default Output

- Use `PNG` for UI-heavy documentation with text, forms, tables, and menus.
- Use `JPEG` when file size matters more than maximum text sharpness.
- Extract one still image per shot or timecode.
- Prefer a representative moment inside the shot, not the very first frame.
- Define crop once on a reference image, then reuse it across the full batch if framing is stable.

## Required Inputs

- Source video path
- Timecodes or shot list
- Output format: `png` or `jpg`
- Output directories
- Crop rectangle in `width:height:x:y` format

## Tools

- `ffmpeg`
- shell / terminal
- optional: `GIMP` for crop selection

## Workflow

### 1. Verify FFmpeg

```bash
ffmpeg -version
```

If missing:

```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Create output folders

```bash
mkdir -p docs/screens_full
mkdir -p docs/screens_cropped
```

### 3. Extract still frames

Single PNG:

```bash
ffmpeg -y -ss 00:01:23 -i "docs/video.mp4" -frames:v 1 "docs/screens_full/shot_01.png"
```

Single JPEG:

```bash
ffmpeg -y -ss 00:01:23 -i "docs/video.mp4" -frames:v 1 -q:v 2 "docs/screens_full/shot_01.jpg"
```

Batch PNG:

```bash
while IFS=, read -r num ts; do
  ffmpeg -y -ss "$ts" -i "docs/video.mp4" -frames:v 1 "docs/screens_full/shot_${num}.png"
done <<'EOF'
01,00:00:01
02,00:00:06.5
03,00:00:17
EOF
```

Batch JPEG:

```bash
while IFS=, read -r num ts; do
  ffmpeg -y -ss "$ts" -i "docs/video.mp4" -frames:v 1 -q:v 2 "docs/screens_full/shot_${num}.jpg"
done <<'EOF'
01,00:00:01
02,00:00:06.5
03,00:00:17
EOF
```

### 4. Verify extraction count

```bash
ls docs/screens_full | wc -l
```

### 5. Determine crop rectangle

Use GIMP Crop tool on a representative frame.

Map GIMP fields to FFmpeg:

- `Position X` -> `x`
- `Position Y` -> `y`
- `Size X` -> `width`
- `Size Y` -> `height`

Convert to:

```text
crop=width:height:x:y
```

Example:

```text
Position X = 3
Position Y = 117
Size X = 1664
Size Y = 887
```

becomes:

```text
crop=1664:887:3:117
```

### 6. Test crop on one frame

PNG:

```bash
ffmpeg -y -i "docs/screens_full/shot_01.png" -vf "crop=1664:887:3:117" "docs/screens_cropped/test.png"
```

JPEG:

```bash
ffmpeg -y -i "docs/screens_full/shot_01.jpg" -vf "crop=1664:887:3:117" -q:v 2 "docs/screens_cropped/test.jpg"
```

### 7. Apply crop to all frames

PNG:

```bash
for f in docs/screens_full/*.png; do
  name=$(basename "$f")
  ffmpeg -y -i "$f" -vf "crop=1664:887:3:117" "docs/screens_cropped/$name"
done
```

JPEG:

```bash
for f in docs/screens_full/*.jpg; do
  name=$(basename "$f")
  ffmpeg -y -i "$f" -vf "crop=1664:887:3:117" -q:v 2 "docs/screens_cropped/$name"
done
```

### 8. Verify final output

```bash
ls docs/screens_cropped | wc -l
```

## Decision Rules

- If output contains lots of UI text, prefer `PNG`.
- If the image must stay small, use `JPEG`.
- If the first frame looks transitional or incomplete, move the timestamp deeper into the shot.
- If framing changes significantly during the video, do not reuse a single crop blindly; split the batch into groups.

## Best Practices

- Remove desktop wallpaper, OS bars, black borders, and unrelated side elements when possible.
- Keep final framing consistent across images from the same manual.
- Test on one file before running the full crop batch.
- Select only the most informative final images for the manual.

## Common Problems

### Batch stopped early

Re-run the missing commands or split the batch into smaller blocks.

### Heredoc block broke in terminal

Cancel with `Ctrl + C` and use shorter command groups.

### Crop looks wrong

Re-check the crop rectangle in GIMP and test again on one frame.

### Images look blurry

Switch from `JPEG` to `PNG`.
