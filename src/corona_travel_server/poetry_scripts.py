from pathlib import Path
from subprocess import call

scr_path = Path(__file__) / ".."
scr_path = scr_path.resolve()


def mypy():
    call(["mypy", scr_path])


def black():
    call(["black", scr_path])

def dev():
    call(["uvicorn", "corona_travel_server.app:app", "--reload", "--reload-dir", scr_path, "--port", "4000"])
