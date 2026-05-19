## A.  Judul Program: Program Stack Histori Browser

## B. Deskripsi Singkat: 
Program ini dibuat menggunakan struktur data Stack dengan konsep LIFO (Last In First Out). Program digunakan untuk menyimpan histori website yang dibuka pengguna dan menghapus histori terakhir yang masuk terlebih dahulu.
Operasi yang digunakan meliputi push, pop, peek, display, dan clear history.

## C. Source Code : 
<img width="1816" height="5544" alt="tugas_akhir_stack_Judul4 py" src="https://github.com/user-attachments/assets/5b97cb4c-36c1-401c-ab20-e4f1e590a6e3" />

Penjelasan kode program Stack Histori Browser secara baris per baris:

Baris 1
class StackBrowserHistory:

Membuat class bernama StackBrowserHistory. Class ini digunakan untuk mengelola histori browser menggunakan struktur data Stack.

Baris 2
def __init__(self, max_size=100):

Method constructor yang otomatis dijalankan saat objek dibuat. Parameter max_size=100 menentukan kapasitas maksimal stack.

Baris 3
self.MAX = max_size

Menyimpan kapasitas maksimum stack ke variabel MAX.

Baris 4
self.stack = [None] * self.MAX

Membuat list kosong sebanyak kapasitas maksimum stack.

Contoh:
[None, None, None, ...]

Baris 5
self.top = -1

Menandakan stack masih kosong. Nilai -1 berarti belum ada data di dalam stack.

Baris 7
def is_empty(self):

Method untuk mengecek apakah stack kosong.

Baris 8
return self.top == -1

Mengembalikan nilai True jika stack kosong.

Baris 10
def is_full(self):

Method untuk mengecek apakah stack penuh.

Baris 11
return self.top == self.MAX - 1

Jika posisi top sudah mencapai kapasitas maksimum, maka stack dianggap penuh.

Baris 13
def push(self, website):

Method push digunakan untuk menambahkan histori website ke stack.

Baris 14
if self.is_full():

Mengecek apakah stack penuh sebelum menambahkan data.

Baris 15
print("Histori browser penuh!")

Menampilkan pesan jika stack penuh.

Baris 16
return

Menghentikan proses push.

Baris 18
self.top += 1

Menambah posisi top satu langkah ke atas.

Contoh:
-1 menjadi 0

Baris 19
self.stack[self.top] = website

Menyimpan website ke posisi top.

Baris 20
print(f"Website '{website}' berhasil ditambahkan ke histori.")

Menampilkan pesan bahwa histori berhasil ditambahkan.

Baris 22
def pop(self):

Method pop digunakan untuk menghapus histori terakhir.

Baris 23
if self.is_empty():

Mengecek apakah stack kosong.

Baris 24
print("Histori browser kosong!")

Menampilkan pesan jika stack kosong.

Baris 25
return

Menghentikan proses pop.

Baris 27
deleted = self.stack[self.top]

Menyimpan histori teratas ke variabel deleted.

Baris 28
self.top -= 1

Menurunkan posisi top karena data teratas dihapus.

Baris 29
print(f"Histori terakhir '{deleted}' berhasil dihapus.")

Menampilkan histori yang berhasil dihapus.

Baris 31
def peek(self):

Method untuk melihat histori terakhir tanpa menghapusnya.

Baris 32
if self.is_empty():

Mengecek apakah stack kosong.

Baris 33
print("Histori browser kosong!")

Menampilkan pesan jika stack kosong.

Baris 34
return

Menghentikan proses peek.

Baris 36
print(f"Histori terakhir: {self.stack[self.top]}")

Menampilkan histori paling atas pada stack.

Baris 38
def display(self):

Method untuk menampilkan seluruh histori browser.

Baris 39
if self.is_empty():

Mengecek apakah stack kosong.

Baris 40
print("Tidak ada histori browser.")

Menampilkan pesan jika histori kosong.

Baris 41
return

Menghentikan proses display.

Baris 43
print("DAFTAR HISTORI BROWSER ")

Menampilkan judul daftar histori.

Baris 44
for i in range(self.top, -1, -1):

Perulangan dari data paling atas sampai paling bawah.

Contoh:
range(3, -1, -1)

Artinya:
3, 2, 1, 0

Baris 45
print(f"{self.top - i + 1}. {self.stack[i]}")

Menampilkan isi histori browser satu per satu.

Baris 47
def clear_history(self):

Method untuk menghapus semua histori browser.

Baris 48
self.top = -1

Mengosongkan stack dengan mengembalikan top ke -1.

