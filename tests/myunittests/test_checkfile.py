import os
from unittest import TestCase

from tests.myfuncs import checkfile


class TestCheckFile(TestCase):

    def setUp(self):
        with open('testfile.txt', 'w') as f:
            f.write('first line')

    def tearDown(self):
        if os.path.exists('testfile.txt'):
            os.remove('testfile.txt')

    def test_existent(self):
        self.assertTrue(checkfile('testfile.txt'))

    def test_nonexistent(self):
        self.assertFalse(checkfile('testfile123.txt'))
