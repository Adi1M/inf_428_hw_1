import unittest

from task_3 import time_diff


class TestTimeDiff(unittest.TestCase):
    def test_day_diff(self):
        self.assertEqual(time_diff(23, 1), 2)
        self.assertEqual(time_diff(1, 23), 22)

    def test_same_time(self):
        self.assertEqual(time_diff(5, 5), 0)


if __name__ == '__main__':
    unittest.main()
