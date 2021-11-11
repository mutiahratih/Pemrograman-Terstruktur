print('DATA SAYURAN')
myset = {'bayam','kangkung','wortel','selada'}

print('menu pilihan')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')

while True:
    pilih = str(input('Pilihan anda : '))
    if pilih == 'a':
        tambah = str(input('menu tambahan: '))
        myset.add(tambah)
    try:
        if pilih == 'b':
            hapus = str(input('sayur yang akan dihapus: '))
            myset.remove(hapus)
    except KeyError:
        print('data tidak ditemukan')
    if pilih == 'c':
        print(myset)
        break
