print ("---TRIPLE PYTHAGORAS---")
print ()

def pythagoras(a,b,c):
    hasil = a**2 + b**2
    if hasil == c**2:
        print ("a=",a," b=", b," c=", c, "->", True)
    else:
        print ("a=",a," b=", b," c=", c, "->", False)

pythagoras(3,4,5)
pythagoras(5,9,12)
pythagoras(8,6,10)
pythagoras(7,8,11)
