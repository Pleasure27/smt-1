def pembagian_matriks(matriks1, matriks2, matriks3):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] // matriks2[i][j] // matriks3[i][j]
    return hasil

matriks1 = [
    [141,771,481],
    [214,427,415],
    [215,461,812]
]

matriks2 = [
    [6,3,11],
    [2,15,9],
    [10,7,11]
]

matriks3 = [
    [2,7,8],
    [3,3,2],
    [9,4,6]
]


hasil_pembagian = pembagian_matriks(matriks1,matriks2,matriks3)

print("matriks 1:")
for row in matriks1:
    print(row)

print("\nmatriks 2:")
for row in matriks2:
    print(row)

print("\nmatriks 3:")
for row in matriks3:
    print(row)

print("\nhasil pembagian : ")
for row in hasil_pembagian:
    print(row)
    
"""
Nama Kelompok
1. Dio Herlambang (17230526)
2.Fajar Ramadhan (17230511)
3. Ambrusius Paska Dipta (17230562)
4. Haykal Ryan Andre (17230519)
5. Muhammad Nasal Ekaputra (17230564)
"""