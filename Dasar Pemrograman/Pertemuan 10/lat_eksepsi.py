import sys

lists = ['a', 0, 4]

for each in lists:
    try:
        print("Masukkan :", each)
        r = 1/int(each)
        break
    except:
        print("Uppssss>", sys.exc_info()[0], ' terrjadi')
        print("Masukkan berikutnya: ")
        print()
print("Kebalikkan dari ", each, "=", r)