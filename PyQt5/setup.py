from cx_Freeze import setup, Executable
import sys
base = 'WIN32GUI' if sys.platform == "win32" else None


executables = [Executable("hello.py", base=base, icon='icon.ico')]

packages = []
include_files=['icon.png']
options = {
    'build_exe': {
        'packages':packages,
        'include_files': include_files
    },

}

setup(
    name = "prog",
    options = options,
    version = "1.0",
    description = 'desc of program',
    executables = executables
)