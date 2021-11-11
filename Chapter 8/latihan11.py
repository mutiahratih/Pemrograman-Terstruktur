hargabuah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

print('Menu:')
print('A. Tambah data buah')
print('B. Beli buah')

pilih = str(input('Pilihan menu: '))
if pilih == 'a':
    buah = str(input('Masukkan nama buah: '))
    harga = int(input('Masukkan harga satuan: '))
    if buah in hargabuah:
        print('buah '+buah+' sudah tersedia')
        print(hargabuah)
    else:
        hargabuah[buah] = harga
        for x,y in hargabuah.items():
            print('-'+x+' ('+str(y)+')')
if pilih == 'b':
    total = 0            
    while True:
        buah = str(input('Nama buah yang dibeli: '))
        jumlah = int(input('Berapa kg? '))
        if buah in hargabuah:
            total1 = jumlah*hargabuah[buah]
            total += total1
        else:
            print('Buah tidak tersedia')
        beli = str(input('Beli buah yang lain(y/n)?'))
        if beli == 'y':
            True
        elif beli == 'n':
            print('-------------------------')
            print('Total harga : ', total)
            break
