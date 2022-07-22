#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-07-22
Purpose: How many bottles
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
    
    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    
    return args
# --------------------------------------------------
def verse(bottles):
    """Sing a verse"""

    next_bottles=bottles - 1 if bottles >=2 else 'No more'
    s1='' if bottles ==1 else 's'
    s2='' if next_bottles ==  1 else 's'

    return f"""{bottles} bottle{s1} of beer on the wall,
{bottles} bottle{s1} of beer,
Take one down, pass it around,
{next_bottles} bottle{s2} of beer on the wall!"""

# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
    
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args=get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))
# --------------------------------------------------
if __name__ == '__main__':
    main()