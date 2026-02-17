#!/usr/bin/env python3
"""
Generate a sample release notes output file from release-notes-spec.yaml.
Uses built-in sample content if no --content file is provided.
Output is written to the test directory by default.

Usage:
  python src/generate_release_notes_sample.py [--output path]
  python src/generate_release_notes_sample.py --content path/to/content.yaml --output path
"""

import argparse
from pathlib import Path
from typing import List, Optional

try:
    import yaml
except ImportError:
    yaml = None

# Sample content used when --content is not provided
SAMPLE_CONTENT = {
    "features": [
        {
            "title": "ASQL Search Variables",
            "body": "Queries can now use variables (e.g. $EARLIEST, $SENSOR_TYPE) so users can parameterize and reuse the same query with different bindings.",
        },
        {
            "title": "Homenet Report",
            "body": "A new homenet report uses variables to visualize internal-to-external traffic. Users can set internal CIDR lists and time range per sensor or region.",
        },
    ],
    "fixes": [
        {
            "title": "Variable binding validation",
            "body": "Fixed an issue where invalid timestamp bindings for $EARLIEST or $LATEST could produce unclear errors. Validation messages are now clearer.",
        },
    ],
    "docs": [
        {
            "title": "Search Variables (variables.md)",
            "body": "Documentation for ASQL search variables now includes variable syntax, binding rules, and NIDS field name reference. See variables.md in the output folder.",
        },
    ],
}


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, encoding="utf-8") as f:
        if yaml:
            return yaml.safe_load(f) or {}
        raise RuntimeError("PyYAML required. Install with: pip install pyyaml")


def generate_output(spec: dict, content: dict, output_path: Path, section_ids: Optional[List[str]] = None) -> None:
    lines = []
    sections = spec.get("sections", [])
    if section_ids is not None:
        section_ids_set = {s.strip().lower() for s in section_ids}
        sections = [s for s in sections if s.get("id", "").lower() in section_ids_set]
    for section in sections:
        section_id = section.get("id", "")
        title = section.get("title", section_id)
        items = content.get(section_id)
        if not items:
            continue
        lines.append(title)
        lines.append("")
        for item in items:
            if isinstance(item, dict):
                t = item.get("title", "")
                b = item.get("body", "")
                if t:
                    lines.append(f"{t}: {b}" if b else t)
            else:
                lines.append(str(item))
            lines.append("")
        lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(lines).strip()
    output_path.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")


def main():
    root = Path(__file__).resolve().parent.parent
    spec_path = root / "src" / "templates" / "release-notes-spec.yaml"
    default_out = root / "test" / "sample-release-notes.txt"

    parser = argparse.ArgumentParser(
        description="Generate a sample release notes output from release-notes-spec.yaml"
    )
    parser.add_argument(
        "--output", "-o", type=Path, default=default_out, help="Output file path"
    )
    parser.add_argument(
        "--spec", type=Path, default=spec_path, help="Path to release-notes-spec.yaml"
    )
    parser.add_argument(
        "--content", "-c", type=Path, default=None,
        help="YAML content file (features, fixes, docs). If omitted, built-in sample is used.",
    )
    parser.add_argument(
        "--sections", "-s", type=str, default=None,
        help="Comma-separated section ids to include (e.g. features,docs). If omitted, all sections with content are included.",
    )
    args = parser.parse_args()

    spec = load_yaml(args.spec)
    content = load_yaml(args.content) if args.content else SAMPLE_CONTENT
    section_ids = [s.strip() for s in args.sections.split(",")] if args.sections else None
    generate_output(spec, content, args.output, section_ids=section_ids)


if __name__ == "__main__":
    main()
