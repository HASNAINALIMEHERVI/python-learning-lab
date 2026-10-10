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

The current curated set contains 33 examples. Syntax checks passed, and guessing-game boundaries, prime classification, recursion boundaries and all nine rock-paper-scissors outcomes were checked. Original personal text files and hardcoded Windows paths are excluded. The supplied files have now been triaged into useful project groups; see [the upload audit](UPLOAD-AUDIT.md) for scope, exclusions and pending work.

File mutation examples use `TemporaryDirectory`; demo data is automatically removed. The original uploaded file-deletion and rename scripts are not run against user folders.

## Additional audited exercises

Five further examples were repaired from the supplied learning files: bounded star patterns, a fictional grade classifier, structural pattern matching, inheritance with `super()`, and type hints with explicit empty-sequence handling. All prompts and documentation are in English; sample objects do not represent personal records.

```sh
python examples/patterns.py
python examples/grade_classifier.py
python examples/match_examples.py
python examples/inheritance_examples.py
python examples/type_hint_examples.py
```

Checks covered pattern sizes 1 and 3, grade cutoff boundaries, origin/axis classification, invalid days and numeric values, empty sequences, and inherited initialization. The grading thresholds are educational examples, not UET's official policy. Type annotations are not a substitute for runtime validation.

## Further reviewed work

Additional English examples cover validated collections, enumeration and `finally` cleanup. A repaired [Desktop Assistant Demo](projects/desktop-assistant/README.md) now includes a standard-library text interface, fixed browser destinations, optional local speech output and eight passing regression tests. Its audio hardware is unverified. It currently lives as a project directory here; a separate repository has not been created.
