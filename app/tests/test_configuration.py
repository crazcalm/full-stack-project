import unittest
import os
import sys

# Adds the src dir to path so that I can import my files with reference to src
sys.path.insert(0, os.path.abspath('..'))


class Testing(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testing(self):
        self.assertEqual(2, 1 + 1, "Testing")


if __name__ == '__main__':
    unittest.main()