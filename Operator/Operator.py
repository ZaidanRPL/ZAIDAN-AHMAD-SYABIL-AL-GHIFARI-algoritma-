nilai1 = int(input("Masukan nilai pelajaran ; "))
nilai2 = int(input("Masukan nilai akhlak ; "))

penjumlahan = nilai1 + nilai2
print("Hasil penjumlahan:",penjumlahan) 

lebih_besar= nilai1 >= nilai2
lebih_kecil= nilai1 <= nilai2
Sama_Besar= nilai1 == nilai2

print("nilai 1 lebih besar dari nilai 2",lebih_besar)
print("nilai 1 lebih kecil dari nilai 2",lebih_kecil)
print("nilai 1 sama besar dengan nilai 2",Sama_Besar)

if nilai1 > 70 and nilai2 > 70:
    print("Anda Lulus")
else:
    print("Anda Gagal")

Hasil_akhir = penjumlahan / 2
print("Nilai rata-rata:",Hasil_akhir)