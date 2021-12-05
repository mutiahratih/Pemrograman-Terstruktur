try :
    file = input('Masukkan nama file : ')
    myfile = open(file,'r')
    keyword = int(input('Masukkan keyword decode (dalam angka): '))
    mylist = list(myfile.readline())

    akhir = ''
    for karakter in mylist:
        if(karakter.isalpha()):
            kode = ord(karakter) - ord('A')
            newkode = (kode - keyword) % 26
            newteks = newkode + ord('A')
            newkarakter = chr(newteks)
            akhir += newkarakter
        else :
            akhir += newkarakter
    fileakhir = open('decode.txt','w')
    fileakhir.write(''.join(akhir))
    fileakhir.close
    print(akhir)
except FileNotFoundError:
    print('File tidak ditemukan')
