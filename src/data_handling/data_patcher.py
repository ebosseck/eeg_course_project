
import tools.filetools as files

EXTENSIONS = ['vmrk', 'vhdr']
FILENAME = 'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg'

PATTERNS = {
    'DataFile': '{}.eeg',
    'MarkerFile': '{}.vmrk'
}

DATA_BASE_DIR = "../../data/"

SUBJECT_IDS = [ 1,  2,  3,  4,  5,  6,  7,      9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41,     43, 44, 45, 46,     48, 49, 50]

#endregion

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
