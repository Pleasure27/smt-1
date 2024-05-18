def SelectionSort(val):
    for i in range(len(val)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if val[I]>val[Max]:
                Max = I
            temp = val[i]
            val[i] = val[Max]
            val[Max] = temp
            
angka = [22,10,15,3,8,2]
SelectionSort(angka)
print(angka)