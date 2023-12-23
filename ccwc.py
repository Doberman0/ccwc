import argparse 
import os

def filesize_bytes(file_path : str) -> int:
    return os.path.getsize(file_path)

parser = argparse.ArgumentParser(prog='ccwc',
                                 description='Generate various statistics about a file')
parser.add_argument('-c', '--bytes_count', type=str)

args = parser.parse_args()

if args.bytes_count != None:
    file_size = filesize_bytes(args.bytes_count)
    print(str(file_size) + ' ' + args.bytes_count)
