import argparse 
import os
from functools import reduce

def filesize_bytes(file_path : str) -> int:
    return os.path.getsize(file_path)

def num_of_lines(file_path : str) -> int:
    with open(file_path) as file:
        num_of_lines = len(file.readlines())
    return num_of_lines

def num_of_words(file_path : str) -> int:
    with open(file_path) as file:
        words = file.read().split()
    return len(words)

# TODO: Test/capture all special characters
def count_characters(file_path : str) -> int:
    with open(file_path) as file:
        char_count = len(file.read())
    newline_count = num_of_lines(file_path)
    return char_count + newline_count

def nothing_flagged(args) -> bool:
    return not (args.bytes_count or args.lines_count or args.words_count or args.characters_count)
    

parser = argparse.ArgumentParser(prog='ccwc',
                                 description='Generate various statistics about a file')
parser.add_argument('-c', '--bytes_count', action='store_true')
parser.add_argument('-l', '--lines_count', action='store_true')
parser.add_argument('-w', '--words_count', action='store_true')
parser.add_argument('-m', '--characters_count', action='store_true')
parser.add_argument('filepath')

args = parser.parse_args()

if nothing_flagged(args):
    file_size = filesize_bytes(args.filepath)
    line_count = num_of_lines(args.filepath)
    word_count = num_of_words(args.filepath)
    print(str(line_count) + ' ' + str(word_count) + ' ' + str(file_size) + ' ' + args.filepath)
else:
    if args.bytes_count:
        file_size = filesize_bytes(args.filepath)
        print(str(file_size) + ' ' + args.filepath)
    if args.lines_count:
        line_count = num_of_lines(args.filepath)
        print(str(line_count) + ' ' + args.filepath)
    if args.words_count:
        word_count = num_of_words(args.filepath)
        print(str(word_count) + ' ' + args.filepath)
    if args.characters_count:
        character_count = count_characters(args.filepath)
        print(str(character_count) + ' ' + args.filepath)
