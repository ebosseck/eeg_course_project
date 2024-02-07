import errno
import os
import urllib.request
import hashlib
import zipfile as zf
from os.path import basename
from time import time

from typing import Union, AnyStr, List, Optional
from .logtools import *

def filenameof(path):
    """
    Compute the base filename of path
    :param path: path to compute filename of

    :return: the basename sans last extension
    """
    name = basename(path)

    return '.'.join(name.split('.')[:-1])

def writeFileBinary(path: Union[str, bytes, os.PathLike[str], os.PathLike[bytes], int], content: AnyStr, mode: str="wb"):
    """
    Writes content to a file at the given path

    :param path: Path of the file to write
    :param content: Content to write to the file
    :param mode: File Open mode, 'w' for write, 'a' for append
    :return: None
    """
    dirname = os.path.dirname(path)
    if len(dirname.strip()) > 0 and not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(path, mode)
    try:
        f.write(content)
    finally:
        f.close()


def readFileBinary(path: Union[str, bytes, os.PathLike[str], os.PathLike[bytes], int]) -> AnyStr:
    """
    Read the complete file as bytes

    :param path: Path to read from
    :return: the data of the file
    """
    f = open(path, "rb")
    result = None
    try:
        result = f.read()
    finally:
        f.close()

    return result


def writeFile(path: Union[str, bytes, os.PathLike[str], os.PathLike[bytes], int], content: AnyStr, mode: str="w"):
    """
    Writes content to a file at the given path

    :param path: Path of the file to write
    :param content: Content to write to the file
    :param mode: File Open mode, 'w' for write, 'a' for append
    :return: None
    """
    dirname = os.path.dirname(path)
    if len(dirname.strip()) > 0 and not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(path, mode, encoding='utf8')
    try:
        f.write(content)
    finally:
        f.close()


def readFileLines(path: Union[str, bytes, os.PathLike[str], os.PathLike[bytes], int]) -> List[str]:
    """
    Read the file Line by Line and strip each line of leading and trailing whitespaces

    :param path: Path to read from
    :return: a list of stripped Lines
    """
    f = open(path, "r", encoding='utf8')
    lines = []
    try:
        for line in f:
            lines.append(line)
    finally:
        f.close()

    return lines

start_time = time()
last_reported_progress = 0
delta_progress = 0.0001

def saveURL(url: str, filename: str):
    global start_time, last_reported_progress, delta_progress
    """
    Save the file from the given URL to disk
    :param url: Download path
    :param filename: Path for the downloaded file
    """
    start_time = time()
    last_reported_progress = 0
    delta_progress = 0.001 # report progress in 0.1 % steps

    urllib.request.urlretrieve(url=url, filename=filename, reporthook=reportDownloadProgress)


def reportDownloadProgress(blocks, curr_file, expected_size):
    global last_reported_progress
    progress = (blocks*curr_file)/expected_size

    if progress >= last_reported_progress + delta_progress:
        progress_time = time() - start_time
        eta = progress_time * (1 / progress - 1)
        print(formatString("Download Progress:", style=STYLE_DEFAULT),
              formatString("{: 5.2f}".format(progress * 100), ' %', style=[STYLE_BOLD, STYLE_TEXT_BLUE], sep=''),
              formatString('ETA: ', "{: 4}".format(int(eta//60)), ':', "{:05.2f}".format(eta%60), style=[STYLE_BOLD, STYLE_TEXT_YELLOW], sep=''))
        last_reported_progress = progress



def unzip(filename: str, base_path: str, prefix: Optional[str] = "ds003702/sub"):
    with zf.ZipFile(filename, "r", zf.ZIP_DEFLATED, False) as zip_file:
        for info in zip_file.infolist():
            if info.is_dir():
                continue
            if prefix is not None:
                if not info.filename.startswith(prefix):
                    continue
            writeFileBinary("".join([base_path, info.filename]), zip_file.read(info, None))

def checksum(filename: str):
    """
    Computes the checksum of the file (SHA2-512)

    :param filename: Filename to compute checksum for
    :return:
    """
    hash = hashlib.sha512()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


