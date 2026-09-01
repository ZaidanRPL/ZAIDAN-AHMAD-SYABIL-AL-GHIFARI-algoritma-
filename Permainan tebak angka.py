import random

jawaban = random.randint(1, 10)
kesempatan = 3

print("Mari Bung/Mbak kita bermain permainan simpel yaitu tebak angka")
print("Cara bermain: Saya akan mengacak angka dari 1-10, anda memiliki kesempatan menjawab 3 kali")

nama = input("Masukkan nama anda terlebih dahulu: ")

while kesempatan > 0:
    hasil = int(input(f"\nMasukkan tebakan anda {nama}, dan berdoalah itu benar: "))

    if hasil == jawaban:
        print(f"Yoo! Selamat {nama}, insting anda tepat, patut diacungi jempol!")
        break

    else:
        kesempatan -= 1
        print(f"Ya... maaf {nama}, anda gagal.")
        print(f"Kesempatan anda masih ada {kesempatan}")

        if kesempatan > 0:
            print(f"Mari coba lagi {nama}, saya beri petunjuk.")

            if hasil > jawaban:
                print(f"Angkanya lebih kecil dari jawaban anda, coba pikirkan secara logika {nama}.")
            else:
                print(f"Angkanya lebih besar dari jawaban anda, coba pikirkan secara logika {nama}.")

if kesempatan == 0:
    print(f"\nMaaf ya {nama}, anda harus coba lagi entah nanti, besok, maupun kapanpun.")
    print(f"Jawaban aslinya adalah {jawaban}.")
else:
    print("Permainan selesai. 👍")