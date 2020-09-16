#!/usr/bin/env python3
"""
Author : eugene <eugene@localhost>
Date   : 2020-09-16
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_file = args.outfile
    text = args.text

    print(text.upper()
          if not os.path.isfile(text)
          else open(text).read().upper(),
          file=open(out_file, 'wt') if out_file else sys.stdout)


# --------------------------------------------------
if __name__ == '__main__':
    main()
