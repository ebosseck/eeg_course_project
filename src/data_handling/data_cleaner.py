import os
import shutil

from tools.logtools import *

def removeDirectory(file_path: str):
    if os.path.isdir(file_path):
        print(formatString("Removing directory:", style=STYLE_TEXT_LIGHT_RED),
              formatString(file_path, style=STYLE_TEXT_BLUE))
        shutil.rmtree(file_path)