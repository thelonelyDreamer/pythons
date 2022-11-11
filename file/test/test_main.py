import unittest
import draft as d


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = d.sum2str("a","b")
        self.assertEqual(result, "ab")  # add assertion here


if __name__ == '__main__':
    unittest.main()
