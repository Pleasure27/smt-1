def tambah_matriks(matriks1, matriks2, matriks3):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j] + matriks3[i][j]
    return hasil

matriks1 = [
    [45,37,80],
    [34,47,50],
    [12,26,80]
]

matriks2 = [
    [34,64,98],
    [32,67,90],
    [21,67,40]
]

matriks3 = [
    [64,37,68],
    [14,73,20],
    [90,30,36]
]

hasil_pemjumlahan = tambah_matriks(matriks1,matriks2,matriks3)

print("matriks 1:")
for row in matriks1:
    print(row)

print("\nmatriks 2:")
for row in matriks2:
    print(row)

print("\nmatriks 3:")
for row in matriks3:
    print(row)

print("\nhasil penjumlahan : ")
for row in hasil_pemjumlahan:
    print (row)
    
"""
Nama Kelompok
1. Dio Herlambang (17230526)
2. Fajar Ramadhan (17230511)
3. Ambrusius Paska Dipta (17230562)
4. Haykal Ryan Andre (17230519)
5. Muhammad Nasal Ekaputra (17230564)
"""