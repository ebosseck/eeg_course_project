import os
import shutil


def removeDirectory(file_path: str):
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)