import sys
from os.path import dirname, abspath, join, isfile
from pathlib import Path


def retrieve_data_files(module, filename, subpath="data", current_folder="./"):
    home = str(Path.home())
    search_folders = [
        dirname(abspath(current_folder)),
        join(dirname(abspath(current_folder)), module),
        join(sys.prefix, module),
        join(sys.exec_prefix, module),
        join(home, ".local", module)
    ]
    for folder in search_folders:
        file = join(folder, subpath, filename)
        if isfile(file):
            return file
    raise FileNotFoundError("Cannot find data file %s" % filename)
