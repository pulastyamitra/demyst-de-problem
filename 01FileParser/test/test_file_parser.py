import os
import sys
import unittest
# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.generate_data import generate_data
from util.file_parser import fixed_width_parser

class TestFileParser(unittest.TestCase):
    def setUp(self):
        self.spec_file_name = 'spec.json'
        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.data_dir = os.path.join(self.parent_dir, 'data')
        self.sample_file_name = 'test_sample_parser_file.txt'
        self.sample_file_path = os.path.join(self.data_dir, self.sample_file_name)
        self.output_file_name = 'test_output_parser_file.csv'
        self.output_file_path = os.path.join(self.data_dir, self.output_file_name)
        print(self.sample_file_path)

    def tearDown(self):
        # Clean up any files created during the tests
        if os.path.exists(self.sample_file_path):
            os.remove(self.sample_file_path)
        if os.path.exists(self.output_file_path):
            os.remove(self.output_file_path)

    def test_fixed_width_parser(self):
        row_count = 0
        row_count = generate_data(self.spec_file_name, 100000,self.sample_file_name)
        fixed_width_parser(self.spec_file_name, self.sample_file_path, self.output_file_path)
        self.assertTrue(os.path.exists(self.output_file_path))

        # Check the number of rows in the output file
        with open(self.output_file_path, 'r') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), row_count)

if __name__ == '__main__':
    unittest.main()