#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-05-26
Purpose: Rock the Casbah
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Crow's nest"""
    args = get_args()
    word = args.word
    
    article='an' if word[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
# --------------------------------------------------
if __name__ == '__main__':
    main()
