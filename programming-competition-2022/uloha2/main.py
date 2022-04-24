
# import OS module
import os
import sys
from diacritics import remove_diacritics, has_diacritics
from get_file import get_files_in_directory

path: str

# if there is no parameter
if len(sys.argv) < 2:
    print("Nebyla zadána cesta k adresáři")

    # ask for path as input
    if input("Přejete si zadat cestu nyní? (y/n) ").capitalize() == "Y":
        path = input("Zadejte cestu k adresáři: ")
    else:
        exit()
# if path is given
else:
    path = sys.argv[1]

# check if directory is in correct format
if path[:-1] != "/":
    path += "/"


get_files_in_directory(path)
print(path[:-1] + " -> " + (remove_diacritics(path)
                            if has_diacritics(path) else "není nutné přejmenovat"))
os.rename(path,  remove_diacritics(path))
