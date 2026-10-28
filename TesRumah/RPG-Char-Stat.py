skill_point = 10

atk = 0
hp = 0
spd = 0
b_atk = 5000
b_hp = 10000
b_spd = 50
maks = 5

nama = input("Masukkan nama karakter: ")

while skill_point > 0:
    print(f"\n=== Stat Karakter {nama} ===")
    print(f"Attack      : {atk}/5")
    print(f"Health Point: {hp}/5")
    print(f"Speed       : {spd}/5")
    print(f"Skill Point : {skill_point}/10")

    print("\nStat yang ingin ditingkatkan:")
    print("1. Attack")
    print("2. Health Point")
    print("3. Speed")
    print("4. Selesai")

    pilihan = input("Masukkan pilihanmu: ")

    if pilihan == "4":
        break

    if pilihan not in ["1", "2", "3"]:
        print("Pilihan tidak valid!")
        continue

    try:
        jumlah = int(input("Berapa level yang ingin ditingkatkan?: "))
    except ValueError:
        print("ERROR: Masukkan angka!")
        continue

    if jumlah <= 0:
        print("Minimal upgrade 1 level!")
        continue

    if jumlah > skill_point:
        print("Skill Point kamu tidak cukup!")
        continue

    if pilihan == "1":
        if atk + jumlah <= maks:
            atk += jumlah
            skill_point -= jumlah
            print("Stat ATK berhasil ditingkatkan!")
        else:
            print("ATK sudah mencapai batas maksimal!")

    elif pilihan == "2":
        if hp + jumlah <= maks:
            hp += jumlah
            skill_point -= jumlah
            print("Stat HP berhasil ditingkatkan!")
        else:
            print("HP sudah mencapai batas maksimal!")

    elif pilihan == "3":
        if spd + jumlah <= maks:
            spd += jumlah
            skill_point -= jumlah
            print("Stat SPD berhasil ditingkatkan!")
        else:
            print("SPD sudah mencapai batas maksimal!")


atk_akhir = 10 * atk + b_atk
hp_akhir = 100 * hp + b_hp
spd_akhir = 5 * spd + b_spd

print(f"\n=== Stat Akhir Karakter {nama} ===")

print(f"Total ATK         : {atk_akhir}")
print(f"Total HP          : {hp_akhir}")
print(f"Total SPD         : {spd_akhir}")
print(f"Sisa Skill Point  : {skill_point}")