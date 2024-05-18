import time
import datetime
from datetime import timedelta

pilihan = 0
mbanking_id = 0
keluar = False
sudah_login = False

index = -1

pelanggan = [
    {
        "nama":"Muhammad Nasal Ekaputra",
        "id_user":"2712",
        "email":"nep@gmail.com",
        "password":"nep321",
        "saldo_pl":0,
        "failed_login":0,
        "transaksi":[]
    },
]

mbanking = [
    {   
        "id":"1234",
        "no_rekening":"12344321",
        "username":"Nasal",
        "pin":"2712",
        "saldo":50000000
    },
]

barang = [
    {
        "nama":"Intel Core i3 6100",
        "harga":935000,
        "kategori":"Processor",
        "type":"Sky Lake",
        "merk":"Intel",
        "deskripsi":"\nJumlah Core : 2\nJumlah Threads : 4\nFrekuensi Clock : 3.70Ghz\nTDP : 51W\nJenis Memori : DDR4-1866/2133\nGrafis Processor : Intel HD Graphics 530\nSocket : LGA 1151",
    },
    {
        "nama":"Intel Core i5 11400F",
        "harga":1970000,
        "kategori":"Processor",
        "type":"Rocket Lake",
        "merk":"Intel",
        "deskripsi":"\nJumlah Core : 6\nJumlah Threads : 12\nFrekuensi Clock : 4.40Ghz\nJumlah Cache : 12MB Intel Smart Cache\nTDP : 65 W\nJenis Memori : DDR4-3200\nGrafis Processor : -\nSocket : LGA 1200",
    },
    {
        "nama":"Intel Core i9 13900K",
        "harga":10600000,
        "kategori":"Processor",
        "type":"Raptor Lake",
        "merk":"Intel",
        "deskripsi":"\nJumlah Core : 24\nJumlah Threads : 32\nFrekuensi Clock : 5.80Ghz\nJumlah Cache : 36MB Intel Smart Cache\nTDP : 120 W\nJenis Memori : DDR4-3200 & DDR5-5600\nGrafis Processor : Intel UHD Graphics 770\nSocket : LGA 1700",
    },
    { 
        "nama":"AMD Ryzen 3 5300G",
        "harga":3950000,
        "kategori":"Processor",
        "type":"Ryzen",
        "merk":"AMD",
        "deskripsi":"\nJumlah Core : 4\nJumlah Threads : 8\nFrekuensi Clock : 4.20Ghz\nJumlah Cache : 8MB\nTDP : 65 W\nJenis Memori : DDR4-3200\nGrafis Processor : AMD Radeon Rx Vega 6\nSocket : AM4",
    },
    { 
        "nama":"AMD Ryzen 5 7600X",
        "harga":6500000,
        "kategori":"Processor",
        "type":"Ryzen",
        "merk":"AMD",
        "deskripsi":"\nJumlah Core : 6\nJumlah Threads : 12\nFrekuensi Clock : 4.70GHz up to 5.30GHz\nJumlah Cache : 32MB\nTDP : 105 W\nJenis Memori : DDR5-5200\nGrafis Processor : AMD Radeon Graphics\nSocket : AM5",
    },
    { 
        "nama":"AMD Ryzen Threadripper 3990X",
        "harga":65000000,
        "kategori":"Processor",
        "type":"Ryzen",
        "merk":"AMD",
        "deskripsi":"\nJumlah Core : 64\nJumlah Threads : 128\nFrekuensi Clock : 2.90GHz up to 4.30Ghz\nJumlah Cache : 256MB\nTDP : 280 W\nJenis Memori : DDR4-3200\nGrafis Processor : -\nSocket : TRX4",
    },
    {
        "nama":"MSI GTX 1660 Super Gaming X",
        "harga":1750000,
        "kategori":"VGA Card",
        "type":"GTX",
        "merk":"MSI",
        "deskripsi":"\nMemory Size : 6GB\nMemory Tipe : GDDR6\nCore Speed : 1.830MHz\nMemory Speed : 14.000MHz\nInterface : PCIE 3.0 x16\nL1 % L2 Cache : 64KB & 1536MHz\nTDP : 125 W\nOutput : 1x HDMI 2.0b, 3x Display Port 1.4",
    },
    {
        "nama":"Nvidia RTX 3090 Founders Edition",
        "harga":30600000,
        "kategori":"VGA Card",
        "type":"RTX",
        "merk":"Nvidia",
        "deskripsi":"\nMemory Size : 24GB\nMemory Tipe : GDDR6X\nCore Speed : 1.400MHz\nMemory Speed : 19.500MHz\nInterface : PCIE 4.0 x16\nL1 % L2 Cache : 128KB & 6MB\nTDP : 350 W\nOutput : 1x HDMI 2.1, 3x Display Port 1.4a",
    },
    {
        "nama":"AMD Radeon RX 580",
        "harga":1250000,
        "kategori":"VGA Card",
        "type":"Radeon",
        "merk":"AMD",
        "deskripsi":"\nMemory Size : 8GB\nMemory Tipe : GDDR5\nCore Speed : 1.257MHz\nMemory Speed : 2.000MHz\nInterface : PCIE 3.0 x16\nL1 % L2 Cache : 12KB & 2MB\nTDP : 185 W\nOutput : 1x HDMI 2.0b, 3x Display Port 1.4a",
    },
    {
        "nama":"AMD Radeon RX 7900 XTX",
        "harga":25500000,
        "kategori":"VGA Card",
        "type":"Radeon",
        "merk":"AMD",
        "deskripsi":"\nMemory Size : 24GB\nMemory Tipe : GDDR6\nCore Speed : 2.000MHz\nMemory Speed : 20.000MHz\nInterface : PCIE 4.0 x16\nL1 % L2 Cache : 256KB & 6MB\nTDP : 355 W\nOutput : 1x HDMI 2.1a, 2x Display Port 2.1, 1x USB Type-C",
    },
    {
        "nama":"MSI B450M Pro VDH MAX",
        "harga":1070000,
        "kategori":"Motherboard",
        "type":"B450M",
        "merk":"MSI",
        "deskripsi":"\nSocket : AM4\nMemory : 4 x DDR4 DIMM\nMaximum Memory : 64GB\nInterface : 1x PCIE 3.0 x16, 2x PCIE 2.0 x1\nStorage : 4x SATA 6Gb/s, 1x M.2 Slot\nAudio Chipset : Realtek ALC892\nPorts : VGA Port, USB 2.0, USB 3.2 Gen1, LAN Port, HD Audio Connectors, HDMI Port, DVI-D Port",
    },
    {
        "nama":"Asrock B660M PRO RS",
        "harga":2300000,
        "kategori":"Motherboard",
        "type":"B660M",
        "merk":"Asrock",
        "deskripsi":"\nSocket : LGA1700\nMemory : 4 x DDR4 DIMM\nMaximum Memory : 128GB\nInterface : 1x PCIE 4.0 x16, 1x PCIE 3.0 x16,1x PCIE 3.0 x1\nStorage : 4x SATA3 6Gb/s, 1x Hyper M.2 Slot, 1x Ultra M.2 Slot\nAudio Chipset : Realtek ALC897\nPorts : HDMI Port, 2x USB 2.0, 4x USB 3.2 Gen1, DisplayPort 1.4, HD Audio Jacks",
    },
    {
        "nama":"Corsair Vengeance RGB RS 16GB DDR4-3200MHz",
        "harga":1030000,
        "kategori":"RAM",
        "type":"DDR4",
        "merk":"Corsair",
        "deskripsi":"\nSocket : AM4\nMemory : 4 x DDR4 DIMM, Supports DDR4\nMaximum Memory : 64GB Dual Channel\nInterface : 1x PCIE 3.0 x16, 2x PCIE 2.0 x1\nStorage : 4x SATA 6Gb/s, 1x M.2 Slot\nAudio Chipset : Realtek ALC892\nPorts : VGA Port, USB 2.0, USB 3.2 Gen1, LAN Port, HD Audio Connectors, HDMI Port, DVI-D Port",
    },
    {
        "nama":"Corsair CV Series CV650 650W 80+ Bronze ",
        "harga":950000,
        "kategori":"PSU",
        "type":"CV650",
        "merk":"Corsair",
        "deskripsi":"\nPower : 650 W\nPSU Form Factor : ATX\nCable Type : Sleeved\nConnector : 2x PCIE Connector, 1x Floppy Connector, 7x SATA Connector",
    },
    {
        "nama":"LG Monitor 22MR410-B",
        "harga":1209000,
        "kategori":"Monitor",
        "type":"22MR410-B",
        "merk":"LG",
        "deskripsi":"\nMemory Tipe : DDR4\nMemory Size : 16GB (2x8GB)\nMemory Speed : 3200MHz\nSpeed Voltage : 1.2V\nSpeed Latency : 15-15-15-36\nSpeed Rating : PC4-25600"
    },
]

