print('DATA MAHASISWA')
print()

data = []
i = 0
jumlah = int(input('Berapa Mahasiswa ? '))
while True:
    mhs = str(input('Nama mahasiswa: '))
    data = data + [mhs]
    i = i+1
    if i == jumlah:
        break
data.sort()
for i in data:
    print(i + ' ' + str(len(i)) + ' karakter')
