import errno
import os.path

import tools.logtools
from tools.logtools import *
from tools.filetools import *

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

#region Initialisation

def init():
    tools.logtools.ENABLE_FANCY_LOG = FANCY_LOG

#endregion

#region Data Aquisition

# Ilias proofing folder structure

def ensureDataDirPresent():
    """
    Ensures that the base dir for all data is present in the expected location
    :return:
    """
    if not os.path.isdir(DATA_BASE_DIR):
        print(formatString("Data directory not found. Expected at:", style=STYLE_TEXT_RED),
              formatString('"', DATA_BASE_DIR, '"', style=[STYLE_UNDERLINE, STYLE_TEXT_BLUE], sep=''))
        print(formatString("Your current working directory is:", style=STYLE_TEXT_RED),
              formatString('"', os.getcwd(), '"', style=[STYLE_UNDERLINE, STYLE_TEXT_BLUE], sep=''))
        print("Create new data directory ? (y/n)", style=STYLE_TEXT_RED)
        response = input().lower()
        if response != 'y':
            print("Please ensure the data directory exists and is properly configured in this script, then retry.", style=STYLE_TEXT_RED)
            print("Exiting", style=STYLE_TEXT_RED)
            exit(-1)
        try:
            os.makedirs(DATA_BASE_DIR)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def checkAllDataPresent():
    """
    Checks if all data for all subjects is present

    :return:
    """
    for subject in SUBJECT_IDS:
        for file in PER_SUBJECT_FILES:
            current_file = "".join([DATA_BASE_DIR, file.format(subject, subject)])
            if not os.path.exists(current_file):
                print(formatString("File not Found:", style=STYLE_TEXT_RED),
                      formatString('"', current_file, '"', style=[STYLE_UNDERLINE, STYLE_TEXT_BLUE], sep=''))
                return False
    return True

def getZipFile():
    """
    Checks if a pre-downloaded version of the zip file exists. If not, downloads a fresh copy of the data from nemar
    :return:
    """
    zip_path = "".join([DATA_BASE_DIR, DATA_PATH])
    if not os.path.exists(zip_path):
        print("Missing raw data. Download raw data ? (y/n)", style=STYLE_TEXT_RED)
        response = input().lower()
        if response != 'y':
            print("Please ensure all required data is present or allow downloading a fresh copy.", style=STYLE_TEXT_RED)
            print("Exiting", style=STYLE_TEXT_RED)
            exit(-1)

        print(formatString("Downloading data from ", style=STYLE_DEFAULT),
            formatString('"', DATA_DOWNLOAD_URL, '"', style=[STYLE_UNDERLINE, STYLE_TEXT_BLUE], sep=''))
        saveURL(DATA_DOWNLOAD_URL, zip_path)

    print("Validating Data", style=STYLE_DEFAULT)
    chksum = checksum(zip_path)

    if chksum == DATA_CHECKSUM:
        print(formatString("Verification Result: ", style=STYLE_DEFAULT), formatString("OK", style=STYLE_TEXT_GREEN))
    else:
        print(formatString("Verification Result: ", style=STYLE_DEFAULT),
              formatString("FAIL", style=[STYLE_HIGHLIGHT_RED, STYLE_TEXT_WHITE]), ' ')
        print("{:<10} | {:>140}".format("Expected:", formatString(DATA_CHECKSUM, style=STYLE_TEXT_GREEN)))
        print("{:<10} | {:>140}".format("Got:", formatString(chksum, style=STYLE_TEXT_RED)))

    return zip_path

def ensureRawDataPresent():
    """
    Ensures that the raw data is present
    :return:
    """
    if not checkAllDataPresent():
        zip_path = getZipFile()
        print("Extracting files...", style=STYLE_DEFAULT)
        #unzip(zip_path, DATA_BASE_DIR)
        print("Extraction Done.", style=STYLE_DEFAULT)

def fetchData():
    """
    Ensures the raw data is where we expect it to be
    :return:
    """
    ensureDataDirPresent()
    ensureRawDataPresent()

#endregion

#region Preprocessing

#endregion

#region Analysis

#endregion

if __name__ == "__main__":
    init()
    if ENABLE_CHECK_RAW_DATA:
        fetchData()
