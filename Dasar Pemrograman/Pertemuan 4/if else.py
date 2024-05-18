kode_baju = str(input("Masukkan Kode Baju [SP/AD] : "))
ukuran = str(input("Masukkan Ukuran Baju [S/M] : "))

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran == "S" or ukuran =="s":
        harga1 = 450000
    elif ukuran == "M" or ukuran == "m":
        harga1 = 500000
    else:
        harga1 = 0
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga1 = 650000
    elif ukuran == "M" or ukuran == "m":
        harga1 = 700000
    else:
        harga1 = 0
else:
    merk = "Anda Salah Memasukkan Kode Produk"
    harga1 = 0

tambah = str(input("Apakah anda ingin menambah barang? "))
if tambah == "YA" or tambah == "Ya" or tambah == "ya":
    pass

kode_baju = str(input("Masukkan Kode Baju [SP/AD] :"))
ukuran1 = str(input("Masukkan Ukuran Baju [S/M] :"))
if kode_baju == "SP" or kode_baju == "sp":
    brand = "SuperDry"
    if ukuran1 == "s" or ukuran == "S":
        biaya1 = 450000
    elif ukuran1 == "m" or ukuran == "M":
        biaya1 = 500000
    else:
        biaya1 = 0
elif kode_baju == "AD" or kode_baju == "ad":
    brand = "Adidas"
    if ukuran1 == "S" or ukuran == "s":
        biaya1 = 650000
    elif ukuran1 == "M" or ukuran == "m":
        biaya1 = 700000
    else:
        biaya1 = 0
else:
        0


print("====================")
print("Merk Baju : ", str(merk)+ "[" +str(ukuran) + "]" + " + "
                     +str (brand)+ "[" + str(ukuran1) + "]" ) 
print("Harga : Rp.", int(harga1 + biaya1))
