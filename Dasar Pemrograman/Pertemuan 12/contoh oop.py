class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(5, 10)
segitiga2 = Segitiga(10, 10)

print("Luas Segitiga 1 : ", segitiga1.get_luas())
print("Luas Segitiga 2 :", segitiga2.get_luas())