mat1 = [
    [9, 21, 12],
    [3, 74, 15],
    [12, 54, 26],
]

mat2 = [
    [6, 76, 69],
    [7, 2, 23],
    [23, 24, 56],
]
mat3 = []
# Penjumlahan
for x in range(0, len(mat1)):
    for y in range(0, len(mat1[0])):
        print(mat1[x][y] + mat2[x][y]),
    print
print("")
