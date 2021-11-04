print ('------------------------')
print ('PROGRAM HITUNG RATA-RATA')
print ('------------------------')

data = []

while True:
    try:
        masuk = int(input('Masukkan bilangan bulat : '))
        data.append(masuk)
            
        jawab = str(input('Lagi (y/n)? '))
        if jawab == 'n':
            rata2 = sum(data)/len(data)
            print ('===========================')
            print ('Rata-ratanya adalah: ', rata2)
            break
    except ValueError:
        print ('Bukan bilangan bulat')    
