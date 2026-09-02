tinggi=6

for i in range(tinggi):
    spasi = " " *(tinggi - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)


for i in range(tinggi -2, -1, -1):
    spasi = " " * (tinggi - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)
