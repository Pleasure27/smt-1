import pandas as tg
from datetime import datetime, timedelta

kode_studio = []
jenis_studio = []
hrg_studio = []
nama_pemesan = []
jumhar = []
jumbay = 0

print("------------------------------------------------------")
print("Pemesanan Tiket Bioskop Nussa")
tgl_pemesan = datetime.now()
print("Tanggal Pemesanan : ", tgl_pemesan)
nama_pemesan.append(input("Masukkan Nama Pemesan :"))
data = int(input("Masukkan Jumlah Transaksi : "))


for i in range(data):
    print("\nTransaksi ke -" + str(i+1))
    kode_studio = int(input("Masukkan Kode Studio [1/2/3]: "))
    jmlh_tiket = int(input("Masukkan Jumlah Tiket: "))
    if kode_studio == 1:
        jenis_studio.append("Regular")
        hrg_studio.append(35000)
    elif kode_studio == 2:
        jenis_studio.append("VIP")
        hrg_studio.append(45000)
    elif kode_studio == 3:
        jenis_studio.append("Ekslusif")
        hrg_studio.append(55000)
    else:
        jenis_studio.append("Salah Kode")
        hrg_studio.append(0)
    print("------------------------------------------------------")
    
for i in range(data):
    jumhar.append(hrg_studio[i]*jmlh_tiket)
    jumbay = jumhar[i]
    pajak = 0.10 * jumbay
    tobay = pajak + jumbay
    
for i in range(data):
    transaksi = {
        "Kode Studio" : kode_studio,
        "Jenis Studio" : jenis_studio,
        "Jumlah Tiket" : jmlh_tiket,
        "Harga" : hrg_studio,
        "Subtotal" : jumhar,
    }

data_transaksi = tg.DataFrame(transaksi)
data_pembelian = tg.DataFrame

print("Tanggal Pemesanan : ", tgl_pemesan)
print("=========== DATA PEMESANAN TIKET BIOSKOP NUSSA ===========")
print(data_transaksi)
print("----------------------------------------------------------")
print("Total : Rp.", jumbay)
print("Pajak : Rp.", pajak)
print("Total Keseluruhan : Rp.", int(tobay))
uang_bayar = int(input("Uang Bayar : Rp."))
uang_kembali = uang_bayar - tobay
print("Uang Kembali : Rp.", int(uang_kembali))
print("==========================================================")
