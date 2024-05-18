n = int(input("Masukkan Anak Ayam : "))
print("Tek Kotek Kotek Kotek, Anak Ayam Turun Berkotek Anak Ayam Turunlah 1, mati 1 Tinggal Induknya")
if n>2:
    while n>2:
        print("Anak Ayam Turunlah %d Mati Satu Tinggallah %d"%(n, n-1))
        n=n-1
    if n == 2:
        print("Anak Ayam Turunlah %d Mati Satu Tinggallah Induknya"%(n))