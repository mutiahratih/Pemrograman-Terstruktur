print ("Hai.. nama saya Ms. Geny, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan ditebak ya !!!")

from random import randint
bil = randint (0,100)

while True:
    tebak = int(input("Tebakan anda : "))
    if tebak < bil:
        print ("Hehehe.. Bilangan tebakan anda terlalu kecil")
    elif tebak > bil:
        print ("Hehehe.. Bilangan tebakan anda terlalu besar")
    elif tebak == bil:
        print ("Yeeee.. Bilangan tebakan anda BENAR :)")
        break
