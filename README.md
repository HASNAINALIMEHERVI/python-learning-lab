# Python Learning Lab

Personal Python practice by Hasnain Ali Mehervi (Sunny). These are educational exercises, not client projects or a production software library.

## Run

Python 3.10+; no external packages are needed for the currently curated examples.

```sh
python examples/number_guessing.py
python examples/list_directory.py .
python examples/loops.py
```

Examples cover loops, map/filter/reduce, dictionary merging, class and instance attributes, the main guard, directory listing and a terminal guessing game. Imports do not run interactive prompts. Directory listing is read-only and accepts a chosen path.

## Audit status

The current curated set contains 25 examples. Syntax checks passed, and guessing-game boundaries, prime classification, recursion boundaries and all nine rock-paper-scissors outcomes were checked. Original personal text files and hardcoded Windows paths are excluded. Additional supplied exercises are still under review; this repository does not claim to include them all.

File mutation examples use `TemporaryDirectory`; demo data is automatically removed. The original uploaded file-deletion and rename scripts are not run against user folders.
