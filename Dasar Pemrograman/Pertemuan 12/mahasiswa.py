class Mahasiswa_UBSI:
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk
    
    def perkenalan(self):
        print("Nama : ", self.nama)
        print("Jurusan : ", self.jurusan)
        print("IPK : ", self.ipk)
        print()
        
        
mahasiswa1 = Mahasiswa_UBSI("Mely", "Sistem Informasi", 3.75)
mahasiswa2 = Mahasiswa_UBSI("Adnan", "Teknik Komputer", 4.00)
mahasiswa3 = Mahasiswa_UBSI("Nasal", "Teknologi Informasi", 4.00)

mahasiswa1.perkenalan()
mahasiswa2.perkenalan()
mahasiswa3.perkenalan()