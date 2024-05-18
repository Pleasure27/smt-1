def InsertionSort(val):
    for index in range(1,len(val)):
        a = val[index]
        b = index
        while b > 0 and val[b-1]>a:
            val[b]=val[b-1]
            b = b-1
        val[b] = a
            
angka = [1000,200,326,186,291,438,128,321]
InsertionSort(angka)
print(angka)