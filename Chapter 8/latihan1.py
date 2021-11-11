print('---------------')
print('URUTAN BILANGAN')
print('---------------')

data = []
i = 1
urutan = int(input('berapa bilangan bulat?'))
while True:
    bil = int(input('Masukkan bilangan ke-' + str(i)+'='))
    data = data + [bil]
    i = i+1
    if i-1 == urutan:
        break
data.sort(reverse=True)
print(data)
