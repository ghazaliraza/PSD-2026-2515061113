class Node:
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, npm, nama):
        if root is None:
            return Node(npm, nama)

        if npm < root.npm:
            root.left = self.insert(root.left, npm, nama)
        elif npm > root.npm:
            root.right = self.insert(root.right, npm, nama)

        return root

    def search(self, root, npm):
        if root is None:
            return None

        if root.npm == npm:
            return root

        if npm < root.npm:
            return self.search(root.left, npm)

        return self.search(root.right, npm)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"NPM: {root.npm}, Nama: {root.nama}")
            self.inorder(root.right)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, npm):
        if root is None:
            return root

        if npm < root.npm:
            root.left = self.delete(root.left, npm)

        elif npm > root.npm:
            root.right = self.delete(root.right, npm)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.npm = temp.npm
            root.nama = temp.nama
            root.right = self.delete(root.right, temp.npm)

        return root


def menu():
    bst = BinarySearchTree()

    data_awal = [
        ("2515061001", "yudi"),
        ("2515061002", "namkul"),
        ("2515061003", "rustan"),
        ("2515061004", "rajuy"),
        ("2515061005", "Eko")
    ]

    for npm, nama in data_awal:
        bst.root = bst.insert(bst.root, npm, nama)

    while True:
        print("SISTEM PENCARIAN DATA MAHASISWA UNILA")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Mahasiswa berdasarkan NPM")
        print("3. Hapus Data Mahasiswa")
        print("4. Tampilkan Semua Data")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            npm = input("Masukkan NPM: ")
            nama = input("Masukkan Nama: ")
            bst.root = bst.insert(bst.root, npm, nama)
            print("Data berhasil ditambahkan.")

        elif pilih == "2":
            npm = input("Masukkan NPM yang dicari: ")
            hasil = bst.search(bst.root, npm)

            if hasil:
                print(f"Data ditemukan: {hasil.npm} - {hasil.nama}")
            else:
                print("Data tidak ditemukan.")

        elif pilih == "3":
            npm = input("Masukkan NPM yang akan dihapus: ")
            bst.root = bst.delete(bst.root, npm)
            print("Data berhasil dihapus.")

        elif pilih == "4":
            print("Daftar Mahasiswa:")
            bst.inorder(bst.root)

        elif pilih == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    menu()