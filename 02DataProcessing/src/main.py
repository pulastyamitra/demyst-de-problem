import argparse
import os
import sys
# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import data_anonymiser 

def main():
    arg_parser = argparse.ArgumentParser(description ='Process csv file to anonumise the data.')
    arg_parser.add_argument('input_filename', type=str, help='The name of the csv input file with path')
    arg_parser.add_argument('output_file', type=str, help='The name of the output file with path')
    args = arg_parser.parse_args()

    data_anonymiser.anonymise_data (args.input_filename, args.output_file)

if __name__ == '__main__':
    main()
