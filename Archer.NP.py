import sys
import time

def efek_ketik(teks, kecepatan=0.05):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()  # Untuk baris baru di akhir teks

# Menjalankan fungsi
efek_ketik("I am the bone of my sword.")
time.sleep(1)
efek_ketik("Steel is my body and fire is my blood.")
time.sleep(1)
efek_ketik("I have created over a thousand blades.")
time.sleep(1)
efek_ketik("Unknown to death.Nor known to life.")
time.sleep(1)
efek_ketik("Have withstood pain to create many weapons.")
time.sleep(1)
efek_ketik("Yet those hands shall never hold anything.")
time.sleep(1)
efek_ketik("So, as I pray,")
time.sleep(0.2)
efek_ketik("Unlimited")
time.sleep(0.2)
efek_ketik("Blade")
time.sleep(0.2)
efek_ketik("work")
