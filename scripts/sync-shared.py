"""Check or refresh packaged copies of shared skill references (Python 3.10+)."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONSUMERS = {
    "evidence.md": ("triage-bug", "triage-cve", "review-pr", "fix-issue"),
    "security-handling.md": ("triage-bug", "triage-cve", "review-pr", "fix-issue"),
    "duplicate-search.md": ("triage-bug", "triage-cve"),
}


def sync(root: Path, write: bool = False) -> list[str]:
    root = root.resolve()
    errors = []
    for name, consumers in CONSUMERS.items():
        source = root / "shared" / name
        try:
            if not source.resolve().is_relative_to(root):
                raise ValueError("shared source resolves outside the repository")
            content = source.read_bytes()
        except (OSError, ValueError, RuntimeError) as exc:
            errors.append(f"{source.relative_to(root)}: {exc}")
            continue
        expected = (f"<!-- Generated from shared/{name}; edit the source and run "
                    "python scripts/sync-shared.py --write. -->\n\n").encode() + content
        for skill in consumers:
            target = root / "skills" / skill / "references" / name
            try:
                if not target.resolve().is_relative_to(root):
                    raise ValueError("packaged reference resolves outside the repository")
                # Refuse symlinks: every skill must carry its own portable copy.
                if target.is_symlink() or target.parent.is_symlink():
                    raise ValueError("packaged reference must not be a symlink")
                if write:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(expected)
                elif not target.is_file() or target.read_bytes() != expected:
                    errors.append(f"{target.relative_to(root)}: missing or stale; "
                                  "run python scripts/sync-shared.py --write")
            except (OSError, ValueError, RuntimeError) as exc:
                errors.append(f"{target.relative_to(root)}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="refresh checked-in copies")
    args = parser.parse_args()
    errors = sync(ROOT, write=args.write)
    for error in errors:
        print(f"FAIL: {error}")
    if not errors:
        print("PASS: shared references " + ("synchronized" if args.write else "match packaged copies"))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
