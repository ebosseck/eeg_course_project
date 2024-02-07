from pathlib import Path

CLEAN_DATA = True

DATA_BASE_DIR = "../data/"
# Alternate download url
# https://github.com/OpenNeuroDatasets/ds003702/archive/refs/heads/master.zip
DATA_DOWNLOAD_URL = "https://nemar.org/dataexplorer/download?filepath=/data/nemar/openneuro/zip_files/ds003702.zip"
DATA_DOWNLOAD_URL_ALT = "https://github.com/OpenNeuroDatasets/ds003702/archive/refs/heads/master.zip"

DATA_PATH = "ds003702.zip"
DATA_CHECKSUM = '95f393b9c197cb4c54d7b56577438ef2ef552e2190198b9af350d774820125d45216d873f29cbd2c9c8212387f6d94825cff1c8ba6a7c76e8c3ba7894fbe8140'
VALIDATE_DATA = False

NO_QUESTIONS = True

PER_SUBJECT_FILES = [
    'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_channels.tsv',
    'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg.eeg',
    'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg.json',
    'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg.vhdr',
    'ds003702/sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg.vmrk',
]

SUBJECT_IDS = [ 1,  2,  3,  4,  5,  6,  7,      9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41,     43, 44, 45, 46,     48, 49, 50]

#region Patching
FILENAME = 'sub-{:02d}/eeg/sub-{:02d}_task-SocialMemoryCuing_eeg'

EXTENSIONS = ['vmrk', 'vhdr']

PATTERNS = {
    'DataFile': '{}.eeg',
    'MarkerFile': '{}.vmrk'
}
#endregion


def getDataPathFromBidsRoot(bids_path: str) -> str:
    return str(Path(bids_path).parent) + '/'