myfile = open('penjumlahan.txt','r')
hasil = str('')
for data in myfile:
    angka = data.split('|')
    angka = angka
    jumlah = int(angka[0]) + int(angka[1].rstrip('\n'))
    hasil += str(jumlah) + '\n'

newfile = open('hasil.txt','w')
newfile.write(hasil)
print(hasil)
newfile.close()
        
