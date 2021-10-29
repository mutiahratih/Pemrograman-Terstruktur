def sum(*myData):
    sum = 0
    for data in myData:
        sum += data
    return sum
def average(*myData):
    i = 0
    for data in myData:
        i += 1
    rata2 = sum(*myData)/i
    return rata2
def maks(*myData):
    maksimal = max(myData)
    return maksimal
def minimal(*myData):
    minimal = min(myData)
    return minimal
