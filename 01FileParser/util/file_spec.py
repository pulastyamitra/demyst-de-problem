import json

# Function to read the file spec as JSON file.

def read_file_spec(file_path :str) -> dict:
    """
    Read the file spec as JSON file.
    Parameters:
    file_path (str): The path to the JSON file.
    Returns:
    dict: The file spec details.
    """
    
    try:
        # Read the JSON spec file
        with open(file_path, 'r') as file:
            spec_str = file.read()
        # Parse the JSON spec file
        spec = json.loads(spec_str)
        # Extract the file spec        
        column_names = spec["ColumnNames"]
        offsets = list(map(int, spec["Offsets"]))
        include_header = spec["IncludeHeader"].lower() 
        widt_encoding = spec["FixedWidthEncoding"]
        delimited_encoding = spec["DelimitedEncoding"]
        spec_details :dict = {
            "column_names": column_names,
            "offsets": offsets,
            "include_header": include_header,
            "widt_encoding": widt_encoding,
            "delimited_encoding": delimited_encoding
        }
    except KeyError as e:
        print(f"Error: {e}")
        print("Please check that the JSON spec file contains the required fields.")
        raise

    return spec_details