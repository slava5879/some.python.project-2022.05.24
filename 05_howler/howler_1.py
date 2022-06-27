#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-05-31
Purpose: Rock the Casbah
"""
import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')
    parser.add_argument('-o',
                        '--outdir',
                        help='--------',
                        action='store_true')
    parser.add_argument('-e', '--ee', help='Swith to lowercase output', action='store_true')
    args = parser.parse_args()

    if os.path.isdir(args.text):
        files = os.listdir(args.text)
        #args.text = open(args.text).read().rstrip()
        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    #print(args.text)

    if args.outdir:
        for file in files:
            content = open(os.path.join(args.text,file)).read().rstrip()

            out_fh = open(file, 'wt')

            if args.ee:
                out_fh.write(content.lower() + '\n')
            else:    
                out_fh.write(content.upper() + '\n')
            out_fh.close()
    else:
        out_fh=sys.stdout
        if args.ee:
            out_fh.write(args.text.lower() + '\n')
        else:
            out_fh.write(args.text.upper() + '\n')
        out_fh.close()




# --------------------------------------------------
if __name__ == '__main__':
    main()
