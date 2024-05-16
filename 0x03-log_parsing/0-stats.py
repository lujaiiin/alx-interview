#!/usr/bin/python3
"""modules"""
import sys


def formated_print(data):
    """formated print funct"""

    i = "File size: {}\n".format(data['size'])
    for key in data['codes']:
        if data['codes'][key] != 0:
            i += '{}: {}\n'.format(key, data['codes'][key])
    sys.stdout.write(i)
    sys.stdout.flush()


def extract(data, line):
    """extract function """

    line = line.rsplit()
    try:
        sta = line[-2]
        if sta in data['codes']:
            data['codes'][sta] += 1
        data['size'] += int(line[-1])
    except (IndexError, ValueError):
        pass


def main(data):
    """ main """

    j = 0
    for line in sys.stdin:
        extract(data, line)
        j += 1
        if j % 10 == 0:
            formated_print(data)
    formated_print(data)


if __name__ == '__main__':
    data = {
        'size': 0, 'codes': {
            '200': 0, '301': 0,
            '400': 0, '401': 0, '403': 0,
            '404': 0, '405': 0, '500': 0
        }
    }

    try:
        main(data)
    except KeyboardInterrupt:
        formated_print(data)
        raise
