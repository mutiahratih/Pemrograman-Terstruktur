try:
    masuk = str(input('Masukkan nama file : '))
    file = open(masuk,'a')
    jawab = 'y'
    while jawab == 'y' :
        tambah = str(input('Data yang mau ditambahkan : '))
        file.write(tambah)
        jawab = str(input('Mau lagi(y/n)? '))
        if jawab == 'n':
            break
    file.close()
except FileNotFoundError:
    print ('File tidak ditemukan')
