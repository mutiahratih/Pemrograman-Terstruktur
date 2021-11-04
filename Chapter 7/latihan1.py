try:
    masuk = str(input('Masukkan nama file : '))
    
    file = open(masuk,'r')
    print('Isi file ',masuk)
    print(file.read())
except FileNotFoundError:
    print ('File tidak ditemukan')
