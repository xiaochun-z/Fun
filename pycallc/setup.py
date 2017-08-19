#!/usr/bin/env python
# --coding:utf-8--

from cx_Freeze import setup, Executable
import sys

base = 'WIN32GUI' if sys.platform == "win32" else None

executables = [Executable("MainWindow.py", base=base, icon='icon.ico')]

packages = []
include_files = ['icon.png']
options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files
    },

}

setup(
    name="proxy server setting",
    options=options,
    version="1.0",
    description='set the proxy for internet explorer',
    executables=executables
)
