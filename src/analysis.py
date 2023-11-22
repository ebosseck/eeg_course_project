import errno
import os.path

import tools.logtools
import data_handling.data_downloader as dl
import data_handling.data_patcher as patch
import data_handling as dh

from mne_bids import BIDSPath, read_raw_bids, inspect_dataset

import matplotlib
matplotlib.use('qtagg')

#region Configuration

FANCY_LOG = True # Set to false, in case log output contains lots of strange character combinations, but no colors.

#region Raw Data

ENABLE_CHECK_RAW_DATA = True

DATA_BASE_DIR = "../data/"
# Alternate download url
# https://github.com/OpenNeuroDatasets/ds003702/archive/refs/heads/master.zip
DATA_DOWNLOAD_URL = "https://nemar.org/dataexplorer/download?filepath=/data/nemar/openneuro/zip_files/ds003702.zip"
DATA_PATH = "ds003702.zip"
DATA_CHECKSUM = '95f393b9c197cb4c54d7b56577438ef2ef552e2190198b9af350d774820125d45216d873f29cbd2c9c8212387f6d94825cff1c8ba6a7c76e8c3ba7894fbe8140'



#endregion

#region Preprocessing

#endregion

#region Analysis

#endregion

#endregion

#region Data

#region data check

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

#endregion

#endregion

#region processing

#region Initialisation

def init():
    tools.logtools.ENABLE_FANCY_LOG = FANCY_LOG

    dh.DATA_BASE_DIR = DATA_BASE_DIR
    dh.DATA_DOWNLOAD_URL = DATA_DOWNLOAD_URL
    dh.DATA_PATH = DATA_PATH
    dh.DATA_CHECKSUM = DATA_CHECKSUM

    dh.PER_SUBJECT_FILES = PER_SUBJECT_FILES
    dh.SUBJECT_IDS = SUBJECT_IDS
#endregion

#region Preprocessing

#endregion

#region Analysis

#endregion

#endregion

if __name__ == "__main__":
    init()
    if ENABLE_CHECK_RAW_DATA:
        dl.fetchData()
    patch.patchAllFiles() # Correct errors made when exporting data

    bids_root = "../data/ds003702/"

    bids_path = BIDSPath(subject='01', task="SocialMemoryCuing",
                         datatype='eeg', suffix='eeg',
                         root=bids_root)

    inspect_dataset(bids_path, l_freq=2, h_freq=30)
