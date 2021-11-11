hargabuah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

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

