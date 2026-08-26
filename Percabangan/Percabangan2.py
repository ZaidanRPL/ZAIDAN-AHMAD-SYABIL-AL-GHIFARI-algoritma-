nama = str(input("Masukan Nama Anda:"))
nilai = int(input("Masukan Nilai Anda:"))
akhlak = int(input("Masukan Nilai Akhlak Anda:"))
absen = int(input("Masukan Nilai  Anda:"))

if nilai >= 70:
    if akhlak >= 70:
        if absen <= 10:
            print("Lulus,hore hore")

else:
    print("Tidak Lulus,Coba Lagi lain Saat")