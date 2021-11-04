print ("---STATUS KELULUSAN MAHASISWA---")

bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
matematika = int(input("Masukkan nilai Matematika : "))

if (100 > bindo > 60) and (100 > ipa > 60) and (100 > matematika > 70):
    print ("Status Kelulusan : LULUS")
elif (bindo < 0) or (ipa < 0) or (matematika < 0):
    print ("Maaf input ada yang tidak valid")
elif (bindo > 100) or (ipa > 100) or (matematika > 100):
    print ("Maaf input ada yang tidak valid")
else :
    print ("Status Kelulusan : TIDAK LULUS")

