#!/usr/bin/env python3
"""
Author : eugene <eugene@localhost>
Date   : 2020-09-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default: False)',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    is_sorted = args.sorted
    items = args.items
    phrase = 'You are bringing'

    if is_sorted:
        items.sort()

    if len(items) == 1:
        print(f'{phrase} {items[0]}.')
    elif len(items) == 2:
        items = ' and '.join(items)
        print(f'{phrase} {items}.')
    else:
        items[-1] = f'and {items[-1]}'
        items = ', '.join(items)
        print(f'{phrase} {items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
