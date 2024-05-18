jus_yang_tersedia = ('mangga', 'rambutan', 'apel', 'jeruk', 'nanas',\
                     'alpukat', 'anggur', 'durian', 'red_velvet')
jus_yang_dicari = input('Masukkan Nama Jus: ')

if (jus_yang_dicari in jus_yang_tersedia):
    print('Jus Tersedia!')
else:
    print('Maaf, Jus yang anda cari tidak tersedia')
