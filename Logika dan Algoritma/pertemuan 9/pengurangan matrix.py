def pengurangan_matriks(matriks1, matriks2, matriks3):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] - matriks2[i][j] - matriks3[i][j]
    return hasil

matriks1 = [
    [14,77,48],
    [24,47,45],
    [25,46,82]
]

matriks2 = [
    [13,16,11],
    [12,11,19],
    [11,17,11]
]

matriks3 = [
    [12,17,18],
    [11,13,12],
    [19,11,16]
]


hasil_pengurangan = pengurangan_matriks(matriks1,matriks2,matriks3)

print("matriks 1:")
for row in matriks1:
    print(row)

print("\nmatriks 2:")
for row in matriks2:
    print(row)

print("\nmatriks 3:")
for row in matriks3:
    print(row)

print("\nhasil pengurangan : ")
for row in hasil_pengurangan:
    print(row)
    
"""
Nama Kelompok
1. Dio Herlambang (17230526)
2.Fajar Ramadhan (17230511)
3. Ambrusius Paska Dipta (17230562)
4. Haykal Ryan Andre (17230519)
5. Muhammad Nasal Ekaputra (17230564)
"""