"""Read-only folder listing; accepts a path instead of a personal Windows path."""
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", default=".")
    args = parser.parse_args()
    folder = Path(args.folder).expanduser()
    if not folder.is_dir():
        parser.error("The selected path must be an existing directory.")
    try:
        for item in sorted(folder.iterdir(), key=lambda item: item.name.lower()):
            print(item.name)
    except OSError as exc:
        parser.error(f"Cannot read the directory: {exc.strerror}")

if __name__ == "__main__":
    main()
