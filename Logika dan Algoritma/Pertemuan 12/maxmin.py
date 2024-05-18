A = [23,4,21,5,6,767,843,34]

def STRAITMAXMIN(A,n):
    max = A[0]
    min = A[0]
    for i in range(1,n):
        if A[i] > max:
            max = A[i]
        else:
            if A[i] < min:
                min = A[i]
    print("Max = ", max, "Min = ", min)