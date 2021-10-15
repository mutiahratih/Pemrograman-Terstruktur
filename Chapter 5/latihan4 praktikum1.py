print ("---PERHITUNGAN GAJI KARYAWAN---")

kode = input ("Masukkan kode karyawan : ")
nama = input ("Masukkan nama karyawan : ")
gol = input ("Masukkan golongan : ")

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
gajipotongan = gajipokok*(potongan/100)

print ("=====================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-------------------------------------")
print ("Nama Karyawan : " + nama + "(Kode: " + kode + ")")
print ("Golongan : " + gol)
print ("-------------------------------------")
print ("Gaji Pokok : " + "Rp " + str(gajipokok))
print ("Potongan" + "("+str(potongan)+"%) :" + "Rp " + str(gajipotongan))
print ("-------------------------------------")
print ("Gaji Bersih :" + "Rp " + str(gajipokok-gajipotongan))