voucher = [
    {
        "kode":25122003,
        "kategori":"Processor",
        "merk":"",
        "dipakai":False,
        "diskon":5,
        "expired":"2023-12-20 23:00:00",
    },
    {
        "kode":9122023,
        "kategori":"VGA Card",
        "merk":"",
        "dipakai":False,
        "diskon":3,
        "expired":"2023-12-20 23:00:00",
    },
]

batas_pembayaran_transaksi = 5
done = False

def cekPelanggan(email,password):
    i = 0
    for pl in pelanggan:
        if (str(pl['email']) == email and str(pl['password']) == password):
            return i
        i+=1
    return "Tidak Ada"

def failedLogin(email):
    i = 0
    for pl in pelanggan:
        if(str(pl['email']) == str(email)):
            pelanggan[i]['failed_login'] += 1
            return pl['failed_login']
        i += 1
    return 0

def cekVoucher(kode):
    i = 0
    for vc in voucher:
        if vc['kode'] == kode:
            return i
        i+=1
    return "Tidak Ada"

status_login = False
pakai_atm = "y"

def cek_login(p):
    for us in mbanking:
        if us['pin'] == p:
            return us
    return False     

def cek_mbanking(id):
    for i in range(len(mbanking)):
        if mbanking[i]['id'] == str(id):
            return int(i)
    return -1

