mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('=================================================================')
print('NIM     NAMA MAHASISWA           TGL LAHIR       TEMPAT LAHIR    ')
print('-----------------------------------------------------------------')

for i in mhs:
    pecah = i.split(':')
    print(pecah[0].ljust(8), end='')
    print(pecah[1].ljust(25), end='')
    tanggal = pecah[2].split('-')
    urut = '/'.join([tanggal[2],tanggal[1],tanggal[0]])
    print(urut.ljust(16), end='')
    print(pecah[3].ljust(16))

print('-----------------------------------------------------------------')
