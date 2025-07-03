import os

import requests
import json

import ctypes
import winreg

from bntu import cli, __app_name__, __version__

application_dir = os.path.dirname(__file__)

FILE_NAME_WORKING = "working"
FILE_NAME_CURRENT = "current"

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()