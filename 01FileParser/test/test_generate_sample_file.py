import os
import sys
import unittest
# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.generate_data import generate_data

class TestGenerateSampleFile(unittest.TestCase):

    def setUp(self):
        self.spec_file_name = 'spec.json'
        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.data_dir = os.path.join(self.parent_dir, 'data')
        self.sample_file_name = 'sample_parser_file.txt'
        self.sample_file_name_2 = 'sample_parser_file_2.txt'
        self.sample_file_path = os.path.join(self.data_dir, self.sample_file_name)
        self.sample_file_path_2 = os.path.join(self.data_dir, self.sample_file_name_2)
        #print(self.sample_file_path)

    def tearDown(self):
        # Clean up any files created during the tests
        if os.path.exists(self.sample_file_path):
            os.remove(self.sample_file_path)
        if os.path.exists(self.sample_file_path_2):
            os.remove(self.sample_file_path_2)


    def test_generate_sample_file(self):
        generate_data(self.spec_file_name, 1000,self.sample_file_name)
        self.assertTrue(os.path.exists(self.sample_file_path))

    def test_generate_sample_file_with_different_file_name(self):
        generate_data(self.spec_file_name, 1000, self.sample_file_path_2)
        self.assertTrue(os.path.exists(self.sample_file_path_2))

    def test_generate_sample_file_with_different_size(self):
        row_count =0
        row_count = generate_data(self.spec_file_name, 500,self.sample_file_name)
        self.assertTrue(os.path.exists(self.sample_file_path))
        with open(self.sample_file_path, 'r') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), row_count)

    def test_generate_sample_file_zero_size(self):
        row_count =0
        row_count = generate_data(self.spec_file_name, 0,self.sample_file_name)
        self.assertTrue(os.path.exists(self.sample_file_path))
        with open(self.sample_file_path, 'r') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), row_count)

if __name__ == '__main__':
    unittest.main()