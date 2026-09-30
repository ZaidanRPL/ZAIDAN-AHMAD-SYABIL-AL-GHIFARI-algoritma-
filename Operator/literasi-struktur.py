nilai = [85, 92, 78, 95]
for n in nilai:
    print(n, end=" ")

for i, n in enumerate(nilai) :
    print(f"Nilai ke-{i+i}: {n}")

siswa = {'Budi': 85, 'Ani': 92, 'Candra': 78}
for nama, nilai in siswa.items():
    print(f"{nama}: {nilai}")

