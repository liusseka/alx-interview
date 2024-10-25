#!/usr/bin/python3
'''
The script reads stdin line by line and computes metrics:

    - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
    - After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size> (see input format above)
    - Number of lines by status code:
    - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: <status code>: <number>
    - status codes should be printed in ascending order
'''
import sys
import re
import signal

# Initialize data structures
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

def print_statistics():
    """Print the statistics gathered so far."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_statistics()
    sys.exit(0)

# Register signal handler for graceful exit on CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Regular expression for parsing the log lines
log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>.+?)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'

try:
    for line in sys.stdin:
        line_count += 1
        match = re.match(log_pattern, line)
        if match:
            status = int(match.group('status'))
            size = int(match.group('size'))
            total_size += size
            
            if status in status_counts:
                status_counts[status] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Handle CTRL + C gracefully
    print_statistics()

except Exception as e:
    print("Error processing input: {}".format(e))
