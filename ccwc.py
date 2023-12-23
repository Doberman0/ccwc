import argparse 
import os

def filesize_bytes(file_path : str) -> int:
    return os.path.getsize(file_path)

def num_of_lines(file_path : str) -> int:
    with open(file_path) as file:
        num_of_lines = len(file.readlines())
    return num_of_lines

# TODO: Add logic
def num_of_words(file_path : str) -> int:
    return 0

parser = argparse.ArgumentParser(prog='ccwc',
                                 description='Generate various statistics about a file')
parser.add_argument('-c', '--bytes_count', type=str)
parser.add_argument('-l', '--lines_count', type=str)
parser.add_argument('-w', '--words_count', type=str)

args = parser.parse_args()

if args.bytes_count != None:
    file_size = filesize_bytes(args.bytes_count)
    print(str(file_size) + ' ' + args.bytes_count)
elif args.lines_count != None:
    line_count = num_of_lines(args.lines_count)
    print(str(line_count) + ' ' + args.lines_count)
elif args.words_count != None:
    num_of_words = num_of_words(args.words_count)
    print(str(num_of_words) + ' ' + args.words_count)