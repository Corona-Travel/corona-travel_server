from pathlib import Path
from subprocess import call


def mypy():
    call(["mypy", Path(__file__)/".."])