def cek_rekening(no):
    for i in range(len(pelanggan)):
        if str(pelanggan[i]['id_user']) == str(no):
            return int(i)
    return -1
            
def atm():
    status_login = False
    pakai_atm = "y"
    while pakai_atm == "y":
        while status_login == False:
            print("")
            print("==================== LOGIN KE ATM BeSeA ====================")
            print("Silahkan masukan pin anda")
            pin = input("Masukan PIN : ")
            print("")
            cl = cek_login(pin)
            if cl != False:
                print("Selamat Datang! "+cl['username'])
                print("")
                mbanking_id = cl['id']
                status_login = True
                loop = "y"
            else:
                print("")
                print("Oops PIN anda salah")
                print("")
                print("")
        
        while loop == "y" and status_login == True:
            u = mbanking[cek_mbanking(mbanking_id)]
            print("")
            print("=============== SELAMAT DATANG DI ATM BeSeA ================")
            print("Halo "+cl['username'],"!")
            print("Saldo anda : Rp.",int(mbanking[index]['saldo']))
            print("1. Top Up")
            print("2. Keluar")
            a = int(input("Silahkan pilih menu : "))
            if a == 1:
                nominal = input("Jumlah top up : Rp. ")
                index1 = cek_mbanking(mbanking_id)
                if index1 >= 0:
                    if mbanking[index1]['saldo'] >= int(nominal):
                        mbanking[index1]['saldo'] =mbanking[index1]['saldo'] - int(nominal)
                        pelanggan[index1]['saldo_pl'] =pelanggan[index1]['saldo_pl'] + int(nominal)
                        print("")
                        print("Anda berhasil top up sebesar Rp. "+ (nominal))
                        print("Sisa saldo anda adalah Rp.",mbanking[index1]['saldo'])
                    else:
                        print("")
                        print("Oops aldo anda tidak cukup")
                print("")
                loop = "n"
            elif a == 2:
                status_login = False
                loop = "n"
                pakai_atm = "n"
            else:
                print("Pilihan tidak tersedia")
            if status_login == True:
                
                input("Kembali Ke menu (Enter) ")
                print("")
                loop = "y"

