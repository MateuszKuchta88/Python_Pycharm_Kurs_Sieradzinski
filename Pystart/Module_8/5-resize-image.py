# Module 8 - Resize images

# TASK DESCRIPTION
# Prepare a folder called “to_scale” and place any 5-6 files in it
# photos. It is important that the photos are larger than 800 pixels wide.
#  Using the libraries: Pillow and os.walk, navigate through all files including
# directory, then save the thumbnails in the thumbnails folder. The files should have
# the same names.

# Import libraries
from os import walk, path, makedirs
from pathlib import Path
import argparse
from PIL import Image

# Testing data
# file = Path('test.pdf')

# Declare function
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)  # i.e. --dir=.\to_scale

# Tests
args = parser.parse_args()
for directory, directories_in_directory, files_in_directory in walk(args.dir):
    for file in files_in_directory:
        im = Image.open(f'{args.dir}\\{file}')
        thumbnail = im.resize((300, 300))
        if not path.exists(f'./resized'):
            makedirs(f'./resized')
        thumbnail.save(f'resized/{Path(file).stem}_300x300{Path(file).suffix}')

# Print output message
