def faktorial(n):
    faktorial = 1
    for i in range(2,n+1):
        faktorial *= i
    return faktorial

c = faktorial(5)/(faktorial(3)*faktorial(5-3))
print ("C (5,3) : ", c)

p = faktorial(10)/faktorial(10-7)
print ("P (10,7) : ", p)
