n = 0
ganjil = 0
jumlah = 0
while n < 100:
    n +=1
    if n % 2 != 0:
        print (n)
        ganjil += 1
        jumlah += n
print ("Banyaknya bilangan ganjil : ", str(ganjil))
print ("Jumlah seluruh bilangan : ", str(jumlah))
