#!/usr/bin/env python3
"""
Generate a requirements output file from requirements-spec.yaml (in src/templates/).
Optionally pass section content via a YAML content file.

Usage:
  python generate_requirements_output.py [--output path]
  python generate_requirements_output.py --content sample-content.yaml [--output path]

Default output: output/test-requirements.txt

Content file keys must match section ids in the spec (e.g. description, acceptance_criteria).
See test/sample-requirements-content.yaml for format.
"""

import argparse
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, encoding="utf-8") as f:
        if yaml:
            return yaml.safe_load(f) or {}
        raise RuntimeError("PyYAML required. Install with: pip install pyyaml")


def generate_output(spec: dict, content: dict, output_path: Path) -> None:
    lines = [
        "# Requirements Output",
        "# Generated from requirements-spec.yaml",
        "",
    ]
    for section in spec.get("sections", []):
        section_id = section.get("id", "")
        title = section.get("title", section_id)
        lines.append("-" * 76)
        lines.append(title)
        lines.append("-" * 76)
        lines.append("")
        # Use content file if provided for this section
        section_content = content.get(section_id) if content else None
        if "items" in section:
            if isinstance(section_content, list):
                for entry in section_content:
                    if isinstance(entry, dict):
                        sid = entry.get("id", "")
                        stmt = entry.get("statement", "")
                        lines.append(f"{sid}: {stmt}")
                    else:
                        lines.append(str(entry))
                    lines.append("")
            else:
                for item in section["items"]:
                    sid = item.get("id", "")
                    stmt = item.get("statement", "")
                    lines.append(f"{sid}: {stmt}")
                    lines.append("")
        else:
            if section_content is not None and section_content != "":
                if isinstance(section_content, dict):
                    body = section_content.get("body")
                    if body is not None and str(body).strip():
                        lines.append(str(body).strip())
                        lines.append("")
                    examples = section_content.get("examples")
                    if examples:
                        lines.append("Examples:")
                        lines.append("")
                        for ex in examples:
                            if isinstance(ex, dict):
                                label = ex.get("label", "")
                                text = ex.get("text", "")
                                if label:
                                    lines.append(f"  {label}:")
                                if text:
                                    for line in str(text).strip().splitlines():
                                        lines.append(f"    {line}" if line else "    ")
                            else:
                                lines.append(f"  - {ex}")
                            lines.append("")
                else:
                    lines.append(section_content.strip() if isinstance(section_content, str) else str(section_content))
                    lines.append("")
            else:
                lines.append("[Content for this section.]")
                lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")


def main():
    root = Path(__file__).resolve().parent.parent
    spec_path = root / "src" / "templates" / "requirements-spec.yaml"
    default_out = root / "output" / "test-requirements.txt"

    parser = argparse.ArgumentParser(description="Generate requirements output from YAML spec")
    parser.add_argument("--output", "-o", type=Path, default=default_out, help="Output file path")
    parser.add_argument("--spec", type=Path, default=spec_path, help="Path to requirements-spec.yaml (default: src/templates/requirements-spec.yaml)")
    parser.add_argument("--content", "-c", type=Path, default=None, help="YAML file with section content (keys = section ids)")
    args = parser.parse_args()

    spec = load_yaml(args.spec)
    content = load_yaml(args.content) if args.content else {}
    generate_output(spec, content, args.output)


if __name__ == "__main__":
    main()
