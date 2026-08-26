nama = str(input("Masukan Nama Anda:"))
nilai1 = int(input("Masukan Nilai MTK Anda:"))
nilai2 = int(input("Masukan Nilai Kimia Anda:"))
nilai3 = int(input("Masukan Nilai Fisika:"))

a = nilai1 + nilai2 + nilai3
rata = a / 3
if rata >= 90:
    kategori="Nilai A,perilahal sangat bagus :) 😮 "
elif rata >= 80:
    kategori="Nilai B,hasil meyakinkan :) 😋"
elif rata >= 60:
    kategori="Nilai C,seukuran beliau masih layak :) 🤭"
elif rata >= 40:
    kategori="Nilai D,perkara unik.. :| 🫤"
elif rata >= 20:
    kategori="Nilai E,patut dipertanyakan.. :( 😮‍💨"
else:
    kategori="Nilai F,cukup mengenaskan :( 🥹"


print(f"Nilai {nama} adalah {rata}")
print(f"Jadi {nama} masuk ke dalam kategori {kategori}")
