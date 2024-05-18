n = int(input("Masukkan Bilangan/Karakter : "))
kar = input("Masukkan Karakter : ")

if 1<=n<=100:
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + kar * stars)
else:
    print("diluar jangkauan 100")