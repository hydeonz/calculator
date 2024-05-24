import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("calc.py", base=base)]

options = {
    'build_exe': {
        'packages': ["tkinter", "math"],
        'include_files': [],
    },
}

setup(
    name="Calculator",
    version="1.0",
    description="Simple calculator using Tkinter",
    options=options,
    executables=executables
)