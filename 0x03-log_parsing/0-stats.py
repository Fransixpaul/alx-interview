#!/usr/bin/python3
"""
    Prints the accumulated statistics for the log data.

    Outputs:
    - Total file size as "File size: <total size>"
    - Status codes and their occurrence counts, in ascending order.
    Only status codes with occurrences are printed.
    """
import sys

# Step 1: Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Function to print the collected statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    # Step 2: Process each line from stdin
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Step 3: Validate and parse line
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            continue  # Skip if line format is incorrect

        # Step 4: Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
