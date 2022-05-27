#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-05-27
Purpose: Picnic
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Picnic desc',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='item(s) to bring')
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Picnic"""
    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]

    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
