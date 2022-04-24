#!/usr/bin/python

from diacritics import remove_diacritics, has_diacritics
import os


def get_files_in_directory(path: str):
    # get all folders in path
    folders = os.listdir(path)

    for folder in folders:
        if os.path.isdir(path + folder):
            get_files_in_directory(path + folder + "/")
        print(path + folder + " -> " + (remove_diacritics(folder)
              if has_diacritics(folder) else "není nutné přejmenovat"))
        if has_diacritics(folder):
            os.rename(path + folder, path + remove_diacritics(folder))
