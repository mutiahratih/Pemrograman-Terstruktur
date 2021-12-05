myfile = open('input.txt','r')

datamhs = {}
i = 1

for data in myfile:
    mydata = {}
    pecah = data.split('|')
    mydata['nim'] = pecah[0]
    mydata['nama'] = pecah[1]
    mydata['alamat'] = pecah[2].rstrip('\n')

    datamhs[i] = mydata
    i += 1
print(datamhs)
    
