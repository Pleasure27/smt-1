i = 2
while (i < 50):
    j = 2
    while (j <= (i/j)):
        if not (i%j):
            break
        j = j + 1
    if (j>i/j):print(i, "Adalah Bilangan Prima")
    i = i + 1
print("Terimakasih")
