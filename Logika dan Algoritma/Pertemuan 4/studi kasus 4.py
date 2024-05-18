bany_produk = int(input("Masukkan Jumlah Produk yg Terjual : "))
har_produk = int(input("Masukkan Harga Satuan Produk : "))
gaji = 5000000

if bany_produk > 100:
    bonus = (har_produk * bany_produk) * 20/100
else:
    bonus = (har_produk * bany_produk) * 10/100

total_jual = bany_produk * har_produk
total_gaji = gaji + bonus
print("Gaji Pokok  Karyawan = ", gaji)
print("Bonus Karyawan = ", int(bonus))
print (" ")
print("Total Jual: ", int(total_jual))

print("Total Gaji + Bonus : ", int(total_gaji))