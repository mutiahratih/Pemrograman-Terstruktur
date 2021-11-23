def bintang(n):
    for i in range(0,n//2):
        print(('*'*(2*i+1)).center(n))
    print('*'*n)
    for i in range(n//2,0,-1):
        print(('*'*(2*i-1)).center(n))
bintang(7)
