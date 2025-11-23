from prettytable import PrettyTable

# Data login 
users = {
    "admin": "12345",
    "user": "abcde"
}

# List kosong untuk menampung data hewan
hewan = []

# Function lihat daftar hewan
def LihatHewan():
    print("\n=== Daftar Hewan ===")
    if hewan == []:
        print("Belum ada hewan di daftar.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["Nama Hewan", "Jenis", "Lama (hari)"]
        for data in hewan:
            tabel.add_row([data["nama"], data["jenis"], data["lama"]])
        print(tabel)

# Function tambah hewan 
def TambahHewan():
    try:
        nama = input("Masukkan nama hewan: ")
        jenis = input("Masukkan jenis hewan: ")
        lama = int(input("Masukkan lama penitipan (hari): "))
        hewan.append({"nama": nama, "jenis": jenis, "lama": lama})
        print(f"{nama} berhasil ditambahkan!")
    except ValueError:
        print("Lama penitipan harus berupa angka!")

# Function hapus hewan 
def HapusHewan():
    LihatHewan()
    if hewan == []:
        print("Tidak ada hewan yang bisa dihapus.")
    else:
        hapus = input("Masukkan nama hewan yang ingin dihapus: ")
        for data in hewan:
            if data["nama"] == hapus:
                hewan.remove(data)
                print(f"{hapus} berhasil dihapus!")
                break
        else:
            print(f"{hapus} tidak ada di daftar.")

# Function edit hewan 
def EditHewan():
    LihatHewan()
    if hewan == []:
        print("Tidak ada hewan yang bisa diedit.")
    else:
        HewanLama = input("Masukkan nama hewan yang ingin diganti: ")
        for data in hewan:
            if data["nama"] == HewanLama:
                try:
                    namaBaru = input("Nama hewan yang baru: ")
                    jenisBaru = input("Jenis hewan yang baru: ")
                    lamaBaru = int(input("Lama penitipan (hari): "))
                    data["nama"] = namaBaru
                    data["jenis"] = jenisBaru
                    data["lama"] = lamaBaru
                    print(f"Data {HewanLama} berhasil diganti!")
                except ValueError:
                    print("Lama penitipan harus berupa angka!")
                break
        else:
            print(f"{HewanLama} tidak ada di daftar.")

# Menu admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Daftar Hewan")
        print("2. Tambah Hewan")
        print("3. Edit Hewan")
        print("4. Hapus Hewan")
        print("5. Keluar")
        try:
            pilihan = int(input("Pilih menu (1-5): "))
            if pilihan == 1:
                LihatHewan()
            elif pilihan == 2:
                TambahHewan()
            elif pilihan == 3:
                EditHewan()
            elif pilihan == 4:
                HapusHewan()
            elif pilihan == 5:
                print("Terima kasih! Keluar dari program.")
                break
            else:
                print("Pilihan tidak tersedia!")
        except ValueError:
            print("Input harus berupa angka!")

# Menu user
def menu_user():
    while True:
        print("\n=== Menu User ===")
        print("1. Lihat Daftar Hewan")
        print("2. Tambah Hewan")
        print("3. Keluar")
        try:
            pilihan = int(input("Pilih menu (1-3): "))
            if pilihan == 1:
                LihatHewan()
            elif pilihan == 2:
                TambahHewan()
            elif pilihan == 3:
                print("Terima kasih! Keluar dari program.")
                break
            else:
                print("Pilihan tidak tersedia!")
        except ValueError:
            print("Input harus berupa angka!")

# Program utama
print("=== Sistem Manajemen Penitipan Hewan ===")

# Login
for Login in range(3):
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin":
        if password == users["admin"]:
            print("Login berhasil sebagai ADMIN")
            menu_admin()
            break
        else:
            print("Password salah!")
            continue

    elif username == "user":
        if password == users["user"]:
            print("Login berhasil sebagai USER")
            menu_user()
            break
        else:
            print("Password salah!")
            continue

    else:
        print("Username tidak ditemukan!")

else:
    print("Terlalu banyak percobaan. Program berhenti.")