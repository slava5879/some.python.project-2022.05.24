#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-06-29
Purpose: Gashlycrumb
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+',
                        type=str)
    parser.add_argument('-f',
                        '--file',
                        help='Input file (default: gashlycrumb.txt)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    dict={line[0] : line.rstrip() for line in args.file}

    for letter in args.letter:
        print(dict.get(letter.upper(), f'I do not know "{letter}".'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
