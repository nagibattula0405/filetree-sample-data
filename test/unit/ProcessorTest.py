import os
import unittest

import Processor


class ProcessorTest(unittest.TestCase):

    def test_successful_input_file_process(self, resource_path=os.getcwd().replace("unit", "resources")):
        exit_code = Processor.__execute__(resource_path + "/input_success.json", resource_path + "/output_success.json")
        # Can extend furthermore by asserting actual file content
        self.assertNotEqual(os.stat(resource_path + "/output_success.json"), 0)
        self.assertEqual(exit_code, 0)

    def test_failure_input_file_process(self, resource_path=os.getcwd().replace("unit", "resources")):
        exit_code = Processor.__execute__(resource_path + "/input_failure.json", resource_path + "/output.json")
        self.assertEqual(exit_code, 1)

    def test_partial_input_file_process(self, resource_path=os.getcwd().replace("unit", "resources")):
        exit_code = Processor.__execute__(resource_path + "/input_partial.json", resource_path + "/output_partial.json")
        self.assertNotEqual(os.stat(resource_path + "/output_partial.json"), 0)
        self.assertEqual(exit_code, 3)

    def test_empty_object_keys_input_file_process(self, resource_path=os.getcwd().replace("unit", "resources")):
        exit_code = Processor.__execute__(resource_path + "/input_empty.json", resource_path + "/output.json")
        self.assertEqual(exit_code, 4)

    def test_corrupt_input_file_process(self, resource_path=os.getcwd().replace("unit", "resources")):
        exit_code = Processor.__execute__(resource_path + "/input_corrupt.json", resource_path + "/output.json")
        self.assertEqual(exit_code, 1)
