"""Small allowlisted desktop assistant. No shell or arbitrary URL execution."""
from dataclasses import dataclass
from datetime import datetime
import argparse
import webbrowser

SITES = {'open youtube': ('YouTube', 'https://www.youtube.com'),
         'open google': ('Google', 'https://www.google.com'),
         'play music': ('Spotify', 'https://www.spotify.com'),
         'news': ('Google News', 'https://news.google.com')}

@dataclass(frozen=True)
class Response:
    text: str
    url: str | None = None
    stop: bool = False


def process_command(command: str, now: datetime | None = None) -> Response:
    command = ' '.join(command.casefold().split())
    if command in {'exit', 'quit', 'stop'}:
        return Response('Goodbye.', stop=True)
    if command in {'time', "what's the time", 'what is the time'}:
        return Response('The current local time is ' + (now or datetime.now()).strftime('%H:%M'))
    if command in SITES:
        label, url = SITES[command]
        return Response(f'Opening {label}.', url)
    if command == 'help':
        return Response('Commands: open youtube, open google, play music, news, time, help, exit.')
    return Response('Unknown command. Type help for supported commands.')


def deliver(response: Response, opener=webbrowser.open, speaker=None) -> None:
    print('Jarvis: ' + response.text)
    if response.url:
        try:
            if not opener(response.url):
                print('The browser could not be opened. URL: ' + response.url)
        except Exception:
            print('The browser could not be opened. URL: ' + response.url)
    if speaker:
        try:
            speaker.say(response.text)
            speaker.runAndWait()
        except Exception:
            print('Speech output unavailable; continuing in text mode.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--speech', action='store_true', help='Enable optional local text-to-speech; no microphone capture.')
    args = parser.parse_args()
    speaker = None
    if args.speech:
        try:
            import pyttsx3
            speaker = pyttsx3.init()
        except Exception:
            print('Speech output unavailable. Install the optional dependency and check your audio driver. Continuing in text mode.')
    print('Desktop assistant demo. Type help for commands. Type exit to stop.')
    try:
        while True:
            response = process_command(input('You: '))
            deliver(response, speaker=speaker)
            if response.stop:
                break
    except (EOFError, KeyboardInterrupt):
        print('\nGoodbye.')
    finally:
        if speaker:
            try:
                speaker.stop()
            except Exception:
                pass
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
