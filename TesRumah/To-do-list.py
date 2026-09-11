todo = []

while true:
  print("===To Do List===")
  print("1.Tambah Tugas")
  print("2.Lihat Tugas")
  print("3.Hapus Tugas")
  print("4.Keluar")

  pilihan = input("Masukan Perintah(nomer urut)")

  if pilihan == "1":
    tugas=(input("Masukan Tugas Baru:"))
    todo.append(tugas)
    print("Selamat Tugas Baru Telah Ditambahkan!!,entah jadi kesenangan atau kesedihan")

  elif pilihan == "2":
    print("\n Daftar Tugas Anda")

    if len(todo) == 0:
      print("Maaf belum ada tugas,isi dulu gih")
    else:
      for i,tugas in enumerate(todo,1):
        print(f"{f}.{tugas}")

  elif pilihan == "3":
    if len(todo) == 0:
      print("Tidak ada tugas yang bisa dihapus,isi dulu gih")
      else:
      for i,tugas in enumerate(todo,1):
        print(f"{f}.{tugas}")
      
      nomor=(input("Masukan nomer tugas yang ingin anda hapus,entah dah kelar atau gimana juga gak tau:"))
    
    if 1 <= nomor <= len(todo):
      todo.pop(nomor -1)

      print("Tugas berhasil dihapus!,satu masalah hilang..mapakah nanti nambah lagi??")
    else:
      print("Mau hapus apaan kalau emang gak ada?,lupa kah?")

  elif pilihan == "4":
    print("Oke gak jadi ngecek ni?")
    print("Bu-bukannya aku ma-mau dicek yah")
    print("HMPH!!!")

