import shutil
import colorama

from sys import stdout, stdin

from .question import Question
from . import Config
from .loader import load_config

ESC = "\033"

def enter_alt_screen():
    stdout.write("\033[?1049h")
    stdout.flush()

def exit_alt_screen():
    stdout.write("\033[?1049l")
    stdout.flush()

def cursor_to(x: int, y: int):
    stdout.write(f"{ESC}[{y};{x}H")
    stdout.flush()

def clear_scrn():
    stdout.write(f"{ESC}[2J")
    stdout.flush()

def ask_question(config: Config, qn: Question, iteration: int):
    t_width, t_height = shutil.get_terminal_size()
    
    # this function does not get any user input.
    # see the main loop for details.
    def display_question(iteration: int, correct: bool):
        clear_scrn()

        nonlocal t_width
        nonlocal t_height

        # centering stuff
        text = f"What is {colorama.Style.BRIGHT}{colorama.Fore.CYAN}{qn.__repr__()}{colorama.Style.RESET_ALL}?"
        text_len = len(text)
        cur_x, cur_y = int((t_width / 2) - (text_len/4)), int(t_height / 2)

        # print the current question
        cursor_to(cur_x, cur_y-2)
        stdout.write(f"{colorama.Style.BRIGHT}{colorama.Fore.CYAN}{iteration}/{config['count']}{colorama.Style.RESET_ALL}")
        stdout.flush()

        # print the question text
        cursor_to(cur_x, cur_y-1)
        stdout.write(text)
        stdout.flush()
        
        # write the prompt
        cursor_to(cur_x, cur_y+1)
        proompt = f"{colorama.Fore.GREEN}✓ {colorama.Fore.RESET}" if correct else f"{colorama.Fore.RED}× {colorama.Fore.RESET}" # spelt proompt on purpose
        stdout.write(proompt)
        stdout.flush()
    
    # begin by displaying the <correct> symbol.
    #
    # if it broke out of the loop, it means
    # that the previous answer is correct anyway.
    is_prev_correct = True
    while True:
        ans = qn.solve()
        display_question(iteration, is_prev_correct)
        user_ans_s = stdin.readline()

        try:
            user_ans = int(user_ans_s.strip())
        except ValueError:   
            # continue if the user answer is not a valid number
            is_prev_correct = False
            continue

        if user_ans == ans:
            return # break out of the current function
        else:
            # now display the X sign due to incorrectness
            is_prev_correct = False

def run():
    config = load_config()

    # pass in the config for question generation
    # avoids parsing the file multiple times
    qns = [Question(config) for _ in range(config["count"])]
    for it, qn in enumerate(qns):
        # make the iteration human readable by adding one
        ask_question(config, qn, it+1)
