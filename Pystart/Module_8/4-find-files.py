# Module 8 - Find files

# TASK DESCRIPTION
# Write a program that will receive a specific path from the user
# directory and file extension.
#  e.g. python find_files.py --dir=sample --extension=jpg
#  ➔ The result of the operation should be to display all files
# having such an extension.

# Import libraries
from os import walk
from pathlib import Path
import argparse

# Testing data
# file = Path('test.pdf')

# Declare function
# file extension
# print(file.suffix)
# file prefix
# print(file.stem)
# does file exist
# print(file.exists())
# show path to file
# print(file.resolve())
# is it file?
# print(file.is_file())
# is it directory?
# print(file.is_dir())
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)  # i.e. --dir=C:\D\mojeDokumenty\MojePrace
parser.add_argument('--extension', type=str)  # i.e. --extension=.docx

# Tests
args = parser.parse_args()

# Print output message
for directory, directories_in_directory, files_in_directory in walk(args.dir):
    for file in files_in_directory:
        if Path(file).suffix == args.extension:
            print(file)
