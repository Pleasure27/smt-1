list_ktg = []
list_brg = []
list_hrg = []
list_jmlh = []
list_jumhar = []
list_desk = []

print("==============================================================================")
print("Selamat Datang di Toko Cemerlang Elektronik")
print("disini kami menyediakan barang elektronik terbaik dengan harga termurah")
print("")
print("Silahkan Pilih Barang yang ingin anda beli")
print("1. Beli")
print("2. Jual")

pilihan = int(input("Masukkan Pilihan anda: "))
stop = False
i = 0

while(not stop):
    if pilihan == 2:
        list_brg_baru = input("Masukkan Nama Barang ke-{}: ".format(i))
        list_brg.append(list_brg_baru)
        
        list_hrg_baru = int(input("Masukkan Harga Produk ke-{}: ".format(i)))
        list_hrg.append(list_hrg_baru)
        
        list_desk_baru = input("Masukkan Deskripsi Produk ke-{}: ".format(i))
        list_desk.append(list_desk_baru)
        
        
        
        if pilihan == 1:
            print("Pilih Kategori Barang:")
            print("1. Monitor")
            print("2. Processor")
            print("3. VGA")
            print("4. SSD")
            print("5. PSU")
            print("6. RAM")
            
            pil_kat = int(input("Masukkan pilihan kategori [1-6] : "))
            
            if pil_kat == 1:
                print("================================================")
                print("Kategori Monitor")
                print("================================================")
            


