import sys
from quiz.app import App

if __name__ == "__main__":
    try:
        sys.exit(App().run())
    except KeyboardInterrupt:
        sys.exit()
