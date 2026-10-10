import contextlib
from datetime import datetime
import io
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from assistant import process_command, deliver, SITES

class AssistantTests(unittest.TestCase):
    def test_allowlist(self):
        for command, (_,url) in SITES.items():
            self.assertEqual(process_command(command).url,url)
        self.assertEqual(process_command('  OPEN    GOOGLE  ').url,SITES['open google'][1])
    def test_unknown_and_arbitrary_targets(self):
        for command in ['', 'open https://example.com', 'open google and delete files', 'runtime', 'play unknown track', 'rm -rf /']:
            self.assertIsNone(process_command(command).url)
            self.assertFalse(process_command(command).stop)
    def test_time(self):
        self.assertEqual(process_command('time',datetime(2026,1,1,9,7)).text,'The current local time is 09:07')
    def test_exit(self):
        for command in ['exit','quit','stop']:
            self.assertTrue(process_command(command).stop)
        self.assertFalse(process_command('stop now').stop)
    def test_help(self):
        self.assertIn('open youtube',process_command('help').text)
    def test_browser_failure_is_visible(self):
        out=io.StringIO()
        with contextlib.redirect_stdout(out):
            deliver(process_command('open google'),opener=lambda _:False)
        self.assertIn('could not be opened',out.getvalue())
    def test_no_browser_call_for_text(self):
        calls=[]
        with contextlib.redirect_stdout(io.StringIO()):
            deliver(process_command('help'),opener=lambda url:calls.append(url))
        self.assertEqual(calls,[])
    def test_speech_failure_falls_back(self):
        class BrokenSpeaker:
            def say(self,text):raise RuntimeError('Audio unavailable')
        out=io.StringIO()
        with contextlib.redirect_stdout(out):
            deliver(process_command('help'),speaker=BrokenSpeaker())
        self.assertIn('continuing in text mode',out.getvalue())
if __name__=='__main__':unittest.main()
