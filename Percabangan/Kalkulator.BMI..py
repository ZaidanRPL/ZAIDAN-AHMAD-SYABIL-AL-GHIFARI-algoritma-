nama = str(input("Masukan Nama Anda:"))
berat = int(input("Masukan Berat Anda(dalam KG):"))
tinggi = float(input("Masukan Tinggi Anda (dalam meter):"))

hasil=berat/tinggi**2

if hasil <= 18.5:
    kategori=("Kekurangan berat badan (Kurus).")
if hasil >= 18.5:
    kategori=("Normal (Ideal).")
if hasil >= 23.0:
    kategori=("Kelebihan berat badan (Gemuk).")
if hasil >= 25.0:
    kategori=("Obesitas Tingkat I.")
if hasil >= 30.0:
    kategori=("Obesitas Tingkat II.")

print(f"Jadi {nama} hasil perhitungan BMI anda adalah {hasil}")
print(f"{nama} termasuk kategori {kategori}")
