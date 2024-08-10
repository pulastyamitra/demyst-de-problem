import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.file_spec import  read_file_spec


def generate_column_data(length :int) -> str:
    """
    Generate the sample data for the column based on the length.
    Parameters:
    length (int): The length of the column.
    Returns:
    str: The sample data for the column.
    """

    # num is just a dummy string with 10 characters.
    num :str = '123456789_'
    col_data = None

    if length < len(num):
        col_data = num[:length]
    else: #when length is greater than 10.
        col_data = num * (length // 10) + num[:length % 10]
        
    return col_data


def generate_data(spec_file_path :str, row_count : int, sample_file_name :str) -> int:
    """
    Generate the sample data based on the spec file.
    Parameters:
    spec_file_path (str): The path to the JSON spec file.
    row_count (int): The number of rows to generate.
    sample_file_name (str): The name of the sample file.
    Returns:
    int: The number of rows generated.
    """
    spec = read_file_spec(spec_file_path)
    column_names = spec["column_names"]
    offsets = list(map(int, spec["offsets"]))
    include_header = spec["include_header"]
    widt_encoding = spec["widt_encoding"]
    delimited_encoding = spec["delimited_encoding"]

    lines = []

    # Add header if required
    if include_header == 'true':
        header = ''.join([name.ljust(offset) for name, offset in zip(column_names, offsets)])
        lines.append(header)

    for _ in range(row_count):
        line = ''.join([generate_column_data(offset) for offset in offsets])
        lines.append(line)

    # Get the directory one level above the current script
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(parent_dir, 'data')

    # Ensure the directory exists
    os.makedirs(data_dir, exist_ok=True)

    # Write to file
    file_path = os.path.join(data_dir, sample_file_name)
    
    with open(file_path, 'w', encoding=widt_encoding) as file:
        for line in lines:
            file.write(line + '\n')

    # if include_header == 'true': then retrun row_count +1 else row_count
    return row_count + 1 if include_header == 'true' else row_count