def tampilkanBarang():
    no = 1
    print("")
    print("")
    print("====================== DATA BARANG =======================")
    for b in barang:
        print("============================================================")
        print("No ", no)
        print("Nama : ", b['nama'])
        print("Merk : ", b['merk'])
        print("Tipe : ", b['type'])
        print("Kategori : ", b['kategori'])
        print("Deskripsi : ", b['deskripsi'])
        print("")
        print("Harga : Rp.", b['harga'])
        print("============================================================")
        no += 1
    print("")
    print("No "+str(no)+" : Keluar")
    print("")
    beliBarang(no)

def beliBarang(no):
    plh_brg = int(input("Pilih Nomor Barang : "))
    if (plh_brg == no):
        print("")
    else:
        b = barang[plh_brg-1]
        print("======================= BELI BARANG ========================")
        print("Nama : ", b['nama'])
        print("Merk : ", b['merk'])
        print("Tipe : Rp.", b['type'])
        print("Kategori : ", b['kategori'])
        print("Deskripsi : ", b['deskripsi'])
        print("")
        print("Harga : Rp.", b['harga'])
        print("============================================================")
        print("1. Beli")
        print("2. Masukkan Kode Voucher")
        print("3. Kembali")
        plh_mana = int(input("Pilih Nomor Barang : "))
        if plh_mana == 1:
            if (b['harga'] > pelanggan[index]['saldo_pl']):
                print("Saldo Anda Tidak Cukup")
            else:
                trans = {
                    "barang":b,
                    "total":b['harga'],
                    "batas_waktu":datetime.datetime.now()+timedelta(minutes=batas_pembayaran_transaksi),
                    "status":"Belum Bayar",
                }
                print("=============================================================")
                print("Anda sudah membeli : ")
                print("Nama : ", b['nama'])
                print("Dengan harga : Rp.", b['harga'])
                print("Silahkan bayar tagihan sebelum ", trans["batas_waktu"])
                print("=============================================================")
                pelanggan[index]['transaksi'].append(trans)
        elif plh_mana == 2:
            kd_vcr = int(input("Masukkan kode voucher : "))
            cek = cekVoucher(kd_vcr)
            if cek != "Voucher tidak tersedia":
                if voucher[cek]['dipakai']:
                    print("=============================================================")
                    print("Voucher sudah tidak tersedia atau sudah digunakan")
                    print("=============================================================")
                    print("")
                    print("")
                elif (datetime.datetime.strptime(voucher[cek]['expired'], '%Y-%m-%d %H:%M:%S') < datetime.datetime.now()):
                    print("============================================================")
                    print("Masa berlaku voucher sudah habis")
                    print("============================================================")
                    print("")
                    print("")
                elif voucher[cek]['kategori'] != "all" and voucher[cek]['kategori'] != b['kategori']:
                    print("============================================================")
                    print("Voucher tidak bisa digunakan untuk barang ini")
                    print("============================================================")
                    print("")
                    print("")
                else:
                    potongan = b['harga'] * voucher[cek]['diskon']/100
                    trans = {
                        "barang":b,
                        "total": b['harga']-potongan,
                        "batas_waktu":datetime.datetime.now()+timedelta(minutes=5),
                        "status":"Belum Dibayar"
                    }
                    print("============================================================")
                    print("Anda sudah membeli : ")
                    print("Nama : ", b['nama'])
                    print("Dengan harga : Rp.", b['harga'])
                    print("Anda juga mendapatkan potongan sebesar "+str(voucher[cek]['diskon']), "%")
                    print("Total harga : Rp.", int(b['harga']-potongan))
                    print("Silahkan bayar tagihan anda sebelum : ", trans['batas_waktu'])
                    print("============================================================")
                    voucher[cek]['dipakai'] = True
                    pelanggan[index]['transaksi'].append(trans)
            else:
                print("Voucher tidak ditemukan")
        print("")
        print("")

