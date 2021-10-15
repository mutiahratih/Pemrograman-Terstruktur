print ("---STATUS KELULUSAN MAHASISWA---")

print ("Range nilai 0-100")
bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA : "))
matematika = int(input("Masukkan nilai Matematika : "))

if (100 > bindo > 60) and (100 > ipa > 60) and (100 > matematika > 70):
    print ("Status Kelulusan : LULUS")
else :
    print ("Status Kelulusan : TIDAK LULUS")
    
