myfile = open('bilangan.txt','r')
ganjil = 0
genap = 0
for data in myfile:
    if (int(data)%2 == 0):
        genap += 1
    else:
        ganjil += 1
print('Banyaknya bilangan genap : ', genap)
print('Banyaknya bilangan ganjil : ', ganjil)
myfile.close()
