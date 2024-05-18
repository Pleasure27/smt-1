print("    GEROBAK FRIED CHICKEN ")
print("------------------------------")
print("Kode", "Jenis Potong", "Harga")
print("------------------------------")
print(" D         Dada        Rp.2500")
print(" P         Paha        Rp.2000")
print(" S         Sayap       Rp.1500")
print("------------------------------\n")

list_kode = []
list_jenis = []
list_jml = []
list_jumhar = []
list_harga =  []
jumbay = 0

data = int(input("Masukkan Banyak Jenis : "))

for i in range(data):
    print("Jenis Ke - " + str(i+1))
    list_kode.append(input("Kode Potong [D/P/S] : "))
    list_jml.append(int(input("Masukkan Banyak Potong : ")))

    if list_kode[i] == "D" or list_kode[i] == "d":
        list_jenis.append("Dada")
        list_harga.append(2500)
    elif list_kode[i] == "P" or list_kode[i] == "p":
        list_jenis.append("Paha")
        list_harga.append(2000)
    elif list_kode[i] == "S" or list_kode[i] == "s":
        list_jenis.append("Sayap")
        list_harga.append(1500)
    else:
        list_jenis.append("Salah Kode")
        list_harga.append(0)

for i in range (data):
        list_jumhar.append(list_harga[i]*list_jml[i])
        jumbay = jumbay + list_jumhar[i]
        pajak = 0.10 * jumbay
        tobay = pajak + jumbay

print("    GEROBAK FRIED CHICKEN ")
print("-------------------------------------------------")
print("No.  Jenis        Harga   Banyak   Jumlah")
print("     Potong       Satuan   Beli     Harga")
print("-------------------------------------------------")
for i in range(data):
     print (" %d     %s     %d      %d     %d " %
            (i+1, list_jenis[i], list_harga[i], list_jml[i], list_jumhar[i]))
print("-------------------------------------------------")
print("                     Jumlah Bayar : Rp.", int(jumbay))
print("                     Pajak        : Rp.", int(pajak))
print("                     Total Bayar  : Rp.", int(tobay))