def nilaiakhir(nilaimhs):
    nilaiakhir = None
    akhir = {}
    for x in nilaimhs:
        nilai = (x['mid']+(2*x['uas']))/3
        if(nilaiakhir is None) or (nilai > nilaiakhir):
            nilaiakhir = nilai
            akhir['nim'] = x['nim']
            akhir['nama'] = x['nama']
    return akhir
    


nilaimhs = [{'nim':'A01','nama':'Amir','mid':50,'uas':80},
            {'nim':'A02','nama':'Budi','mid':40,'uas':90},
            {'nim':'A03','nama':'Cici','mid':50,'uas':50},
            {'nim':'A04','nama':'Dedi','mid':20,'uas':30},
            {'nim':'A05','nama':'Fifi','mid':70,'uas':40}]
print(nilaimhs)
print()
akhir = nilaiakhir(nilaimhs)
if(bool(akhir)):
    print('Mahasiswa dengan nilai tertinggi adalah {0}, nim {1}'.format(akhir['nama'],akhir['nim']))
