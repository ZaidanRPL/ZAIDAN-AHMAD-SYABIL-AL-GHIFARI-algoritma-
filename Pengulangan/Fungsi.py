panjang = int(input("Masukan panjang: "))
tinggi = int(input("Masukan tinggi: "))

luas = panjang * tinggi
def luas_persegi_panjang(panjang, tinggi):
    return panjang * tinggi

hasil = luas_persegi_panjang(panjang, tinggi)
print("=" * 20)
print(f"Hasilnya adalah {hasil}")
print("=" * 20)

def sapa(nama="Anton", salam="halo"):
    print(salam + ", " + nama +"!" )

sapa('Alfonso Deaburquerque')

