import datetime
from datetime import timedelta
from os import path

pilihan = 0
keluar = False
sudah_login = False

index = -1

pelanggan = [
    {
        "nama":[],
        "email":[],
        "password":[],
        "saldo":[],
        "failed_login":0,
        "transaksi":[]
    },
    {
        "nama":[],
        "email":[],
        "password":[],
        "saldo":[],
        "failed_login":0,
        "transaksi":[]
    }
]

barang = [
    {
        "nama":[],
        "harga":[],
        "kategori":[],
        "merk":[],
        "deskripsi":[]
    },
]

voucher = [
    {
        "kode":[],
        "kategori":[],
        "merk":[],
        "dipakai":[],
        "diskon":[],
        "expired":[],
    },
]

batas_pembayaran_transaksi = 5

def cekPelanggan(email,password):
    i = 0
    for pl in pelanggan:
        if (str(pl['email']) == email and str(pl['password']) == password):
            return i
        i+=1
    return "Tidak Ada"
print(len(pelanggan))
while keluar == False:
    if sudah_login == False:
        print("====== SELAMAT DATANG DI MEGATEC COMPUTER =======")
        print("1. Login")
        print("2. Belum punya akun? Daftar Sekarang!")
        print("3. Keluar")
        pilihan = int(input("Masukkan Pilihan Anda : "))
        if pilihan == 1:
            email = str(input("Masukkan Email : "))
            password = str(input("Masukkan Password : "))
            cek = cekPelanggan(email, password)
            if cek == "Tidak Ada":
                print("Email atau Password anda salah")
                sudah_login = False
            else:
                sudah_login = True
                index = cek
        elif pilihan == 2:
            if path.isfile('pelanggan.txt'):
                with open('pelanggan.txt', 'r') as file:
                    pelanggan = file.read().split('\n')
            else:
                pelanggan = []
                while True:
                    email = input('Masukkan Email : ')
                    password = input('Masukkan Password: ')
                    break
                    pelanggan.append(email)
                    pelanggan.append(password)
                with open('pelanggan.txt', 'w') as file:
                    file.write('\n'.join(pelanggan))