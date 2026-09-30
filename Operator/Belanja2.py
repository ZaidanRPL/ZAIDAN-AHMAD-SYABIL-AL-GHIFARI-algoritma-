belanja = []

for i in range(5):
    barang = input(f"Masukkan barang ke-{i+1}: ")
    belanja.append(barang)

print("\n=== DAFTAR BELANJA ===")
for i, barang in enumerate(belanja, start=1):
    print(f"{i}. {barang}")

print(f"\nTotal item: {len(belanja)}")
print(f"Item ke-3: {belanja[2]}")
