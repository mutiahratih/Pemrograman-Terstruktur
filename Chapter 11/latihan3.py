from datetime import *
from latihan1 import diffDate
kode = input('Masukkan kode member\t: ')
myfile = open('DATA PEMINJAMAN BUKU.txt','r')
file = myfile.readlines()
for i in range(len(file)):
    data = file[i]
    data.replace('\n','')
    datapinjam = data.split('|')
    if kode == datapinjam[0]:
        nama = datapinjam[1]
        buku = datapinjam[2]
        pinjam = datapinjam[3]
        y,m,d = (datapinjam[4].split('-'))
        maks = date(int(y),int(m),int(d))
        kembali = datetime.date(datetime.now())
        kurang = kembali-maks
        selisih = kurang.days
        if selisih < 0:
            selisih = 0
        if selisih > 0:
            denda = selisih*2000
        else:
            denda = 0
        print('DATA PEMINJAMAN BUKU')
        print('Kode member\t: ', kode)
        print('Nama member\t: ', nama)
        print('Judul buku\t: ', buku)
        print('Tanggal peminjaman\t: ', pinjam)
        print('Tanggal maks peminjaman\t: ', maks)
        print('Tanggal pengembalian\t: ', kembali)
        print('Terlambat\t\t: ', selisih, 'Hari')
        print('Denda\t\t\t: ', 'Rp', denda)
        break
    else:
        data = 'Tidak ada'
        print('Data tidak ditemukan')
        break
        
        
