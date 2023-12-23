import argparse

parser = argparse.ArgumentParser(prog='ccwc',
                                 description='Generate various statistics about a file')
parser.add_argument('-c', '--bytesCount', type=str)

args = parser.parse_args()

print(args.bytesCount)