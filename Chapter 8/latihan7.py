def mahal(hargabuah):
    data = max(hargabuah.values())
    for x,y in hargabuah.items():
        if y == data:
            print('Buah paling mahal: ',x,y)

hargabuah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
print(hargabuah)
mahal(hargabuah)
