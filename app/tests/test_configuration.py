import unittest
import os
import sys

# Adds the src dir to path so that I can import my files with reference to src
sys.path.insert(0, os.path.abspath('..'))

from configuration import BaseConfig
from configuration import ProductionConfig
from configuration import StagingConfig
from configuration import DevelopmentConfig

"""
I need to ensure that each configuration has a number
of properties set!

Currently, I just need to check:

- SECRET_KEY
- DEBUG
- TESTING
- NEW_CONFIG_VARIABLE

"""


class TestBaseConfig(unittest.TestCase):
    def setUp(self):
        self.config = BaseConfig()

    def tearDown(self):
        pass

    def basics_attrs(self):
        return ["SECRET_KEY", "DEBUG", "TESTING"]

    def test_basic_option(self):
        self.assertIsNotNone(self.config.TESTING)
        self.assertIsNotNone(self.config.DEBUG)
        self.assertIsNotNone(self.config.SECRET_KEY)


class TestDevelopmentConfig(TestBaseConfig):
    def setUp(self):
        self.config = DevelopmentConfig()


class TestStagingConfig(TestBaseConfig):
    def setup(self):
        self.config = StagingConfig()


class TestProductionConfig(TestBaseConfig):
    def setUp(self):
        self.config = ProductionConfig

if __name__ == '__main__':
    unittest.main()
