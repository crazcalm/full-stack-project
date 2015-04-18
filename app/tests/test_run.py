import unittest
import os
import sys

# Adds the src dir to path so that I can import my files with reference to src
sys.path.insert(0, os.path.abspath('..'))

from run import set_config


class TestRun(unittest.TestCase):
    def setUp(self):
        self.func = set_config
        self.options = {
            "dev": "dev",
            "prod": "prod",
            "stage": "stage"
        }

    def test_default(self):
        pass

    def test_dev_option(self):
        pass

    def test_stage_option(self):
        pass

    def tearDown(self):
        pass

    def testing(self):
        self.assertEqual(2, 1 + 1, "Testing")


if __name__ == '__main__':
    unittest.main()
