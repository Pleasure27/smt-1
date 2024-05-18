def perkalian_matriks(matriks1, matriks2, matriks3):
    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            hasil[i][j] = matriks1[i][j] * matriks2[i][j] * matriks3[i][j]
    return hasil

matriks1 = [
    [4,7,8],
    [4,7,5],
    [2,6,8]
]

matriks2 = [
    [3,6,9],
    [2,6,9],
    [1,7,1]
]

matriks3 = [
    [6,7,8],
    [4,3,2],
    [9,1,6]
]


hasil_perkalian = perkalian_matriks(matriks1,matriks2,matriks3)

print("matriks 1:")
for row in matriks1:
    print(row)

print("\nmatriks 2:")
for row in matriks2:
    print(row)

print("\nmatriks 3:")
for row in matriks3:
    print(row)

print("\nhasil perkalian : ")
for row in hasil_perkalian:
    print(row)
    
"""
Nama Kelompok
1. Dio Herlambang (17230526)
2.Fajar Ramadhan (17230511)
3. Ambrusius Paska Dipta (17230562)
4. Haykal Ryan Andre (17230519)
5. Muhammad Nasal Ekaputra (17230564)
"""