import errno
import os
import urllib.request
import hashlib
import zipfile as zf

from typing import Union, AnyStr


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


def saveURL(url: str, filename: str):
    """
    Save the file from the given URL to disk
    :param url: Download path
    :param filename: Path for the downloaded file
    """
    urllib.request.urlretrieve(url=url, filename=filename)


def unzip(filename: str, base_path: str):
    with zf.ZipFile(filename, "r", zf.ZIP_DEFLATED, False) as zip_file:
        for info in zip_file.infolist():
            if info.is_dir():
                continue
            print(info.filename)
            # zip_file.read(info, None)
            #TODO: Extract zip file

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