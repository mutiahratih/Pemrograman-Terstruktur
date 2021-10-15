print ("---PERHITUNGAN GAJI KARYAWAN---")

kode = input ("Masukkan kode karyawan : ")
nama = input ("Masukkan nama karyawan : ")
gol = input ("Masukkan golongan : ")
status = input ("Masukkan status (1: menikah,2:belum) : ")


if (gol == "A") or (gol == "a"):
    gajipokok = 10000
    potongan = 2.5
elif (gol == "B") or (gol == "b"):
    gajipokok = 8500
    potongan = 2.0
elif (gol == "C") or (gol == "c"):
    gajipokok = 7000
    potongan = 1.5
elif (gol == "D") or (gol == "d"):
    gajipokok = 5500
    potongan = 1.0
if status == "1" :
    tunjanganistri = 10
    anak = int(input("Masukkan jumlah anak : "))
    tunjangananak = 5
    tunjangan1 = gajipokok*(tunjanganistri/100)
    tunjangan2 = gajipokok*(tunjangananak/100)*anak
else:
    anak = 0
    tunjangan1 = 0
    tunjangan2 = 0
gajikotor = gajipokok+tunjangan1+tunjangan2
gajipotongan = gajikotor*(potongan/100)

print ("=====================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-------------------------------------")
print ("Nama Karyawan : " + nama + "(Kode: " + kode + ")")
print ("Golongan : " + gol)
print ("Status Menikah : " + status)
print ("Jumlah Anak : " + str(anak))
print ("-------------------------------------")
print ("Gaji Pokok : " + "Rp " + str(gajipokok))
print ("Tunjangan Istri/Suami : " + "Rp " + str(tunjangan1))
print ("Tunjangan Anak : " + "Rp " + str(tunjangan2))
print ("-------------------------------------")
print ("Gaji Kotor : " + "Rp " + str(gajikotor))
print ("Potongan" + "("+str(potongan)+"%) :" + "Rp " + str(gajipotongan))
print ("-------------------------------------")
print ("Gaji Bersih :" + "Rp " + str(gajikotor-gajipotongan))

