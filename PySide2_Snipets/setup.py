import sys
import os
import cx_freeze import setup, Executable

# lancement avec < python setup.py build >

files = ['icon.ico', 'themes/']

target = Executable(
    script = 'main.py',
    base = 'Win32GUI',
    icon = 'icon.ico'
)

setup(
    name = 'applicationName',
    version = '1.0.0',
    description = 'Description de l\'application ici',
    author = 'Frédéric Quivron',
    options = {'build_exe' : {'include_files': files}},
    executable = [target]
)

