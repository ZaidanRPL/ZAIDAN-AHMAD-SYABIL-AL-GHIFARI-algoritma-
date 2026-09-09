def garis_pemisah ():
    print("=<>=" * 12)

def sapa_siswa(nama, kelas):
    print(f"Halo, {nama} dari kelas {kelas}!")

def hitung_luas_segitiga(alas,tinggi):
    luas = 0.5 * alas + tinggi
    return luas

def hitung_keliling_persegi(sisi):
    return 4 * sisi
garis_pemisah()
nama1 = input("Masukkan nama pertama: ")
nama2 = input("Masukkan nama kedua: ")
garis_pemisah()
kelas1 = input("Masukkan kelas murid pertama: ")
kelas2 = input("Masukkan kelas murid kedua: ")
garis_pemisah()
alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
garis_pemisah()
sisi = float(input("Masukkan sisi persegi: "))


garis_pemisah()
sapa_siswa(nama1, kelas1)
sapa_siswa(nama2, kelas2)
garis_pemisah()

l_segitiga = hitung_luas_segitiga(alas,tinggi)
print(f"Luas segitiga (alas={alas} tinggi={tinggi}):{l_segitiga}")

k_persegi = hitung_keliling_persegi(sisi)
print(f"Keliling persegi (sisi={sisi}):{k_persegi}")

print(f"Total luas segitiga dan keliling persegi:{l_segitiga + k_persegi}")
garis_pemisah()