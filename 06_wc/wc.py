#!/usr/bin/env python3
"""
Author : eugene <eugene@localhost>
Date   : 2020-09-20
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        help='Input file(s)',
                        default=[sys.stdin]
                        )

    return parser.parse_args()


def create_stat_obj():
    return {'lines': 0, 'words': 0, 'bytes': 0}


result = {'lines': 0, 'words': 0, 'bytes': 0}


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.file

    for fh in files:
        current_stat = create_stat_obj()
        for line in fh:
            current_stat['lines'] += 1
            current_stat['words'] += len(line.split())
            current_stat['bytes'] += len(line)
        else:
            result['lines'] += current_stat['lines']
            result['words'] += current_stat['words']
            result['bytes'] += current_stat['bytes']

            print('{:8}{:8}{:8} {}'.format(
                current_stat['lines'],
                current_stat['words'],
                current_stat['bytes'],
                fh.name
            ))

    if len(files) > 1:
        print('{:8}{:8}{:8} {}'.format(
            result['lines'],
            result['words'],
            result['bytes'],
            'total'
        ))


# --------------------------------------------------
if __name__ == '__main__':
    main()
