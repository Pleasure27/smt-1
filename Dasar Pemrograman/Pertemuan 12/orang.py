class Orang:
    def __init__(self, nama,  asal):
        self.nama = nama
        self.asal = asal
    
    def perkenalan(self):
        print(f"Perkenalkan Nama Saya {self.nama} dari {self.asal}")