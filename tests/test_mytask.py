import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'examples'))
from mytask import MyTask

class TestHelper(unittest.TestCase):
    def test_task(self):
        result = MyTask().task({'hello': 'world'})
        self.assertEqual(result, {'result': 'world'})
