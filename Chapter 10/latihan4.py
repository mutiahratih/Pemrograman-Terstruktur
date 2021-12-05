myfile = open('input.txt','r')
cari = input('Masukkan NIM yang mau dicari : ')

for data in myfile:
    mydata = data.split('|').copy()
    nim = data.split('|')[0]
    if nim == cari:
        datamhs = mydata
        break
if datamhs:
    print('DATA MAHASISWA')
    print('NIM\t: ', mydata[0])
    print('Nama\t: ', mydata[1])
    print('Alamat\t: ', mydata[2])
else:
    print('Data tidak ditemukan')
