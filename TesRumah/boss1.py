import time
import random

c_hp1 = 10000
c_hp = c_hp1
c_mana_reg = 10
c_mana = 50
c_shield = 0

b_hp1 = 10500
b_hp = b_hp1
b_shield = 0

nama = input("Masukkan nama Anda: ")
time.sleep(1)

while c_hp > 0 and b_hp > 0:
    print("\n=== GILIRAN PEMAIN ===")
    print("1. Normal Attack (500 dmg, 0 mana)")
    print("2. Magic Attack (1000 dmg, 30 mana)")
    print("3. Heal HP (+200 HP, 20 mana)")
    print("4. Shield (+100 shield, 10 mana)")
    time.sleep(0.5)
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        damage = 500
        time.sleep(0.5)
        print(f"\n{nama} melancarkan Normal Attack!")

    elif pilihan == "2":
        if c_mana < 30:
            time.sleep(0.5)
            print("Mana tidak cukup!")
            continue

        c_mana -= 30
        damage = 1000
        time.sleep(0.5)
        print(f"\n{nama} melancarkan Magic Attack!")

    elif pilihan == "3":
        if c_mana < 20:
            time.sleep(0.5)
            print("Mana tidak cukup!")
            continue

            time.sleep(0.5)
        if c_hp >= c_hp1:
            print("HP masih penuh!")
            continue

        pemulihan = min(200, c_hp1 - c_hp)
        c_hp += pemulihan
        c_mana -= 20

        time.sleep(0.5)
        print(f"\n{nama} memulihkan {pemulihan} HP!")
        damage = 0

    elif pilihan == "4":
        if c_mana < 10:
            time.sleep(0.5)
            print("Mana tidak cukup!")
            continue

        c_mana -= 10
        c_shield += 100
        damage = 0
        time.sleep(0.5)
        print(f"\nShield {nama} bertambah 100!")

    else:
        print("Pilihan tidak valid!")
        continue

    if damage > 0:
        serap = min(b_shield, damage)
        b_shield -= serap

        damage_hp = damage - serap
        b_hp = max(0, b_hp - damage_hp)

        time.sleep(0.5)
        print(f"Damage diserap shield boss: {serap}")
        print(f"Damage ke HP boss: {damage_hp}")

    time.sleep(0.5)
    print(f"\n=== STATUS {nama} ===")
    print(f"HP: {c_hp}/{c_hp1}")
    print(f"Mana: {c_mana}")
    print(f"Shield: {c_shield}")

    time.sleep(0.5)
    print("\n=== STATUS BOSS ===")
    print(f"HP: {b_hp}/{b_hp1}")
    print(f"Shield: {b_shield}")

    if b_hp <= 0:
        print("\nBoss berhasil dikalahkan! Anda menang!")
        break

    print("\n=== GILIRAN BOSS ===")

    aksi_boss = [
        ("Normal Attack", 250),
        ("Magic Attack", 500),
        ("Magic Attack2", 600),
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
    time.sleep(0.5)

    if aksi == "Shield":
        b_shield += nilai
        time.sleep(0.5)
        print(f"Shield boss bertambah {nilai}!")

    else:
        serap = min(c_shield, nilai)
        c_shield -= serap

        damage_hp = nilai - serap
        c_hp = max(0, c_hp - damage_hp)

        time.sleep(0.5)
        print(f"Damage diserap shield: {serap}")
        print(f"Damage ke HP Anda: {damage_hp}")

    c_mana += c_mana_reg
    time.sleep(0.5)
    print(f"{nama} memulikan mana sebesar{c_mana_reg}")
    time.sleep(1)
    print(f"\n=== STATUS {nama} ===")
    print(f"HP: {c_hp}/{c_hp1}")
    print(f"Mana: {c_mana}")
    print(f"Shield: {c_shield}")
    time.sleep(0.5)
    print("\n=== STATUS BOSS ===")
    print(f"HP: {b_hp}/{b_hp1}")
    print(f"Shield: {b_shield}")


    if c_hp <= 0:
        print("\nAnda kalah! Silakan coba lagi.")
        break