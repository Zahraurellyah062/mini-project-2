from prettytable import PrettyTable


pengguna = {
    "Admin": "Admin123",
    "Pembeli": "Pembeli123"
}

transaksi = []
poin_reward = {
    "Pembeli": 0
}

reward = [
    {'NO' : 1, 'ITEM' : 'Piring', 'POIN' : 30},
    {'NO' : 2, 'ITEM' : 'Gelas', 'POIN' : 20},
    {'NO' : 3, 'ITEM' : 'Sendok', 'POIN' : 10},
    {'NO' : 4, 'ITEM' : 'Totebag', 'POIN' : 10}
]

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in pengguna and pengguna[username] == password:
        print(f"Selamat Datang, {username}!")
        return username
    else:
        print("Username tidak valid!")
        return None


def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Transaksi")
        print("2. Tambah Transaksi")
        print("3. Ubah Transaksi")
        print("4. Hapus Transaksi")
        print("5. Logout")
        print("\n===================")

        pilihan = input("Pilih opsi diatas: ")

        if pilihan == '1':
            lihat_transaksi()
        elif pilihan == '2':
            tambah_transaksi()
        elif pilihan == '3':
            ubah_transaksi()
        elif pilihan == '4':
            hapus_transaksi()
        elif pilihan == '5':
            print("Logout Berhasil!! Terima Kasih Sudah Menggunakan Program Ini!!")
            break
        else:
            print("Pilihan tidak valid! Silahkan coba lagi!")

def menu_pembeli():
    while True:
        print("\n=== Menu Pembeli ===")
        print("1. Lihat Transaksi")
        print("2. Tambah Transaksi")
        print("3. Lihat Poin Reward")
        print("4. Tukar Poin Reward")
        print("5. Logout")
        print("\n=====================")

        pilihan = input("Pilih opsi diatas: ")

        if pilihan == '1':
            lihat_transaksi()
        elif pilihan == '2':
            tambah_transaksi()
        elif pilihan == '3':
            lihat_poin_reward()
        elif pilihan == '4':
            tukar_poin_reward()
        elif pilihan == '5':
            print("Logout Berhasil!! Terima Kasih Sudah Menggunakan Program Ini!!")
            break
        else:
            print("Pilihan tidak valid! Silahkan coba lagi!")

def tabel_poin_reward():
    table = PrettyTable(["NO", "ITEM", "POIN"])
    for service in reward:
        table.add_row([service['NO'], service['ITEM'], service['POIN']])
    print(table)


item_poin = {
    '1' : 30,
    '2' : 20,
    '3' : 10,
    '4' : 10
}


def lihat_transaksi():
    if transaksi:
        print("\n=== Daftar Transaksi ===")
        for i, t in enumerate(transaksi, 1):
            print(f"{i}. {t}")
    else:
        print("Belum ada transaksi!")


def tambah_transaksi():
    detail = input("Masukkan detail transaksi yang dilakukan: ")
    transaksi.append(detail)
    poin_reward["Pembeli"] += 10 
    print("Transaksi berhasil ditambahkan!")

def lihat_poin_reward():
    print(f"Poin reward anda: {poin_reward['Pembeli']}")

def tukar_poin_reward():
    tabel_poin_reward()
    lihat_poin_reward()
    item_choice = input("Masukkan nomor item untuk ditukar (1-4): ")

    if item_choice in item_poin:
        item_points_value = item_poin[item_choice]
        if poin_reward['Pembeli'] >= item_points_value:
            poin_reward['Pembeli'] -= item_points_value
            print(f"Selamat! Anda telah mendapatkan {reward[int(item_choice) - 1]['ITEM']}!")
        else:
            print("Poin anda tidak cukup untuk menukar item ini!!")
    else:
        print("Pilihan item tidak tersedia! Silahkan coba lagi!")


def ubah_transaksi():
    lihat_transaksi()
    index = int(input("Masukkan nomor transaksi yang ingin diubah: ")) - 1
    if 0 <= index < len(transaksi):
        detail_baru = input("Masukkan detail baru: ")
        transaksi[index] = detail_baru
        print("Transaksi berhasil diubah!")
    else:
        print("Nomor transaksi tidak valid!")


def hapus_transaksi():
    lihat_transaksi()
    index = int(input("Masukkan nomor transaksi yang ingin dihapus: ")) - 1
    if 0 <= index < len(transaksi):
        del transaksi[index]
        print("Transaksi berhasil dihapus!")
    else:
        print("Nomor transaksi tidak valid!")


def main():
    while True:
        print("\n=== Login ===")
        user = login()
        if user == "Admin":
            menu_admin()
        elif user == 'Pembeli':
            menu_pembeli()


if __name__ == "__main__":
    main()