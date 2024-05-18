gp = int(input("Masukkan Gaji Pokok : "))
jk = int(input("Masukkan Jumlah Jam Kerja : "))
tjg = gp * 20/100
pajak = gp * 10/100

if jk > 200:
    lembur = (jk - 200) * 20000
else:
    lembur = 0

total = (gp + tjg + lembur - pajak)
print("=================================================")
print("Honor Yang diterima")
print("   Gaji Pokok : Rp. ", int(gp))
print("   Tunjangan  : Rp. ", int(tjg))
print("   Lembur     : Rp. ", int(lembur))
print("   Pajak      : - Rp. ", int(pajak))
print("              _________________ +")
print("   Total Gaji : Rp. ", int(total))
print("=================================================")