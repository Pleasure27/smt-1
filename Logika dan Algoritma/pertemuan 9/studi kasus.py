matriks = ([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])

for i in range(4):
    for j in range(4):
        if i==j:
            matriks[i][j]=2
        if i<j:
            matriks[i][j]=1
        if i>j:
            matriks[i][j]=0
for i in range(4):
    print(matriks[i])