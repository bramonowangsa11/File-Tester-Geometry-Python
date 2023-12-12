import unittest
from array_operations import find_max_value

class TestArrayOperations(unittest.TestCase):
    def setUp(self):
        self.arr = [7,2,11,6,20]
        self.arrIsEmpty = []
    
    def testArray(self):
        actualyResult = find_max_value(self.arr)
        expectedResult = 20
        self.assertEqual(actualyResult,expectedResult)
    def testArrayIsEmpty(self):
        actualyResult = find_max_value(self.arrIsEmpty)
        expectedResult = None
        self.assertEqual(actualyResult,expectedResult)

if __name__ == '__main__':
    unittest.main()