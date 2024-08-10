import csv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.file_spec import  read_file_spec

def fixed_width_parser(spec_file_path: str, input_filename: str, output_filename: str):
    """
    Read the json spec file for the specification.
    Parse the fixed-width file and write the data into a CSV

    Parameters:
    spec (str): file name with path.
    input_filename (str): The name of the input fixed-width text file.
    output_filename (str): The name of the output CSV file.
    """

    spec = read_file_spec(spec_file_path)
    column_names = spec["column_names"]
    offsets = list(map(int, spec["offsets"]))
    include_header = spec["include_header"]
    widt_encoding = spec["widt_encoding"]
    delimited_encoding = spec["delimited_encoding"]

    #print(f"spec_file_path = {spec_file_path}")
    #print(f"input_filename = {input_filename}")
    #print(f"output_filename = {output_filename}")

    try:
        with open(input_filename, 'r') as in_file, open(output_filename, 'w', newline='', encoding=delimited_encoding) as out_file:

            reader = in_file.readlines()
            writer = csv.writer(out_file)

            if include_header == 'true':
                writer.writerow(column_names)
                #remove the header from the reader
                reader = reader[1:]            

            for line in reader:
                row = []
                start = 0
                for col_length in offsets:
                    row.append(line[start:start + col_length].strip())
                    start += col_length
                writer.writerow(row)

    except Exception as e:
        #print(e)
        raise Exception("Could not process input file!")
    
    return True