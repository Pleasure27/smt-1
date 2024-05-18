def InsertionSort(array):
    for index in range(0,len(array)):
        a = array[index]
        b = index
        while b > 1 and array[b-1]>a:
            array[b]=array[b-1]
            b = b-1
        array[b] = a
            
angka = [90,87,65,73,59,48,36,27,13,8,5,3,12,33,45,45,67,85,90,92,103]
InsertionSort(angka)
print(angka)