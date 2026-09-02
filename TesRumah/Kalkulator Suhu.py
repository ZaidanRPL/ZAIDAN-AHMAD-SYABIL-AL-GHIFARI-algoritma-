from tkinter import *

PASSWORD = "12345"

def cek_password():
    if entry.get() == PASSWORD:
        tampilkan_gambar("images (16).jpeg", "Password Benar")
    else:
        tampilkan_gambar("images (19).jpeg", "Password Salah")

def tampilkan_gambar(file_gambar, judul):
    window = Toplevel(root)
    window.title(judul)

    gambar = PhotoImage(file=file_gambar)

    label = Label(window, image=gambar)
    label.image = gambar   # Agar gambar tidak hilang
    label.pack()

root = Tk()
root.title("Login Password")
root.geometry("300x150")

Label(root, text="Masukkan Password").pack(pady=10)

entry = Entry(root, show="*")
entry.pack()

Button(root, text="Cek Password", command=cek_password).pack(pady=10)

root.mainloop()