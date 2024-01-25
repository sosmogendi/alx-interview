#!/usr/bin/python3
import sys

def print_statistics(total_file_size, status_code_counts):
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        print("{}: {}".format(code, count))

def parse_log_line(line):
    try:
        parts = line.split()
        if len(parts) == 9:
            status_code = int(parts[8])
            file_size = int(parts[7])

            if status_code in status_code_counts:
                return status_code, file_size
    except (ValueError, IndexError):
        pass
    return None, None

def main():
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            if status_code is not None and file_size is not None:
                total_file_size += file_size
                status_code_counts[status_code] += 1

                line_count += 1
                if line_count == 10:
                    print_statistics(total_file_size, status_code_counts)
                    line_count = 0
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        # Ignore Broken Pipe Error when the output is closed
        pass

    # Print final statistics before exiting
    print_statistics(total_file_size, status_code_counts)

if __name__ == "__main__":
    main()
