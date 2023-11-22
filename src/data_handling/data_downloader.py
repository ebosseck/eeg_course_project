import os.path

from tools.logtools import *
from tools.filetools import *

from . import *


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

    if VALIDATE_DATA:
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
        unzip(zip_path, DATA_BASE_DIR)
        print("Extraction Done.", style=STYLE_DEFAULT)

def fetchData():
    """
    Ensures the raw data is where we expect it to be
    :return:
    """
    ensureDataDirPresent()
    ensureRawDataPresent()

#endregion