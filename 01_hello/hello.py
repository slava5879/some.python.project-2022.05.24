#! python3

import argparse

parser = argparse.ArgumentParser(description='Sey hello!')
parser.add_argument('--name',
                    '-n',
                    metavar='name',
                    default='World',
                    help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')