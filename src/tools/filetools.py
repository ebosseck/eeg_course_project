import errno
import os
import urllib.request
import hashlib
import zipfile as zf
from os.path import basename

from typing import Union, AnyStr, List, Optional


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

def saveURL(url: str, filename: str):
    """
    Save the file from the given URL to disk
    :param url: Download path
    :param filename: Path for the downloaded file
    """
    urllib.request.urlretrieve(url=url, filename=filename)


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


