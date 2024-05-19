import os
import unittest

import Validator


class ValidatorTest(unittest.TestCase):
    def test_input_file_not_found_case(self, resource_path=os.getcwd().replace("unit", "resources")):
        is_found = Validator.validate_input_file_path(resource_path + "/dummy.json")
        self.assertEqual(is_found, False)

    def test_input_file_not_having_json_extension(self, resource_path=os.getcwd().replace("unit", "resources")):
        is_json = Validator.validate_input_file_path(resource_path + "/input.txt")
        self.assertEqual(is_json, False)

    def test_no_content_input_file(self, resource_path=os.getcwd().replace("unit", "resources")):
        is_empty = Validator.empty_input_file(resource_path + "/input_no_content.json")
        self.assertEqual(is_empty, True)

    def test_output_file_not_found_case(self, resource_path=os.getcwd().replace("unit", "resources")):
        is_found = Validator.validate_output_file_path(resource_path + "/dummy.json")
        self.assertEqual(is_found, False)

    def test_output_file_not_having_json_extension(self, resource_path=os.getcwd().replace("unit", "resources")):
        is_json = Validator.validate_output_file_path(resource_path + "/output.txt")
        self.assertEqual(is_json, False)
