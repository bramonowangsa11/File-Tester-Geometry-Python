

class GeometryCalculator:
    def luas_segitiga(alas,tinggi):
        return 0.5 * alas * tinggi
    
    def luas_persegi(sisi):
        return sisi*sisi
    
    def diameter_lingkaran(self,jari_jari):
        return 2 * jari_jari

    def luas_lingkaran(self, jari_jari):
        diameter = self.diameter_lingkaran(jari_jari)
        return (1/4) * 3.14159265359 * (diameter * diameter)
    
    def luas_persegi_panjang(panjang,lebar):
        return panjang*lebar
print(GeometryCalculator.luas_segitiga(5,7))
print(GeometryCalculator.luas_persegi(5))
# print(GeometryCalculator.luas_lingkaran(7))
print(GeometryCalculator.luas_persegi_panjang(4,5))