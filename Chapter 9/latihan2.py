def bintang(n):
    kolom = 2*n-1
    for i in range(n):
        print(('*'*(2*i+1)).center(kolom))

bintang(4)
