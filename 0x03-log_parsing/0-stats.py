#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""

import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
          '404': 0, '405': 0, '500': 0}

count = 0
size = 0

try:
    for i in sys.stdin:
        data = i.split()
        data = data[::-1]

        if len(data) > 2:
            count += 1
            if count <= 10:
                size += int(data[0])
                codes = data[1]

            if codes in status.keys():
                status[codes] += 1

            if count == 10:
                print('File size: {}'.format(size))
                for state_code, v in sorted(status.items()):
                    if v != 0:
                        print('{}: {}'.format(state_code, v))
                count = 0
finally:
    print('File size: {}'.format(size))
    for state_code, v in sorted(status.items()):
        if v != 0:
            print('{}: {}'.format(state_code, v))
