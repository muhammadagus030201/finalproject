daftar_kontak = []

def show_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print(f"Nama : {kontak['nama']}")
        print(f"No Telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama : ")
    telepon = input("No Telepon : ")
    kontak = {
        "nama" : nama,
        "telepon" : telepon
    }
    return kontak

while True :
    print('Selamat datang!')
    print('--- Menu ---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')

    menu=input('Pilih menu: ')
    if menu == '3' :
        break
    elif menu == '1' :
        print("Daftar Kontak")
        show_kontak(daftar_kontak)
    elif menu == '2' :
        kontak = new_kontak ()
        daftar_kontak.append(kontak)
        print("Kontak berhasil ditambahkan")
    else:
        print("Menu Tidak Tersedia")

print('Program selesai, sampai jumpa!')
