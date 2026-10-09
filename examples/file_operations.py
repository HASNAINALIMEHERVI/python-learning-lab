"""Read, copy, rename, compare and delete only temporary demo files."""
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

def main():
    with TemporaryDirectory(prefix="sunny-python-demo-") as folder:
        root = Path(folder)
        original = root / "sample.txt"
        original.write_text("Python practice\nSafe sample text\n", encoding="utf-8")
        print(original.read_text(encoding="utf-8"))
        copy = root / "copy.txt"
        shutil.copyfile(original, copy)
        print("Copies match:", original.read_bytes() == copy.read_bytes())
        renamed = copy.rename(root / "renamed.txt")
        print("Renamed:", renamed.name)
        renamed.unlink()
        print("Temporary copy deleted:", not renamed.exists())
    print("Demo folder removed; no existing user files were modified.")

if __name__ == "__main__":
    main()
