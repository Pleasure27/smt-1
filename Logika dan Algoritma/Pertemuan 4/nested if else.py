merk = input("Masukkan Merk Baju [P/A/S] : ")

if merk == "P" or merk == "p":
    print("Merk Polo")
    ukuran = input("Masukkan Ukuran Baju [L/M/S] : ")
    if ukuran == "L" or ukuran == "l":
        print("Harga Baju = Rp.300.000")
    elif ukuran == "M" or ukuran == "m":
        print("Harga Baju = Rp.225.000")
    else:
        print("Harga Baju = Rp.175.000")
elif merk == "A" or merk == "a":
    print("Merk Alissan")
    ukuran = int(input("Masukkan Ukuran Baju [L/M/S] : "))
    if ukuran == "L" or ukuran == "l":
        print("Harga Baju = Rp.275.000")
    elif ukuran == "M" or ukuran == "m":
        print("Harga Baju = Rp.200.000")
    else:
        print("Harga Baju = Rp.175.000")
else:
    print("Merk StYess")
    ukuran = int(input("Masukkan Ukuran Baju  [L/M/S] : "))
    if ukuran == "L" or ukuran == "l":
        print("Harga Baju = Rp.250.000")
    elif ukuran == "M" or ukuran == "m":
        print("Harga Baju = Rp.175.000")
    else:
        print("Harga Baju = Rp.150.000")

