import random
def shuffleString(x,n):
    mylist = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x,len(x)))
        if (acak not in mylist):
            mylist += [acak]
            i += 1
    print(mylist)
shuffleString('aku', 3)
shuffleString('aku', 4)
shuffleString('aku', 5)
