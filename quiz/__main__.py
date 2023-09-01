import sys
from app.app import run, enter_alt_screen, exit_alt_screen

if __name__ == "__main__":
    try:
        enter_alt_screen()
        run()
    except KeyboardInterrupt:
        pass
    finally:
        exit_alt_screen()
        sys.exit()
