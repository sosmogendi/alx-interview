#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_parts = line.split(" ")
        if len(line_parts) > 4:
            code = line_parts[-2]
            size = int(line_parts[-1])
            if code in status_code_counts:
                status_code_counts[code] += 1
            total_file_size += size
            line_counter += 1

        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(status_code_counts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_code_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
