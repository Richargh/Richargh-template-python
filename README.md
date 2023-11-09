# Template for Basic Python

## Features

* Python
* Type Hints

## Prerequisites

Make sure an appropriate python version is installed. If you have [pyenv](https://github.com/pyenv/pyenv) installed, you can call:

* `pyenv local` (will install the version from [.python-version](.python-version))

### Setup Virtual Environment
1. Create a virtual environment by running `python3 -m venv venv` in the project directory.
2. Activate the virtual environment:
   - On macOS and Linux, run `source venv/bin/activate`.
   - On macOS with fish shell, run `source venv/bin/activate.fish`.
   - On Windows, run `venv\Scripts\activate.bat`.

## Usage

* Run tests with `python -m unittest discover`.

## Acknowledgements

### Pyenv vs Virtual Environment

* `pyenv` manages multiple versions of Python itself.
* `virtualenv/venv` manages virtual environments for a specific Python version.
