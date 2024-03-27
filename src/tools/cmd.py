from os import listdir
from os.path import isdir, basename

from .filetools import readFileLines


def ls (directory: str, base_name=True):
    if isdir(directory):
        for f in listdir(directory):
            print(f if base_name else "{}/{}".format(directory, f))
    else:
        if base_name:
            print(basename(directory))
        else:
            print(directory)


def cat(file: str):
    for line in readFileLines(file):
        print(line)
