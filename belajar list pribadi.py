#Menggunakan Slicing List
list_buah = ['anggur', 'rambutan', 'mangga', 'durian']

print("<Slicing List>")
print("======================================================")
print(list_buah)
print("======================================================")
print(" v Menggunakan Slicing List v ")

print(list_buah[3])
print(list_buah[1:])
print(list_buah[2:])
print(list_buah[:3])
print(list_buah[:4])
print(list_buah[:2])


print(' ')
#/////////////////////////////////////////////////////////#

#Mengubah Data Dalam List

list_buah = ['anggur', 'rambutan', 'mangga', 'durian']

print("<Mengubah Data Dalam List>")
print("======================================================")
print(list_buah)
print("======================================================")

list_buah[0] = 'BUAH NAGA' #Angka "0" merupakan urutan buah dalam list
list_buah[2:4] = 'KLENGKENG', 'MELON' #mengubah data dalam range list
print("--> ", list_buah)

print(" ")
#/////////////////////////////////////////////////////////////#
#Menambahkan data dalam list

#menambahkan data pada list menggunakan .append()
#append digunakan untuk menambahkan nilai variabel pada bagian belakang

list_buah = ['anggur', 'rambutan', 'mangga', 'durian']

print(">>>>> Menambahkan Data Dalam List <<<<<")

print("======================================================")
print(list_buah)
print("======================================================")
print(" v Menggunakan .append() v ")

list_buah.append('SEMANGKA')
print("--> ", list_buah) 

print(" ")

#menambahkan data pada list menggunakan .insert()
#insert digunakan untuk menambahkan nilai variabel dimanapun dalam list

list_buah = ['anggur', 'rambutan', 'mangga', 'durian']

print(" v Menggunakan Insert v ")

list_buah.insert(0,'DUKUH')
print("--> ", list_buah)

# angka "0" bisa kita ganti dengan list buah yang ingin kita tambahkan dalam list


print(" ")


#//////////////////////////////////////////////////////////////////#
# Menghapus Data dalam list

#menghapus dan menyimpan nilai variabel menggunakan .pop()
# .pop() digunakan untuk  menghapus dan menyimpan nilai variabel dalam list

list_baju = ['Gamis', 'Kaos', 'Hoodie', 'Kemeja', 'Bomber']

print(">>>>>Menghapus Data Dalam List<<<<<")

print("======================================================")
print(list_baju)
print("======================================================")
print(" v Menggunakan .pop() v ")

baju_yang_terhapus = list_baju.pop() #menyimpan data dengan .pop()

print("--> ", list_baju)
print("----> Baju yang tersimpan: ", baju_yang_terhapus)

""" 'pop()' digunakan untuk menghapus data 
 pada bagian belakang dalam list dan menyimpannya pada variabel baru"""

print(" ")

#menghapus data pada list menggunakan ".remove()"
#remove digunakan untuk menghapus nilai variabel dari list

list_baju = ['Gamis', 'Kaos', 'Hoodie', 'Kemeja', 'Bomber']

print("======================================================")
print(list_baju)
print("======================================================")
print(" v Menggunakan .remove() v ")

list_baju.remove('Gamis')
print("1 --> ", list_baju)

list_baju.remove('Hoodie')
print("2 --> ", list_baju)

print(" ")

#menghapus data pada list menggunakan statement del
#del digunakan untuk menghapus nilai variabel dari list

list_baju = ['Gamis', 'Kaos', 'Hoodie', 'Kemeja', 'Bomber']

print("======================================================")
print(list_baju)
print("======================================================")
print(" v Menggunakan Statement del v ")

del list_baju[0]
print("1 --> ", list_baju)

del list_baju[0:2]
print("2 --> ", list_baju)





