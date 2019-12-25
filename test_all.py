from main import check
import unittest

class TestAOC2019_04(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(check("112233"))
        self.assertFalse(check("123444"))
        self.assertTrue(check("111122"))

if __name__ == '__main__':
    unittest.main()