Baris 49
print("Seluruh histori browser berhasil dihapus.")

Menampilkan pesan bahwa semua histori telah dihapus.

Baris 52
def main():

Function utama program.

Baris 53
browser = StackBrowserHistory()

Membuat objek stack bernama browser.

Baris 55
pilihan = 0

Variabel untuk menyimpan menu pilihan pengguna.

Baris 57
while pilihan != 6:

Perulangan menu selama pengguna belum memilih keluar.

Baris 58
print("MENU HISTORI BROWSER ")

Menampilkan judul menu.

Baris 59 sampai 64
print("1. Tambah histori website")
print("2. Hapus histori terakhir")
print("3. Lihat histori terakhir")
print("4. Tampilkan semua histori")
print("5. Hapus semua histori")
print("6. Keluar")

Menampilkan daftar menu program.

Baris 66
try:

Digunakan untuk menangani error input.

Baris 67
pilihan = int(input("Masukkan pilihan: "))

Menerima input menu dari pengguna dalam bentuk angka.

Baris 68
except ValueError:

Menangkap error jika input bukan angka.

Baris 69
print("Input harus berupa angka!")

Menampilkan pesan kesalahan.

Baris 70
continue

Mengulang menu dari awal.

Baris 72
if pilihan == 1:

Jika pengguna memilih menu 1.

Baris 73
website = input("Masukkan nama website: ")

Meminta input nama website.

Baris 74
browser.push(website)

Menambahkan website ke stack.

Baris 76
elif pilihan == 2:

Jika pengguna memilih menu 2.

Baris 77
browser.pop()

Menghapus histori terakhir.

Baris 79
elif pilihan == 3:

Jika pengguna memilih menu 3.

Baris 80
browser.peek()

Melihat histori terakhir.

Baris 82
elif pilihan == 4:

Jika pengguna memilih menu 4.

Baris 83
browser.display()

Menampilkan seluruh histori browser.

Baris 85
elif pilihan == 5:

Jika pengguna memilih menu 5.

Baris 86
browser.clear_history()

Menghapus seluruh histori.

Baris 88
elif pilihan == 6:

Jika pengguna memilih keluar.

Baris 89
print("Program selesai.")

Menampilkan pesan program selesai.

Baris 91
else:

Jika input menu tidak tersedia.

Baris 92
print("Pilihan tidak valid!")

Menampilkan pesan kesalahan pilihan.

Baris 95
if __name__ == "__main__":

Mengecek apakah file dijalankan langsung.

Baris 96
main()

Menjalankan function utama program.


## D. Output Program
<img width="524" height="451" alt="Cuplikan layar 2026-05-19 210621" src="https://github.com/user-![Uploading Cuplikan layar <img width="523" height="455" alt="Cuplikan layar 2026-05-19 211456" src="https://github.com/user-attachments/assets/b598493b-c3f1-41d3-b99e-897f57520b3a" /><img width="395" height="240" alt="Cuplikan layar 2026-05-19 211505" src="https://github.com/user-attachments/assets/1f724243-9047-4ff4-b0fc-eec7524755e4" />
<img width="519" height="450" alt="Cuplikan layar 2026-05-19 211425" src="https://github.com/user-attachments/assets/6d47d59c-bce8-43b7-a8f8-3c6d02c3ea99" />
<img width="623" height="729" alt="Cuplikan layar 2026-05-19 211411" src="https://github.com/user-attachments/assets/36ef2d00-2752-461e-a197-5154894b56b1" />


pada output program ini terdapat beberapa pilihan untuk user yaitu
1. Tambah histori website
2. Hapus histori terakhir
3. Lihat histori terakhir
4. Tampilkan semua histori
5. Hapus semua histori
6. Keluar

ketika menambahkan histori pada pilihan 1 maka data akan dimasukkan dengan prinsip sistem LIFO (Last In First Out), lalu data akan ditambah terus menerus maksimal 100 sesuai keinginan user. Ketika user menghapus histori terakhir disitulah prinsip LIFO bekerja. Lalu lihat histori terakhir akan menampilkan histori terakhir agar kita tahu histori yang akan kita hapus. Lalu ada tampilkan semua histori dan hapus semua histori


pada foto yang saya berikan saya menambahkan beberapa histori website lalu menghapus bagian terakhir dan seluruhnya, lalu saya mencoba semua opsinya dan semuanya bekerja normal. serta ketika saya memasukan angka yang tidak sesuai akan ter print input tidak valid.

## E. Link Youtube:
https://youtu.be/9yysMIRb4Ys



