def tambah_matriks(matriks1, matriks2, matriks3, matriks4):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j]+matriks2[i][j]+matriks3[i][j]
            return hasil

matriks1 = [
    [21,22,23],
    [31,32,33],
    [41,42,43],
],
matriks2 = [
    [11,12,12],
    [56,54,76],
    [75,12,55],
],
matriks3 = [
    [43,54,22],
    [12,33,21],
    [44,75,21],
]

hasil_penjumlahan = tambah_matriks(matriks1, matriks2, matriks3)

print("Matriks 1:")
for row in matriks1:
    print(row)
    
print("Matriks 2:")
for row in matriks2:
    print(row)
    
print("Matriks 3:")
for row in matriks3:
    print(row)
z

print("\nHasil Penjumlahan: ")
for row in hasil_penjumlahan:
    print(row)