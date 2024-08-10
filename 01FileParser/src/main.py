import argparse
import os
import sys
# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import generate_data, file_spec , file_parser

def main():
    arg_parser = argparse.ArgumentParser(description ='Process fixed width file.')
    arg_parser.add_argument('spec_file', type=str, help='The name of the spec file with path')
    arg_parser.add_argument('input_filename', type=str, help='The name of the input fixed-width text file with path')
    arg_parser.add_argument('output_file', type=str, help='The name of the output CSV file with path')
    args = arg_parser.parse_args()

    file_parser.fixed_width_parser(args.spec_file, args.input_filename, args.output_file)

if __name__ == '__main__':
    main()

#python main.py spec_file input_file output_file
