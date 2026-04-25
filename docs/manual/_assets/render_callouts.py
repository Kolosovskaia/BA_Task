#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from PIL import Image, ImageColor, ImageDraw, ImageFont


SCRIPT_DIR = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render review callout samples for manual screenshots.")
    parser.add_argument(
        "--config",
        type=Path,
        default=SCRIPT_DIR / "callouts.yaml",
        help="Path to YAML config.",
    )
    parser.add_argument(
        "--shots",
        nargs="*",
        help="Optional subset of shot ids to render.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = ["DejaVuSans-Bold.ttf", "Arial Bold.ttf"] if bold else ["DejaVuSans.ttf", "Arial.ttf"]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def clamp_badge(pos: tuple[int, int], radius: int, width: int, height: int) -> tuple[int, int]:
    x, y = pos
    x = max(radius + 6, min(x, width - radius - 6))
    y = max(radius + 6, min(y, height - radius - 6))
    return x, y


def nearest_point(cx: int, cy: int, box: tuple[int, int, int, int]) -> tuple[int, int]:
    x, y, w, h = box
    nx = max(x, min(cx, x + w))
    ny = max(y, min(cy, y + h))
    return nx, ny


def draw_badge(draw: ImageDraw.ImageDraw, center: tuple[int, int], radius: int, value: int, accent: tuple[int, int, int], font: ImageFont.ImageFont) -> None:
    cx, cy = center
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=accent, outline=(255, 255, 255), width=2)
    text = str(value)
    bbox = draw.textbbox((0, 0), text, font=font)
    tx = cx - (bbox[2] - bbox[0]) / 2
    ty = cy - (bbox[3] - bbox[1]) / 2 - 1
    draw.text((tx, ty), text, fill=(255, 255, 255), font=font)


def render_shot(shot_id: str, shot: dict, config: dict, config_dir: Path) -> Path:
    style = config["style"]
    accent = ImageColor.getrgb(style["accent"])
    outline_width = int(style.get("outline_width", 4))
    badge_radius = int(style.get("badge_radius", 18))
    base_legend_height = int(style.get("legend_height", 132))
    legend_padding_x = int(style.get("legend_padding_x", 36))
    legend_padding_y = int(style.get("legend_padding_y", 22))
    legend_line_gap = int(style.get("legend_line_gap", 34))
    title_block_height = 38
    annotations = shot["annotations"]
    dynamic_legend_height = legend_padding_y * 2 + title_block_height + len(annotations) * legend_line_gap + 12
    legend_height = max(base_legend_height, dynamic_legend_height)

    source_dir = (config_dir / config["source_dir"]).resolve()
    output_dir = (config_dir / config["output_dir"]).resolve()
    source_path = source_dir / shot["source"]
    output_path = output_dir / shot["output"]

    image = Image.open(source_path).convert("RGB")
    canvas = Image.new("RGB", (image.width, image.height + legend_height), (255, 255, 255))
    canvas.paste(image, (0, 0))
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(20, bold=True)
    legend_font = load_font(18)
    badge_font = load_font(19, bold=True)

    for annotation in annotations:
        x, y, w, h = annotation["box"]
        draw.rounded_rectangle((x, y, x + w, y + h), radius=12, outline=accent, width=outline_width)
        center = clamp_badge(tuple(annotation["badge_pos"]), badge_radius, image.width, image.height)
        px, py = nearest_point(center[0], center[1], (x, y, w, h))
        draw.line((center[0], center[1], px, py), fill=accent, width=3)
        draw_badge(draw, center, badge_radius, int(annotation["id"]), accent, badge_font)

    separator_y = image.height
    draw.line((0, separator_y, canvas.width, separator_y), fill=(224, 224, 224), width=2)
    title_y = separator_y + legend_padding_y
    draw.text((legend_padding_x, title_y), shot["title"], fill=(35, 35, 35), font=title_font)

    for idx, annotation in enumerate(annotations):
        row_y = title_y + 38 + idx * legend_line_gap
        badge_center = (legend_padding_x + badge_radius, row_y + badge_radius - 2)
        draw_badge(draw, badge_center, badge_radius, int(annotation["id"]), accent, badge_font)
        draw.text((legend_padding_x + badge_radius * 2 + 14, row_y), annotation["legend"], fill=(55, 55, 55), font=legend_font)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path)
    return output_path


def main() -> int:
    args = parse_args()
    config_path = args.config.resolve()
    config = load_yaml(config_path)
    selected = set(args.shots or config["shots"].keys())
    rendered = []
    for shot_id, shot in config["shots"].items():
        if shot_id not in selected:
            continue
        rendered.append(render_shot(shot_id, shot, config, config_path.parent))
    for path in rendered:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
