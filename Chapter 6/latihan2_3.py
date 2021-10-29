def starFormation(n):
    n = n//2
    for i in range (0,n):
        for j in range (0,i+1):
            print ("*", end="")
        print ("\r")
    for i in range (n+2,0,-1):
        for j in range (0,i-1):
            print ("*", end="")
        print ("\r")
starFormation(7)
