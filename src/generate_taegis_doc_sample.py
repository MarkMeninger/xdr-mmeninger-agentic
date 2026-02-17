#!/usr/bin/env python3
"""
Generate a sample .md file that follows the structure defined in
src/templates/taegis-doc-structure.yaml. Output is written to the test directory
by default.

Usage:
  python src/generate_taegis_doc_sample.py [--output path]
  python src/generate_taegis_doc_sample.py --structure path/to/taegis-doc-structure.yaml
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


def build_sample_md(structure_spec: dict) -> str:
    """Build sample Markdown content that conforms to the taegis-doc-structure spec."""
    lines = []

    # Required: ### title at start
    lines.append("### Search Variables (Sample)")
    lines.append("")
    # Intro paragraph(s)
    lines.append(
        "CQL search variables allow users to parameterize queries with placeholders such as "
        "`$EARLIEST`, `$SENSOR_TYPE`, and `$FILTER_FIELD`. Variables are substituted with bound "
        "values before execution."
    )
    lines.append("")
    # Optional syntax summary (inline code)
    lines.append("General form: `search_query_with_$VARIABLE_NAMES`")
    lines.append("")
    # Subsection 1
    lines.append("#### Variable syntax")
    lines.append("")
    lines.append(
        "Use `$VAR_NAME` in the query where a literal or list would appear. "
        "Field name variables (e.g. for sort or filter) can be set to valid NIDS field names "
        "from the schema."
    )
    lines.append("")
    lines.append("**Example:** NIDS query with sensor and time variables:")
    lines.append("")
    lines.append("    from nids where sensor_type = $SENSOR_TYPE earliest = $EARLIEST")
    lines.append("")
    # Subsection 2
    lines.append("#### Binding variables")
    lines.append("")
    lines.append(
        "Before execution, each variable is bound to a value: a string literal, a number, "
        "a timestamp (ISO8601), or a parenthesized list for `IN` / `!IN` clauses."
    )
    lines.append("")
    lines.append("**Example:** NIDS filter by field name variable:")
    lines.append("")
    lines.append("    from nids where $FILTER_FIELD = $FILTER_VALUE earliest = $EARLIEST")
    lines.append("")
    # Optional !!! Note
    lines.append("!!! Note")
    lines.append("")
    lines.append("    This sample document was generated from taegis-doc-structure.yaml.")
    lines.append("    It illustrates the expected structure for files in data/taegis-docs.")
    lines.append("")
    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parent.parent
    structure_path = root / "src" / "templates" / "taegis-doc-structure.yaml"
    default_out = root / "test" / "sample-taegis-doc.md"

    parser = argparse.ArgumentParser(
        description="Generate a sample .md file from taegis-doc-structure.yaml"
    )
    parser.add_argument(
        "--output", "-o", type=Path, default=default_out, help="Output .md file path"
    )
    parser.add_argument(
        "--structure",
        type=Path,
        default=structure_path,
        help="Path to taegis-doc-structure.yaml",
    )
    args = parser.parse_args()

    spec = load_yaml(args.structure)
    content = build_sample_md(spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(content, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
