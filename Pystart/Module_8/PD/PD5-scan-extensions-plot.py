# PD8 5 - Scan directory extensions

# TASK DESCRIPTION
# Prepare a program that will scan the directory for various
# extensions. The result should be a chart showing these extensions

from pathlib import Path
from os import walk
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(
    description='Description',
    prog='Take given directory',
    epilog='Author: Mateusz Kuchta'
)
parser.add_argument('path', type=str, help='Path to the directory containing files.')
args = parser.parse_args()
statistics = {}
for directory, directories_in_directory, files_in_directory in walk(args.path):
    for file in files_in_directory:
        if directory == args.path:
            extension = Path(file).suffix.replace('.', '')
            statistics.update({extension: statistics.get(extension, 0) + 1})

fig1, ax1 = plt.subplots()
extensions = statistics.keys()
nof_occurrence = statistics.values()
ax1.bar(extensions, nof_occurrence)
ax1.set_xlabel('file type')
ax1.set_ylabel('nof occurrence')
plt.savefig('Summary.png')
