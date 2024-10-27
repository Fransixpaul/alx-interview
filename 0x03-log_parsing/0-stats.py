#!/usr/bin/python3
"""
This module processes HTTP log lines from standard input and computes metrics
including total file size and counts of specific HTTP status codes.

The script outputs cumulative statistics every 10 lines of input,
or when interrupted
by a keyboard signal (CTRL + C).
"""

import sys

# Initialize variables to store metrics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """
    Prints the accumulated metrics including the total file size and counts
    for each HTTP status code encountered.

    Outputs:
        - Total file size in the format: "File size: <total size>"
        - Counts for each HTTP status code in ascending order if they appear.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line):
    global total_file_size
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update the total file size
        total_file_size += file_size

        # Update the count for the status code if it is in the predefined list
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (ValueError, IndexError):
        # Skip lines that do not match the required format
        pass


try:
    # Process each line from standard input
    for line in sys.stdin:
        line_count += 1
        process_line(line.strip())

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    # Ensure final statistics print if log ends without interruption
    print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interrupt
    print_stats()
    raise
