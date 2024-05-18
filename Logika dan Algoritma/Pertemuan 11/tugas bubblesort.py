def BubbleSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]>array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp
            
data1 = [90,87,65,73,59,48,36,27,13,8,5,3,12,33,45,45,67,85,90,92,103]
BubbleSort(data1)
print("Ascending")
print(data1)

def BubbleSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]<array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp
            
data2 = [90,87,65,73,59,48,36,27,13,8,5,3,12,33,45,45,67,85,90,92,103]
BubbleSort(data2)
print("Descending")
print(data2)