import unittest
import os
import sys

# Adds the src dir to path so that I can import my files with reference to src
sys.path.insert(0, os.path.abspath('..'))

from app import app


class Testing(unittest.TestCase):
    def setUp(self):
        app.testing = True
        #self.app = app
        self.app = app.app.test_client(self)

    def tearDown(self):
        pass

    def test_home(self):
        rv = self.app.get("/")
        self.assertEqual(rv.status_code, 200)

    def testing(self):
        self.assertEqual(2, 1 + 1, "Testing")


if __name__ == '__main__':
    unittest.main()
