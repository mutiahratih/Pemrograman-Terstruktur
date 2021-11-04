print ("Hai.. nama saya Ms. Geny, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan ditebak ya !!!")

from random import randint
bil = randint (0,100)
score = 100

while True:
    tebak = int(input("Tebakan anda : "))
    if tebak < bil:
        print ("Hehehe.. Bilangan tebakan anda terlalu kecil")
        score -= 2
    elif tebak > bil:
        print ("Hehehe.. Bilangan tebakan anda terlalu besar")
        score -= 2
    elif score < 100:
        print ("Score anda habis")
        break
    elif tebak == bil:
        print ("Yeeee.. Bilangan tebakan anda BENAR :)")
        break
print ("Score Anda : ", str(score))
