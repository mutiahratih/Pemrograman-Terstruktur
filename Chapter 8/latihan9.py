hargabuah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}

while True:
    buah = str(input('Nama buah yang dibeli: '))
    jumlah = int(input('Berapa kg? '))
    print('-----------------------------')
    if buah in hargabuah:
        total = jumlah*hargabuah[buah]
        print('Total harga : ', total)
        break
    else:
        print('Buah tidak tersedia')
