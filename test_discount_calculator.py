import unittest
from discount_calculator import calculate_discount

class TestDiscountCalculator(unittest.TestCase):
    def setUp(self):
        self.vol0 = 100
        self.vol1 = 500
        self.vol2 = 1000
        self.vol3 = 1200

    def test_calculator0(self):
        actualyResult = calculate_discount(self.vol0)
        expectedResult = 0.0
        self.assertEqual(actualyResult,expectedResult, "Failed for volume 100")
    
    def test_calculator1(self):
        actualyResult = calculate_discount(self.vol1)
        expectedResult = 0.05
        self.assertEqual(actualyResult,expectedResult, "Failed for volume 500")
    
    def test_calculator2(self):
        actualyResult = calculate_discount(self.vol2)
        expectedResult = 0.1
        self.assertEqual(actualyResult,expectedResult, "Failed for volume 1000")
    
    def test_calculator3(self):
        actualyResult = calculate_discount(self.vol3)
        expectedResult = 0.1
        self.assertEqual(actualyResult,expectedResult, "Failed for volume 1200")

    # def test_no_discount(self):
    #     self.assertEqual(calculate_discount(100), 0.0, "Failed for volume 100")

    # def test__five_discount(self):
    #     self.assertEqual(calculate_discount(500), 0.05, "Failed for volume 500")

    # def test_ten_discount(self):
    #     self.assertEqual(calculate_discount(1000), 0.1, "Failed for volume 1000")

    # def test_combined_discount(self):
    #     self.assertEqual(calculate_discount(1200), 0.1, "Failed for volume 1200")

if __name__ == '__main__':
    unittest.main()