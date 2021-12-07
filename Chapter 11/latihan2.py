from datetime import *
pinjam = datetime.date(datetime.now())
kembali = pinjam + timedelta(days=7)
myfile = open('DATA PEMINJAMAN BUKU.txt','w')
ulang = 'y'

while ulang == 'y':
    kode = input('Masukkan kode member\t: ')
    nama = input('Masukkan nama member\t: ')
    buku = input('Masukkan judul buku\t: ')
    print()
    mylist = [kode,nama,buku,str(pinjam),str(kembali)]
    mydata = '|'.join(mylist) + '\n'
    myfile.write(mydata)
    ulang = input('Ulangi lagi (y/n)?\t ')
    print()
    if ulang == 'n':
        break
myfile.close()
