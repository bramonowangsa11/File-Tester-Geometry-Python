

class GeometryCalculator:
    def luas_segitiga(alas,tinggi):
        return 0.5 * alas * tinggi
    
    def luas_persegi(sisi):
        return sisi*sisi
    
    def luas_lingkaran(jari):
        return 3.14 * jari * jari
    def luas_persegi_panjang(panjang,lebar):
        return panjang*lebar
print(GeometryCalculator.luas_segitiga(5,7))
print(GeometryCalculator.luas_persegi(5))
print(GeometryCalculator.luas_lingkaran(7))
print(GeometryCalculator.luas_persegi_panjang(4,5))