def tampilkanTransaksi():
    no = 1
    print("")
    print("")
    print("====================== DATA TRANSAKSI ======================")
    for t in pelanggan[index]['transaksi']:
        print("============================================================")
        print("No : ", no)
        print("Nama : ", t['barang']['nama'])
        print("Merk : ", t['barang']['merk'])
        print("Type : ", t['barang']['type'])
        print("Total : Rp.", int(t['total']))
        print("Status : ", t['status'])
        print("Batas Waktu : ", t['batas_waktu'])
        print("============================================================")
        no += 1
    print("")
    print("No " + str(no) + " : Keluar")
    print("")
    bayarTransaksi(no)

def bayarTransaksi(no):
    plh_trans = int(input("Pilih Nomor Transaksi : "))
    print("")
    print("")
    if plh_trans == no:
        print("")
    else:
        trans = pelanggan[index]['transaksi'][(plh_trans - 1)]
        if trans['batas_waktu'] < datetime.datetime.now():
            print("")
            print("")
            print("============================================================")
            print("Transaksi sudah melebihi batas waktu yang ditentukan maka transaksi dianggap batal.")
            print("============================================================")
        elif trans['status'] == "Sudah bayar":
            print("============================================================")
            print("Transaksi sudah dibayar")
            print("============================================================")
        else:
            print("============================================================")
            print("No : ", no)
            print("Nama : ", trans['barang']['nama'])
            print("Merk : ", trans['barang']['merk'])
            print("Type : ", trans['barang']['type'])
            print("Total : Rp.", int(trans['total']))
            print("Status : ", trans['status'])
            print("============================================================")
            print("Berhasil membayar transaksi sebesar : Rp.", int(trans['total']))
            pelanggan[index]['saldo_pl'] -= trans ['total']
            print("============================================================")
    print("")
    print("")

while keluar == False:
    if sudah_login == False:
        print("")
        print("============ SELAMAT DATANG DI MEGATEC COMPUTER ============")
        print("1. Login")
        print("2. Keluar")
        pilihan = int(input("Masukkan pilihan anda : "))
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
            keluar = True
            break
    elif sudah_login == True:
        if pilihan == 1:
            print("")
            print("============ SELAMAT DATANG DI MEGATEC COMPUTER ============")
            print("==============================")
            print("Selamat Datang : ", pelanggan[index]['nama'])
            print("Saldo Anda : Rp.",int(pelanggan[index]['saldo_pl']))
            print("============================================================")
            print("1. Beli Barang")
            print("2. Lihat Transaksi")
            print("3. Top Up Saldo")
            print("4. Logout")
            print("5. Keluar")
            pilihan_pelanggan = int(input("Masukkan pilihan anda : "))
            if pilihan_pelanggan == 1:
                tampilkanBarang()
            elif pilihan_pelanggan == 2:
                tampilkanTransaksi()
            elif pilihan_pelanggan == 3:
                atm()
            elif pilihan_pelanggan == 4:
                sudah_login = False
            elif pilihan_pelanggan == 5:
                keluar = False
                break