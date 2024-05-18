
def SelectionSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]>array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp

def BubbleSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]>array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp

def InsertionSort(X):
    for index in range(0,len(X)):
        a = X[index]
        b = index
        while b > 1 and X[b-1]>a:
            X[b]=X[b-1]
            b = b-1
        X[b] = a
data1 = [90,87,65,73,59,48,36,27,13,8,5,3,12,33,45,45,67,85,90,92,103]

print("Ascending")
SelectionSort(data1)
BubbleSort(data1)
InsertionSort(data1)
print(data1)


def SelectionSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]<array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp
            


def BubbleSort(array):
    for i in range(len(array)-1,0,-1):
        Max = 0
        for I in range(1,i+1):
            if array[I]<array[Max]:
                Max = I
            temp = array[i]
            array[i] = array[Max]
            array[Max] = temp




def InsertionSort(X):
    for index in range(0,len(X)):
        a = X[index]
        b = index
        while b < 0 and X[b-1]<a:
            X[b]=X[b-1]
            b = b-1
        X[b] = a
        
data1 = [90,87,65,73,59,48,36,27,13,8,5,3,12,33,45,45,67,85,90,92,103]
        
print("Descending")
SelectionSort(data1)
BubbleSort(data1)
InsertionSort(data1)
print(data1)

print("")
print("Muhammad Nasal Ekaputra")
print("17230564")
print("17.1A.04")