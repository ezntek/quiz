# quiz

I was forced to make this by these 2 student club leaders. No offense intended towards these leaders, but I was still forced to make this.

## Installation
Clone the repository, and issue `pip install .`. Alternatively, one can use `pipx` to avoid breaking system packages.

The general process goes something like this:
```
git clone https://github.com/ezntek/quiz --depth=1 # do this if you don't plan on contributing
cd quiz
pipx install .
```

## Contributing
**NOTE**: Be sure to have poetry installed on your system.

You can contribute to this if you want (read: don't, because this is really rushed). Just clone the repository, and set up a virtual environment:

```
poetry config virtualenvs.in-project true # set up if you want better code editor integration
poetry config use python3 # replace python3 with your interpreter
```

Then, install the dependencies:

```
poetry install
```

If you are using neovim, you can launch `nvim` like this:

```
poetry run nvim .
```

and run the app like this:

```
poetry run python quiz
```

### Setting up a formatter

Do use yapf with the settings found in the `pyproject.toml`. I cannot get it working with my code editor, so I don't run it very much. 
