def rata(hargabuah):
    rata2 = sum(hargabuah.values())/len(hargabuah.keys())
    print('Rata-ratanya: ', rata2)

hargabuah = {'apel':5000,'jeruk':8500,'mangga':7800,'duku':6500}
print(hargabuah)
rata(hargabuah)
