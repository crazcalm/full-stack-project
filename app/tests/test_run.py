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
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")

    def test_default(self):
        self.func(self.test_object)
        output = sys.stdout.getvalue().strip()
        self.assertIn("default", output)

    def test_dev_option(self):
        self.test_object.dev = True
        self.func(self.test_object)
        output = sys.stdout.getvalue().strip()
        self.assertIn("dev", output)

    def test_stage_option(self):
        self.test_object.stage = True
        self.func(self.test_object)
        output = sys.stdout.getvalue().strip()
        self.assertIn("stage", output)

    def tearDown(self):
        pass

    def testing(self):
        print("hello world")
        output = sys.stdout.getvalue().strip()
        self.assertIn("world", output)


if __name__ == '__main__':
    assert not hasattr(sys.stdout, "getvalue")
    unittest.main(module=__name__, buffer=True, exit=False)
