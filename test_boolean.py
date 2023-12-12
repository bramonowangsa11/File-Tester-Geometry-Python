import unittest
from boolean import isEven

class testBoolean(unittest.TestCase):
    def setUp(self):
        self.numbers = 4
        self.numberIsNotEven = 3

    def test_evenTrue(self):
        actualyResult = isEven(self.numbers)
        expectedResult = True
        self.assertTrue(actualyResult,expectedResult)

    def test_evenFalse(self):
        actualyResult = isEven(self.numberIsNotEven)
        expectedResult = False
        self.assertFalse(actualyResult,expectedResult)

if __name__ == '__main__':
    unittest.main()