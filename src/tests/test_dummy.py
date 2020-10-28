import unittest
from main import dummy

class TestMain(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(dummy('VOID'), 'VOID')