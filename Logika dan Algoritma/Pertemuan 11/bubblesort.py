def BubbleSort(X):
    for i in range(len(X)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if X[I]>X[Max]:
                Max = I
            temp = X[i]
            X[i] = X[Max]
            X[Max] = temp
            
angka = [5,3,8,1,2,14,25,13,64,71,96,23]
BubbleSort(angka)
print(angka)