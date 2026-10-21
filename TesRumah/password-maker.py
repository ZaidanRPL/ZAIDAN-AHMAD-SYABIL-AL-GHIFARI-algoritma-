import secrets
import string


def buat_password(panjang):
  karakter = string.ascii_letters + string.digits + string.punctuation

  password = "".join(secrets.choice(karakter) for _ in range(panjang))
  return password


input_panjang = int(input("Masukkan panjang password yang diinginkan: "))

if input_panjang < 6:
    print("⚠️ Peringatan: Password terlalu pendek! Disarankan minimal 8-12 karakter.")
elif input_panjang == int:
    print("❌ Masukkan harus berupa angka!")

password_baru = buat_password(input_panjang)
print(f"Password acak Anda ({input_panjang} karakter): {password_baru}")

