import unittest
import os
import sys

# Adds the src dir to path so that I can import my files with reference to src
sys.path.insert(0, os.path.abspath('..'))

from run import set_config

"""
To test this, I need to both mock the app.config.from_object call and
check the capture the stdout in a buffer so that I can check the text.

OR,

I can create a fake app class here and do the buffer stuff tonight...

"""


class TestConfig:
    def __init__(self):
        self.name = "Used me for testing only!"

    def from_object(self, object):
        # I should check the class type and return an answer here!!!!
        pass


class TestApp:
    def __init__(self):
        self.dev = False
        self.stage = False
        self.prod = False
        self.config = TestConfig()


class TestRun(unittest.TestCase):  # Still need to add the logig for the tests
    def setUp(self):
        self.func = set_config
        self.test_object = TestApp()
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
