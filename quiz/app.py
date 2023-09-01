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

    def _ask_qn(self, qn: Question, correct: bool, iteration: int) -> bool:
        def _ask(correct: bool, iteration: int):
            # clear
            _clear(self.stdout)

            # centering stuff
            text = f"What is {colorama.Style.BRIGHT}{colorama.Fore.BLUE}{qn.__repr__()}{colorama.Style.RESET_ALL}?"
            text_len = len(text)
            cur_x, cur_y = int((self.t_width / 2) - (text_len/4)), int(self.t_height / 2)

            _cursor_to(self.stdout, cur_x, cur_y-2)
            self.stdout.write(f"{colorama.Style.BRIGHT}{colorama.Fore.BLUE}{iteration}/{self._config['count']}{colorama.Style.RESET_ALL}")
            self.stdout.flush()

            _cursor_to(self.stdout, cur_x, cur_y-1)
            self.stdout.write(text)
            self.stdout.flush()
            
            _cursor_to(self.stdout, cur_x, cur_y+1)
            proompt = f"{colorama.Fore.GREEN}✓ {colorama.Fore.RESET}" if correct else f"{colorama.Fore.RED}× {colorama.Fore.RESET}" # spelt proompt on purpose
            self.stdout.write(proompt)
            self.stdout.flush()
        
        # avoid weird python function argument mutation behavior
        correct_internal = correct
        while True:
            ans = qn.solve()
            _ask(correct_internal, iteration)
            user_ans_s = self.stdin.readline()
            try:
                if int(user_ans_s.strip()) == ans:
                    return True
                else:
                    correct_internal = False
            except ValueError:            
                correct_internal = False

    def run(self):
        qns = [Question(self._config) for _ in range(self._config["count"])]
        correct = False
        for it, qn in enumerate(qns):
            correct = self._ask_qn(qn, correct, it+1)
