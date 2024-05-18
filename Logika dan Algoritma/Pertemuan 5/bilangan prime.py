bilangan = int(input("Masukkan bilangan : "))
if bilangan > 1:
    for i in range(2, bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "Bukan Bilangan Prima")
            print(i, "kali", bilangan//i, "=", bilangan)
            break
    else:
        print(bilangan, "Adalah Bilangan Prima")
else:
    print(bilangan, "Bukan Bilangan Prima")