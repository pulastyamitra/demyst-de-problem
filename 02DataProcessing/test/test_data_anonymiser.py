import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.data_anonymiser import extract_client_machine_info, hash_column, anonymise_data

import pandas as pd
import dask.dataframe as dd
import hashlib

class TestDataAnonymiser(unittest.TestCase):

    def test_extract_client_machine_info(self):
        client_info = "Client: processes=4 threads=8 memory=16.0 GiB"
        processes, threads, memory_limit = extract_client_machine_info(client_info)
        self.assertEqual(processes, 4)
        self.assertEqual(threads, 8)
        self.assertEqual(memory_limit, 16.0)

    def test_hash_column(self):
        original_string = "test_string"
        hashed_string = hash_column(original_string)
        expected_hashed_string = hashlib.sha256(original_string.encode('utf-8')).hexdigest()
        self.assertEqual(hashed_string, expected_hashed_string)

    def test_anonymise_data(self):
        input_file = 'test_input.csv'
        output_file = 'test_output.parquet'
        
        # Create a sample CSV file
        df = pd.DataFrame({
            'first_name': ['John', 'Jane'],
            'last_name': ['Doe', 'Smith'],
            'address': ['123 Elm St', '456 Oak St']
        })
        df.to_csv(input_file, index=False)
        
        # Run the anonymise_data function
        anonymise_data(input_file, output_file)
        
        # Read the output Parquet file
        df_anonymised = dd.read_parquet(output_file).compute()
        
        # Check if the columns are hashed
        for col in ['first_name', 'last_name', 'address']:
            for original_value in df[col]:
                hashed_value = hash_column(original_value)
                self.assertIn(hashed_value, df_anonymised[col].values)
        
        
        # Clean up
        os.remove(input_file)
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()

