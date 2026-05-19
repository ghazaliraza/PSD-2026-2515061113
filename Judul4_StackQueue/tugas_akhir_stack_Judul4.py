class StackBrowserHistory:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.stack = [None] * self.MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.MAX - 1

    def push(self, website):
        if self.is_full():
            print("Histori browser penuh!")
            return

        self.top += 1
        self.stack[self.top] = website
        print(f"Website '{website}' berhasil ditambahkan ke histori.")

    def pop(self):
        if self.is_empty():
            print("Histori browser kosong!")
            return

        deleted = self.stack[self.top]
        self.top -= 1
        print(f"Histori terakhir '{deleted}' berhasil dihapus.")

    def peek(self):
        if self.is_empty():
            print("Histori browser kosong!")
            return

        print(f"Histori terakhir: {self.stack[self.top]}")

    def display(self):
        if self.is_empty():
            print("Tidak ada histori browser.")
            return

        print("DAFTAR HISTORI BROWSER ")
        for i in range(self.top, -1, -1):
            print(f"{self.top - i + 1}. {self.stack[i]}")

    def clear_history(self):
        self.top = -1
        print("Seluruh histori browser berhasil dihapus.")


def main():
    browser = StackBrowserHistory()

    pilihan = 0

    while pilihan != 6:
        print("MENU HISTORI BROWSER ")
        print("1. Tambah histori website")
        print("2. Hapus histori terakhir")
        print("3. Lihat histori terakhir")
        print("4. Tampilkan semua histori")
        print("5. Hapus semua histori")
        print("6. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            website = input("Masukkan nama website: ")
            browser.push(website)

        elif pilihan == 2:
            browser.pop()

        elif pilihan == 3:
            browser.peek()

        elif pilihan == 4:
            browser.display()

        elif pilihan == 5:
            browser.clear_history()

        elif pilihan == 6:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()