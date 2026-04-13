#!/usr/bin/env python3
"""Generate design configuration based on selected pattern.

Creates a design.yaml file with Tailwind CSS custom properties
for the selected design pattern.
"""

import argparse
import json
import os
import sys


PATTERNS = {
    "glassmorphic": {
        "background": "linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)",
        "colors": {
            "primary": "#6366f1",
            "secondary": "#8b5cf6",
            "accent": "#a78bfa",
            "background": "#0f172a",
            "surface": "rgba(30, 41, 59, 0.7)",
            "surface_hover": "rgba(51, 65, 85, 0.8)",
            "text": "#f8fafc",
            "text_muted": "#94a3b8",
            "border": "rgba(255, 255, 255, 0.1)",
        },
        "typography": {
            "heading": "Inter, system-ui, sans-serif",
            "body": "JetBrains Mono, Fira Code, monospace",
            "heading_weight": 600,
        },
        "effects": {
            "blur": "backdrop-blur-md",
            "border_radius": "0.75rem",
            "shadow": "0 25px 50px -12px rgba(99, 102, 241, 0.15)",
        },
    },
    "minimal": {
        "background": "#ffffff",
        "colors": {
            "primary": "#2563eb",
            "secondary": "#3b82f6",
            "accent": "#60a5fa",
            "background": "#ffffff",
            "surface": "#ffffff",
            "surface_hover": "#f8fafc",
            "text": "#0f172a",
            "text_muted": "#64748b",
            "border": "#e2e8f0",
        },
        "typography": {
            "heading": "Inter, system-ui, sans-serif",
            "body": "Inter, system-ui, sans-serif",
            "heading_weight": 500,
        },
        "effects": {
            "blur": "none",
            "border_radius": "0.5rem",
            "shadow": "0 1px 3px rgba(0, 0, 0, 0.05)",
        },
    },
    "bold": {
        "background": "linear-gradient(180deg, #000000 0%, #1a1a2e 100%)",
        "colors": {
            "primary": "#e94560",
            "secondary": "#0f3460",
            "accent": "#ff6b6b",
            "background": "#000000",
            "surface": "#16213e",
            "surface_hover": "#1a2744",
            "text": "#ffffff",
            "text_muted": "#a0aec0",
            "border": "#e94560",
        },
        "typography": {
            "heading": "Poppins, Montserrat, sans-serif",
            "body": "Inter, system-ui, sans-serif",
            "heading_weight": 700,
        },
        "effects": {
            "blur": "none",
            "border_radius": "1rem",
            "shadow": "0 8px 32px rgba(233, 69, 96, 0.2)",
        },
    },
    "playful": {
        "background": "linear-gradient(135deg, #fdf2f8 0%, #ede9fe 50%, #dbeafe 100%)",
        "colors": {
            "primary": "#a78bfa",
            "secondary": "#f472b6",
            "accent": "#34d399",
            "background": "#fdf2f8",
            "surface": "#ffffff",
            "surface_hover": "#faf5ff",
            "text": "#1e1b4b",
            "text_muted": "#6b7280",
            "border": "transparent",
        },
        "typography": {
            "heading": "Nunito, Quicksand, sans-serif",
            "body": "Inter, system-ui, sans-serif",
            "heading_weight": 600,
        },
        "effects": {
            "blur": "none",
            "border_radius": "1.25rem",
            "shadow": "0 4px 16px rgba(0, 0, 0, 0.06)",
        },
    },
}


def parse_args():
    parser = argparse.ArgumentParser(description="Generate design configuration")
    parser.add_argument(
        "--pattern",
        required=True,
        choices=list(PATTERNS.keys()) + ["custom"],
        help="Design pattern to use",
    )
    parser.add_argument("--output", required=True, help="Output design.yaml path")
    parser.add_argument("--primary", help="Custom primary color (for custom pattern)")
    parser.add_argument("--background", help="Custom background color (for custom pattern)")
    return parser.parse_args()


def dict_to_yaml(data: dict, indent: int = 0) -> str:
    """Simple dict to YAML string conversion without external dependency."""
    lines = []
    prefix = "  " * indent
    for key, value in data.items():
        if isinstance(value, dict):
            lines.append(f"{prefix}{key}:")
            lines.append(dict_to_yaml(value, indent + 1))
        elif isinstance(value, str):
            # Quote strings that contain special characters
            if any(c in value for c in [":", "#", "&", "*", "?", "|", "-", "<", ">", "=", "!", "%", "@", "`", ",", "[", "]", "{", "}"]):
                lines.append(f'{prefix}{key}: "{value}"')
            else:
                lines.append(f"{prefix}{key}: {value}")
        else:
            lines.append(f"{prefix}{key}: {value}")
    return "\n".join(lines)


def generate_design(pattern: str, output: str, custom_primary: str = None, custom_bg: str = None):
    """Generate design.yaml configuration."""
    if pattern == "custom":
        config = {
            "pattern": "custom",
            "colors": {
                "primary": custom_primary or "#6366f1",
                "background": custom_bg or "#0f172a",
            },
            "note": "Custom pattern — edit this file to fine-tune tokens",
        }
    else:
        config = {"pattern": pattern, **PATTERNS[pattern]}

    output_dir = os.path.dirname(output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        f.write(dict_to_yaml(config))

    print(f"Design config generated: {output}")
    print(f"  Pattern: {pattern}")


def main():
    args = parse_args()
    generate_design(args.pattern, args.output, args.primary, args.background)


if __name__ == "__main__":
    main()