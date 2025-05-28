# PD8 3 - Merge txt files (chat GPT improved initial code)

# TASK DESCRIPTION
# Find a way to list files in a directory, then
# write a program that will find all text files
# in the folder of your choice and to a new file called
# scalone.txt will insert the result of combining these files.

from pathlib import Path
import argparse


def parse_arguments():
    """
    Parses command-line arguments to get the target directory path.

    Returns:
        str: The path to the directory containing text files.
    """
    parser = argparse.ArgumentParser(
        description='Merge all .txt files in a directory into a single file.',
        prog='MergeTxtFiles',
        epilog='Author: Mateusz Kuchta'
    )
    parser.add_argument('path', type=str, help='Path to the directory containing text files.')
    args = parser.parse_args()
    return args.path


def merge_text_files(directory_path):
    """
    Merges all .txt files in the specified directory into a single file named 'scalone.txt'.

    Args:
        directory_path (str): Path to the directory containing the text files.

    Returns:
        None
    """
    target_file = Path(directory_path) / "scalone.txt"

    try:
        with open(target_file, 'w', encoding='utf8') as output_file:
            for file in Path(directory_path).glob("*.txt"):
                # Skip the target file to avoid self-merging
                if file.name == "scalone.txt":
                    continue

                try:
                    with open(file, 'r', encoding='utf8') as input_file:
                        output_file.write(input_file.read())
                        output_file.write("\n")  # Ensure files are separated by a newline
                except Exception as e:
                    print(f"Error reading file {file}: {e}")
        print(f"All text files have been merged into {target_file}.")
    except Exception as e:
        print(f"Error writing to file {target_file}: {e}")


def main():
    """
    Main function to parse arguments and merge text files.
    """
    directory_path = parse_arguments()

    if Path(directory_path).exists() and Path(directory_path).is_dir():
        merge_text_files(directory_path)
    else:
        print(f"Invalid directory path: {directory_path}")


if __name__ == "__main__":
    main()
