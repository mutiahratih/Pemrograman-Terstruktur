from datetime import *
def diffDate(x):
    skrg = datetime.date(datetime.now())
    y, m, d = x.split('-')
    tanggal = date(int(y),int(m),int(d))
    selisih = skrg - tanggal
    selisihHari = abs(selisih.days)
    return selisihHari
