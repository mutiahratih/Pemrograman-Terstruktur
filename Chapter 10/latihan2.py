myfile = open('input.txt','w')

while True:
    nim = input('Masukkan NIM\t\t:')
    nama = input('Masukkan nama Mhs\t:')
    alamat = input('Masukkan alamat\t\t:')
    print()
    ulang = input('Ulangi input lagi(y/n)?\t:')
    print()
    myfile.write('{0}|{1}|{2}\n'.format(nim,nama,alamat))
    if ulang not in ('y','Y'):
        break
myfile.close()
