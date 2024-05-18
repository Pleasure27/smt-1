nama_karyawan = str(input("Masukkan Nama Anda : "))
gaji = 300000

golongan = input("Masukkan Golongan Jabatan [1/2/3] : ")
if golongan == "1":
    tun_jabatan = gaji * 5/100
elif golongan == "2":
    tun_jabatan = gaji * 10/100
elif golongan == "3":
    tun_jabatan = gaji * 15/100
else:
    tun_jabatan = 0

pendidikan = str(input("Masukkan Jenjang Pendidikan [SMA/D1/D3/S1] : "))
if pendidikan == "SMA" or pendidikan == "sma":
    tun_pendidikan = gaji * 2.5/100
elif pendidikan == "D1" or pendidikan == "d1":
    tun_pendidikan = gaji * 5/100
elif pendidikan == "D3" or pendidikan == "d3":
    tun_pendidikan = gaji * 20/100
elif pendidikan == "S1" or pendidikan == "s1":
    tun_pendidikan = gaji * 30/100
else:
    tun_pendidikan = "Anda Belum Memasukkan Pendidikan"

jumlah_jam = int(input("Masukkan Jumlah Jam Kerja :  "))

if jumlah_jam > 8 :
    honor = (jumlah_jam - 8) * 3500
else:
    honor =  0

total_tunjangan = int(tun_jabatan) + int(tun_pendidikan)
total_gaji = gaji + total_tunjangan + honor

print(" ")
print("====================/ GAJI KARYAWAN \========================")
print("=============================================================")
print("Karyawan yang bernama", nama_karyawan)
print("Honor yang diterima")
print("   ", "Gaji Pokok            :   Rp.", +int(gaji))
print("   ", "Tunjangan Jabatan     :   Rp.", +int(tun_jabatan))
print("   ", "Tunjangan Pendidikan  :   Rp.", +int(tun_pendidikan))
print("   ", "Honor Lembur          :   Rp.", honor)
print(" ")
print("                            ______________ +")
print("   ", "Total Gaji                Rp.", total_gaji)
print("--------------------------------------------------------------")

#Nama   : Muhammad Nasal Ekaputra
#NIM    : 17230564
#Kelas  : 17.1A.04
