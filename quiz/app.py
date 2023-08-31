import sys
import shutil
import colorama

from .loader import load_config
from typing import TextIO
from quiz.question import Question

ESC = "\033"

def _cursor_to(stdout: TextIO, x: int, y: int):
    stdout.write(f"{ESC}[{y};{x}H")
    stdout.flush()

def _clear(stdout: TextIO):
    stdout.write(f"{ESC}[2J")
    stdout.flush()

class App:
    def __init__(self):
        self._config = load_config()
        self.stdout = sys.stdout
        self.stdin = sys.stdin
        self.t_width, self.t_height = shutil.get_terminal_size()

    def _ask_qn(self, qn: Question):
        def _ask(a):
            _clear(self.stdout)
            _cursor_to(self.stdout, 0, 0)
            text = f"What is {colorama.Style.BRIGHT}{colorama.Back.BLUE}{qn.__repr__()}{colorama.Style.RESET_ALL}? {a}"
            self.stdout.write(text)
            self.stdout.flush()
            _cursor_to(self.stdout, 0, self.t_height)
            self.stdout.write("> ")
            self.stdout.flush()
        
        correct = False
        while not correct:
            ans = qn.solve()
            _ask(ans)
            user_ans_s = self.stdin.readline()
            try:
                if int(user_ans_s.strip()) == ans:
                    break
            except ValueError:            
                continue

    def run(self):
        qns = [Question(self._config) for _ in range(10)]
        for qn in qns:
            self._ask_qn(qn)
