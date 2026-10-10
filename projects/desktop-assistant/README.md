# Desktop Assistant Demo

Personal project by Hasnain Ali Mehervi (Sunny), reworked from the uploaded `main(1).py` Jarvis prototype. This is a Python desktop/terminal companion, separate from the browser assistant project.

## Run

Python 3.10 or newer; the default text mode uses only the standard library:

```sh
python assistant.py
```

Commands: `open youtube`, `open google`, `play music`, `news`, `time`, `help`, `exit`. Browser commands open fixed, allowlisted public pages. Spotify opens its website; the assistant does not control playback or pick a track.

Optional local text-to-speech:

```sh
python -m pip install -r requirements-speech.txt
python assistant.py --speech
```

Speech initialization is lazy and failures fall back to text. Audio output requires a supported local speech engine/driver. No microphone listening, online speech recognition, arbitrary shell execution, arbitrary URL navigation or AI API calls are included. The original missing `music_library` and unrelated dependencies were removed. Wake-word listening is deliberately outside this version's scope.

## Test

```sh
python -m unittest discover -s tests -v
```

Eight regression tests cover command routing, case/whitespace normalization, unknown/unsafe command rejection, deterministic time, stopping, browser failure and speech fallback. Tests mock browser/audio actions: physical Windows audio and real browser launch have not been verified in this environment.

This is educational/demo work, not a completed client assistant, autonomous operating-system agent or voice-cloning system. It stores no input history or credentials.
