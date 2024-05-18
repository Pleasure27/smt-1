bil = 0
pilihan = 'y'
while (pilihan != 'n' or pilihan != 'N'):
    bil = int(input("Masukkan Bilangan : "))

    if (bil>50):
        print("Bilangan Melebihi Angka 50, Silahkan diulang")
        continue
    print("Pangkat dua dari Bilangan Ini Adalah :", bil*bil)
    pilihan = input("Apakah ingin mengulangi? [Y/N] : ")