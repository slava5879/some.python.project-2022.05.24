#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-06-30
Purpose: Aples and bananas
"""
import argparse
import os
import re
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Aples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')
    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))
    
    args=parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text=open(args.text).read().rstrip()
    
    return args
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text=args.text
    vowel = args.vowel
    
    pattern = '[aeiou]'

    text=re.sub(pattern, vowel, text)
    text=re.sub('[AEIOU]', vowel.upper(), text)
    
    print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()
