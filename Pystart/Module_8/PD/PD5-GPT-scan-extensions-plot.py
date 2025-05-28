# PD8 5 - Scan directory extensions (chat GPT improved initial code)

# TASK DESCRIPTION
# Prepare a program that will scan the directory for various
# extensions. The result should be a chart showing these extensions.

from pathlib import Path
import argparse
from collections import Counter
import matplotlib.pyplot as plt


def scan_directory_for_extensions(path):
    """
    Scans the given directory for file extensions and counts their occurrences.

    Args:
        path (str): Path to the directory to scan.

    Returns:
        dict: A dictionary with file extensions as keys and their occurrence counts as values.
    """
    extension_counts = Counter()  # Initialize a Counter to store file extensions and their counts

    # Use Path.glob to iterate through all files in the top-level directory
    for file in Path(path).glob('*'):
        if file.is_file():  # Ensure it's a file and not a directory
            # Extract the file extension, remove the leading dot, and convert to lowercase
            extension = file.suffix.lstrip('.').lower()
            # Increment the count for this extension in the Counter
            extension_counts[extension] += 1

    return dict(extension_counts)  # Convert the Counter to a regular dictionary for returning


def plot_statistics(statistics, output_file='Summary.png'):
    """
    Plots a bar chart for the file extension statistics.

    Args:
        statistics (dict): Dictionary of file extensions and their counts.
        output_file (str): Filename to save the chart image.
    """
    if not statistics:  # Check if the dictionary is empty
        print("No files found in the directory to generate a chart.")  # Notify the user if no data is available
        return  # Exit the function

    # Extract keys (extensions) and values (counts) from the statistics dictionary
    extensions = statistics.keys()
    occurrences = statistics.values()

    # Create a bar chart with a specified figure size and bar color
    plt.figure(figsize=(10, 6))
    plt.bar(extensions, occurrences, color='blue')

    # Add labels and a title to the chart
    plt.xlabel('File Type')
    plt.ylabel('Number of Occurrences')
    plt.title('File Type Distribution')

    # Adjust layout to prevent overlap and save the chart to a file
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Chart saved as {output_file}")  # Notify the user about the saved file


def main():
    """
    The main function to parse arguments, scan the directory, and generate a chart.
    """
    # Set up argument parser for command-line arguments
    parser = argparse.ArgumentParser(
        description='Scans a directory for file extensions and generates a summary chart.',
        prog='Directory Scanner',
        epilog='Author: Mateusz Kuchta'
    )
    parser.add_argument(
        'path',
        type=str,
        help='Path to the directory containing files.'  # Description of the 'path' argument
    )
    args = parser.parse_args()  # Parse the command-line arguments

    # Scan the directory and get statistics for file extensions
    statistics = scan_directory_for_extensions(args.path)

    # Generate and save the bar chart using the collected statistics
    plot_statistics(statistics)


if __name__ == "__main__":
    # Entry point of the script
    main()
