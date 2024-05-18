from orang import Orang

class pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah

Adnan = pelajar('Adnan', 'Bekasi', 'SMA 1 Tambun Selatan')
Adnan.perkenalan()
print("Saya Sekolah di", Adnan.sekolah)