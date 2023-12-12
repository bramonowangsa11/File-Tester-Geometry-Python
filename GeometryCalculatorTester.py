import unittest
from geometry_calculator import GeometryCalculator

class GeometryCalculatorTester(unittest.TestCase):

    #arrange
    def setUp(self):
        self.alas = 5
        self.tinggi = 7
        self.sisi = 5
        self.jari = 7
        self.panjang = 4
        self.lebar = 5

    def test_luas_segitiga(self):
        #act
        actualyResult = GeometryCalculator.luas_segitiga(self.alas, self.tinggi)

        #assert
        expectedResult = 0.5 * self.alas * self.tinggi
        self.assertEqual(actualyResult,expectedResult)

    def test_luas_persegi(self):
        #act
        actualyResult = GeometryCalculator.luas_persegi(self.sisi)

        #assert
        expectedResult = self.sisi*self.sisi
        self.assertEqual(actualyResult,expectedResult)

    def test_luas_lingkaran(self):
        #act
        actualyResult = GeometryCalculator.luas_lingkaran(self.jari)

        #assert
        expectedResult = 3.14 * self.jari * self.jari
        self.assertEqual(actualyResult,expectedResult)
    def test_luas_persegi_panjang(self):
        #act
        actualyResult = GeometryCalculator.luas_persegi_panjang(self.panjang, self.lebar)

        #assert
        expectedResult = self.panjang * self.lebar
        self.assertEqual(actualyResult,expectedResult)

unittest.main()