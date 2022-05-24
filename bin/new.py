#! python3
"""
Author:  Slava
Purpose: Say hello
"""

import argparse


#------------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Say hello!')
    parser.add_argument('--name',
                        '-n',
                        metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


#-------------------------------------------------------------------
def main():
    pass


#-------------------------------------------------------------------
if __name__ == '__main__':
    main()