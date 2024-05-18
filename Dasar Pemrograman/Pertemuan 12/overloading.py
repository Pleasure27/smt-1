class Kendaraan:
    def berjalan(self):
        print("Berjalan..")
        
class Mobil(Kendaraan):
    def berjalan(self, kecepatan, satuan = "KM/J"):
        print(f"Berjalan dengan kecepatan {kecepatan} {satuan}")

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan(150)