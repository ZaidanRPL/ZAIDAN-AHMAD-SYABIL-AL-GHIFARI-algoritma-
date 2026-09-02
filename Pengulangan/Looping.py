for i in range (0, -101, -10):
    print(i, end=" ")

for i in range (0, 101, 10):
    print(i, end="")                                  

print("===================================")

a = "seseorang"
b = 3

print("Anda memiliki 3 kesempatan mengisi.")
nama = str(input("Masukan nama:"))
while b > 0:
    c = str(input("Masukan password: "))


    if c == a:
        print("Password benar.")
        break
    else:
        b -= 1
        if b >= 1:
            print (f"Ulang lagi,kesempatan anda masi ada {b}.")
        

if b == 0:
    print(f"\nMaaf ya {nama}, password anda salah.")
else:
    print("Password anda benar.")

