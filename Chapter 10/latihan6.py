teks = input('Masukkan nama Teks asli : ')
step = int(input('Keyword (dalam angka) : '))

mylist = list(teks)
akhir = ''
for karakter in mylist:
    if (karakter.isalpha()):
        kode = ord(karakter) - ord('A')
        newKode = (kode + step) % 26
        newTeks = newKode + ord('A')
        newKarakter = chr(newTeks)
        akhir += newKarakter
    else:
        akhir += newKarakter
print('Hasil Enkripsi : ', akhir)
