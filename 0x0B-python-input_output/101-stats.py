#!/usr/bin/python3
"""Module"""


import sys


count = 0
size = 0
errors = {}
try:
    for content in sys.stdin:
        line = content.rstrip()
        arr = line.replace('\n', '').split(' ')
        code = int(arr[7])
        filesize = int(arr[8])
        count = count + 1
        size = size + filesize

        if code not in errors.keys():
            errors[code] = 1
        else:
            errors[code] = errors[code] + 1

        if count == 10:
            print('File size: {}'.format(size))
            for key, value in sorted(errors.items()):
                print('{}: {}'.format(key, value))
            count = 0
            errors = {}
            size = 0
except KeyboardInterrupt:
    print('File size: {}'.format(size))
    for key, value in sorted(errors.items()):
        print('{}: {}'.format(key, value))
sys.stdout.flush()
