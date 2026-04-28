class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class Antrian:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_pelanggan(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        print(f"{nama} masuk antrian")

    def layani_pelanggan(self):
        if self.head is None:
            print("Antrian kosong")
        else:
            nama = self.head.nama
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            print(f"{nama} sedang dilayani")

    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong")
            return

        current = self.head
        print("Antrian sekarang:")

        while current:
            print(f"- {current.nama}")
            current = current.next


def main():
    antrian = Antrian()

    while True:
        print("MENU ANTRIAN")
        print("1. Tambah pelanggan")
        print("2. Layani pelanggan")
        print("3. Lihat antrian")
        print("4. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            nama = input("Nama pelanggan: ")
            antrian.tambah_pelanggan(nama)

        elif pilih == "2":
            antrian.layani_pelanggan()

        elif pilih == "3":
            antrian.tampilkan_antrian()

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
    