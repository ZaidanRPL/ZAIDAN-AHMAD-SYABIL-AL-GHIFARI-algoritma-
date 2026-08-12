import sys
import time

def efek_ketik(teks, kecepatan=0.05):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()  # Untuk baris baru di akhir teks

# Menjalankan fungsi
efek_ketik("Attention, entire world!..")
time.sleep(1)
efek_ketik("Hear my proclamation..")
time.sleep(1)
efek_ketik("I am Lelouch vi Britannia, Emperor of the Holy Britannian Empire and your only ruler!..")
time.sleep(1)
efek_ketik("Schneizel has surrendered to me..")
time.sleep(1)
efek_ketik("as a result of this, I am now in control of both the Damocles and the FLEIJA weapons, and even the Black Knights no longer possess the strength to oppose me now..")
time.sleep(1)
efek_ketik("If anyone dares to oppose my supreme authority, they shall know the devastating power of the FLEIJAs.")
time.sleep(1)
efek_ketik("Those who could oppose my military rule no longer exist!.")
time.sleep(1)
efek_ketik("Yes, from this day, from this moment forward, the world belongs to me!.")
time.sleep(1)
efek_ketik("Lelouch vi Britannia commands you.")
time.sleep(1)
efek_ketik("Obey me, subjects!.")
time.sleep(1)
efek_ketik("OBEY ME, WORLD!")
time.sleep(1)
