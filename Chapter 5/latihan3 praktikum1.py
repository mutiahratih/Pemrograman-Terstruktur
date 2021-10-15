print ("---STATUS KELULUSAN MAHASISWA---")

bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
matematika = int(input("Masukkan nilai Matematika : "))

if (bindo > 60) and (ipa > 60) and (matematika > 70):
    print ("Status Kelulusan : LULUS")
if (bindo < 60):
    print ("Status Kelulusan : TIDAK LULUS")
    print ("Sebab : ")
    print ("- Nilai bahasa indonesia kurang dari 60")
    if (ipa < 60):
        print ("- Nilai IPA kurang dari 60")
    if (matematika < 70):
        print ("- Nilai matematika kurang dari 70")
