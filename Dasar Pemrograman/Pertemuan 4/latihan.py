nama = str(input("Masukkan Nama :"))
nis = int(input("Masukkan NIS :"))
kode_jurusan = str(input("Masukkan Kode Jurusan [SI/SIA] :"))

if kode_jurusan == "SI" or kode_jurusan == "si":
    nama_prodi = "Sistem Informasi"
    harga = 2400000
elif kode_jurusan == "SIA" or kode_jurusan == "sia":
    nama_prodi = "Sistem Informasi Akuntansi"
    harga = 2000000
else:
    nama_prodi = "Kode Jurusan Salah"
    harga = 0
print("================================")
print("===PENDAFTARAN MAHASISWA BARU====")
print("---------------------------------")
print("Nama : ", nama)
print("NIS : ", nis)
print("=================================")
print("Nama Prodi : ", nama_prodi)
print("Harga : ", harga)
print("=================================")