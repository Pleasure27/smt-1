class Kendaraan:
    def berjalan(self):
        print('Berjalan..')
        
class Mobil(Kendaraan):
    def berjalan(self):
        print("Berjalan Lebih Cepat..")
        
sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan()