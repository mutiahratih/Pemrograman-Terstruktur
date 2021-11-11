print('STATISTIK DATA')
print()

def datastat(mylist):
    data = []
    rata2 = sum(mylist)/len(mylist)
    tinggi = max(mylist)
    rendah = min(mylist)
    data.append(rata2)
    data.append(tinggi)
    data.append(rendah)
    print(data)
    return data
mylist = [1,2,3,4,5]
print(mylist)
datastat(mylist)
    
