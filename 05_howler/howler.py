#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-05-31
Purpose: Howler (upper-cases input)
"""
import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='str', help='Input string or file')
    parser.add_argument('-o',
                        '--outfile',
                        help='An output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=None)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    out_fh = args.outfile
    pos_arg = args.text

    if os.path.isfile(pos_arg):
        in_fh = open(pos_arg)
        text = in_fh.read().upper().rstrip()
        in_fh.close()
    else:
        text = pos_arg.upper()

    if out_fh != None:
        print(text, file=out_fh)
        out_fh.close()
    else:
        print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
