
import tools.filetools as files

from . import *


def patch_bids_file(path: str):
    filename = files.filenameof(path)
    lines = files.readFileLines(path)

    filtered = []

    for line in lines:
        elements = line.split('=')
        if elements[0] in PATTERNS:
            filtered.append('='.join([elements[0], PATTERNS[elements[0]].format(filename)]))
        else:
            filtered.append(line.strip())

    files.writeFile(path, '\n'.join(filtered))

def patchAllFiles():

    for sub in SUBJECT_IDS:
        for ext in EXTENSIONS:
            filename = ".".join([FILENAME.format(sub, sub), ext])
            patch_bids_file(DATA_BASE_DIR + filename)
