import time
import random

skill_point = 10
maks = 5

atk = 0
hp = 0
mana = 0

nama = input("Masukkan nama karakter: ")
time.sleep(1)
while skill_point > 0:
    print(f"\n=== Stat Karakter {nama} ===")
    print(f"Attack            : {atk}/{maks}")
    print(f"Health Point      : {hp}/{maks}")
    print(f"Mana Regeneration : {mana}/{maks}")
    print(f"Skill Point       : {skill_point}/10")

    time.sleep(0.5)
    print("\nStat yang ingin ditingkatkan:")
    print("1. Attack")
    print("2. Health Point")
    print("3. Mana Regeneration")
    print("4. Selesai")

    time.sleep(0.5)
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
      
    time.sleep(0.5)
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
            print("ATK melebihi batas maksimal!")

    elif pilihan == "2":
        if hp + jumlah <= maks:
            hp += jumlah
            skill_point -= jumlah
            print("Stat HP berhasil ditingkatkan!")
        else:
            print("HP melebihi batas maksimal!")

    elif pilihan == "3":
        if mana + jumlah <= maks:
            mana += jumlah
            skill_point -= jumlah
            print("Stat Mana berhasil ditingkatkan!")
        else:
            print("Mana melebihi batas maksimal!")

b_atk = 2500
b_hp = 10000
b_mana = 2

c_atk = b_atk + (500 * atk)
c_hp1 = b_hp + (1000 * hp)
c_hp = c_hp1

c_mana = b_mana + (1 * mana)

mana_max = 100
c_mana1 = 20

magic_attack = c_atk * 2

c_shield = 0

time.sleep(1)
print(f"\n=== Stat Akhir Karakter {nama} ===")
print(f"Total ATK              : {c_atk}")
print(f"Total HP               : {c_hp1}")
print(f"Mana Regeneration      : {c_mana}")
print(f"Kapasitas Mana         : {mana_max}")
print(f"Sisa Skill Point       : {skill_point}")

bo_hp1 = 50500
bo_hp = bo_hp1
bo_shield = 0
time.sleep(0.5)
print("\n=== STATUS BOSS ===")
print(f"Boss HP: {bo_hp1}")
time.sleep(0.5)
lanjut = input(
    "\nApakah kamu siap melawan boss? (iya/tidak): "
).lower().strip()

time.sleep(0.5)
if lanjut != "iya":
    print("Pertarungan dibatalkan. Persiapkan dirimu dahulu!")
    mulai = False
else:
    print("\nMari kita lawan!")
    mulai = True

time.sleep(1)

while mulai and c_hp > 0 and bo_hp > 0:

    print("\n=== GILIRAN PEMAIN ===")
    print(f"1. Normal Attack ({c_atk} damage, 0 mana)")
    print(f"2. Magic Attack ({magic_attack} damage, 30 mana)")
    print("3. Heal (+400 HP, 20 mana)")
    print("4. Shield (+200 shield, 10 mana)")

    pilihan = input("Masukkan pilihanmu: ")

    damage = 0

    time.sleep(1)
    if pilihan == "1":
        damage = c_atk
        print(f"\n{nama} melancarkan Normal Attack!")

    elif pilihan == "2":
        if c_mana1 < 30:
            print("Mana tidak cukup!")
            continue

        c_mana1 -= 30
        damage = magic_attack
        print(f"\n{nama} melancarkan Magic Attack!")

    elif pilihan == "3":
        time.sleep(0.5)
        if c_mana1 < 20:
            print("Mana tidak cukup!")
            continue

        if c_hp >= c_hp1:
            print("HP masih penuh!")
            continue

        pemulihan = min(400, c_hp1 - c_hp)
        c_hp += pemulihan
        c_mana1 -= 20

        time.sleep(0.5)
        print(f"\n{nama} memulihkan {pemulihan} HP!")

    elif pilihan == "4":
        if c_mana1 < 10:
            print("Mana tidak cukup!")
            continue

        c_mana1 -= 10
        c_shield += 200

        print(f"\nShield {nama} bertambah 100!")

    else:
        print("Pilihan tidak valid!")
        continue

    if damage > 0:
        serap = min(bo_shield, damage)
        bo_shield -= serap

        damage_hp = damage - serap
        bo_hp = max(0, bo_hp - damage_hp)

        time.sleep(1)
        print(f"Damage diserap shield boss: {serap}")
        print(f"Damage ke HP boss: {damage_hp}")

    if bo_hp <= 0:
        print("\nBoss berhasil dikalahkan! Kamu menang!")
        break

    time.sleep(0.5)
    print("\n=== GILIRAN BOSS ===")

    aksi_boss = [
        ("Normal Attack", 500),
        ("Magic Attack", 1500),
        ("Magic Attack 2", 1600),
        ("Shield", 200)
    ]

    peluang = [30, 30, 20, 20]

    aksi, nilai = random.choices(
        aksi_boss,
        weights=peluang,
        k=1
    )[0]
    time.sleep(0.5)
    print(f"Boss melancarkan aksi: {aksi}!")

    if aksi == "Shield":
        bo_shield += nilai
        time.sleep(0.5)
        print(f"Shield boss bertambah {nilai}!")

    else:
        serap = min(c_shield, nilai)
        c_shield -= serap

        damage_hp = nilai - serap
        c_hp = max(0, c_hp - damage_hp)

        time.sleep(0.5)
        print(f"Damage diserap shield: {serap}")
        print(f"Damage ke HP kamu: {damage_hp}")

    if c_hp <= 0:
        print("\nKamu kalah! Silakan coba lagi.")
        break

    mana_sebelum = c_mana1
    c_mana1 = min(mana_max, c_mana1 + c_mana)
    mana_pulih = c_mana1 - mana_sebelum

    print(f"\nMana pulih sebesar {mana_pulih}!")

    time.sleep(0.5)
    print(f"\n=== STATUS {nama} ===")
    print(f"HP     : {c_hp}/{c_hp1}")
    print(f"Mana   : {c_mana1}/{mana_max}")
    print(f"Shield : {c_shield}")

    time.sleep(0.5)
    print("\n=== STATUS BOSS ===")
    print(f"HP     : {bo_hp}/{bo_hp1}")
    print(f"Shield : {bo_shield}")
