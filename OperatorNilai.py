nama = (input("Masukan Nama Anda ; "))
nilai1 = int(input("Masukan nilai Bahasa Indonesia ; "))
nilai2 = int(input("Masukan nilai Bahasa Inggris ; "))
nilai3 = int(input("Masukan nilai Bahasa Jawa ; "))

penjumlahan = nilai1 + nilai2 + nilai3
ratarata = penjumlahan / 3 
print("Rata-Rata Nilai Murid:",ratarata)

if ratarata >= 75:
    nama = print("Nilai Rata-Rata " + nama + " Diatas 75")
    
else :
    nama = print("Nilai Rata-Rata " + nama + " Dibawah 75")
 