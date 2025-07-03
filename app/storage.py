import os
import shutil
from .config import UPLOAD_DIRECTORY

def save_file(file):
    with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file.filename

def list_files():
    return os.listdir(UPLOAD_DIRECTORY)

def file_path(filename):
    return os.path.join(UPLOAD_DIRECTORY, filename)
