#!/usr/bin/python3
'''
The script reads stdin line by line and computes metrics
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
