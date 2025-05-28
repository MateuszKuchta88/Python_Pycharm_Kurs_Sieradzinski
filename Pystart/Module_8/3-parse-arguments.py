# Module 8 - Parse arguments

# TASK DESCRIPTION
# Prepare a program that will receive arguments such as:
# -path (required) (string)
# -target (required) (string)
# -width (integer) (default 300)
# -height (integer) (default 300)
# For now, only display these values one below the other

# Import libraries
import argparse


# Testing data
parser = argparse.ArgumentParser(
    description='Program to parse arguments!',
    prog='Hello World',
    epilog='Author: Mateusz Kuchta'
)

# Declare function
parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('--width', type=int, default=300)
parser.add_argument('--height', type=int, default=300)

# Tests
args = parser.parse_args()

# Print output message
print('path', args.path)
print('target', args.target)
print('width', args.width)
print('height', args.height)
