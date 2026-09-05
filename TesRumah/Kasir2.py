print("Selamat Datang Di Toko Uhui")
print("Kami Menyediakan Berbagai Mainan Yang menarik")

print("•List Mainan")

print("-Rubik 2x2(a)")
print("Harga RP 21.000")

print("-Rubik 3x3(b)")
print("Harga RP 33.000")

print("-Rubik 4x4(c)")
print("Harga RP 41.000")

print("-Rubik 5x5(d)")
print("Harga RP 46.000")

a=21.000
b=33.000
c=41.000
d=46.000

nama=str(input("Masukan Nama Anda:"))
kode=str(input("Masukan Kode Barang:"))
jumlah=int(input("Masukan Jumlah barang:"))
uang=float(input("Masukan Total Pembayaran Anda:"))

if kode == "a":
  hasil=(jumlah*a)
  
elif kode == b:
  hasil=jumlah*b
  
elif kode == c:
  hasil=jumlah*c
  
elif kode == d:
  hasil=jumlah*d

print(f"Total Belanja Anda Adalah {hasil}00 Rupiah")


if hasil<uang:
  kembalian=uang-hasil
  print(f"Selamat Atas Pembelian Anda {nama},anda masi punya kembalian {kembalian}00 Rupiah")
elif hasil>uang:
  kurang=hasil-uang
  print(f"Maaf {nama},tetapi anda masi kurang {kurang}00 Rupiah")
else:
  print(f"Selamat Atas Pembelian Anda {nama}.")

  