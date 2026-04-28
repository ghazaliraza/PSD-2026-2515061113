a.JUDUL PROGRAM: Program Implementasi Struktur Data Dasar Python

b. Deskripsi Singkat: Program ini digunakan untuk mengelola antrian pelanggan secara terstruktur. User dapat menambahkan pelanggan ke dalam antrian, melayani pelanggan dari urutan paling depan, serta melihat daftar antrian yang sedang berlangsung. Sistem ini meniru kondisi nyata seperti antrian di kasir atau layanan publik, di mana pelanggan yang datang lebih dulu akan dilayani lebih dulu.

Program ini menerapkan algoritma struktur data linked list dengan konsep queue FIFO. Setiap data pelanggan disimpan dalam node yang saling terhubung menggunakan pointer. Operasi penambahan dilakukan di bagian belakang antrian dengan memanfaatkan pointer tail, sedangkan penghapusan dilakukan di bagian depan dengan menggeser pointer head. Pendekatan ini membuat proses tambah dan hapus data berjalan efisien tanpa perlu menggeser elemen lain.


c. Source Code: <img width="707" height="898" alt="Cuplikan layar 2026-04-28 203442" src="https://github.com/user-attachments/assets/049c517d-0ea0-4494-94f3-3e6b067dceca" />
<img width="877" height="820" alt="Cuplikan layar 2026-04-28 203453" src="https://github.com/user-attachments/assets/aea7e9d3-514e-440b-8929-d2e007f1be4c" />
<img width="918" height="792" alt="Cuplikan layar 2026-04-28 203510" src="https://github.com/user-attachments/assets/57b01c03-41de-4b6d-add0-080d26cfe788" />
<img width="516" height="93" alt="Cuplikan layar 2026-04-28 203517" src="https://github.com/user-attachments/assets/2084d95d-619d-44d4-a50e-e2fa050ca434" />

BAGIAN 1. CLASS NODE

class Node:
Mendefinisikan blueprint untuk satu elemen antrian.
def init(self, nama):
Constructor. Dipanggil saat objek Node dibuat.
self.nama = nama
Menyimpan data pelanggan dalam node.
self.next = None
Inisialisasi pointer ke node berikutnya. Nilai awal None karena belum terhubung.


BAGIAN 2. CLASS ANTRIAN

class Antrian:
Struktur utama linked list untuk mengelola antrian.
def init(self):
Constructor class.
self.head = None
Menunjuk node pertama. Ini pelanggan paling depan.
self.tail = None
Menunjuk node terakhir. Ini pelanggan paling belakang.


BAGIAN 3. TAMBAH PELANGGAN

def tambah_pelanggan(self, nama):
Fungsi untuk menambahkan pelanggan ke antrian.
new_node = Node(nama)
Membuat node baru berisi nama pelanggan.
if self.head is None:
Mengecek apakah antrian kosong.
self.head = new_node
Jika kosong, node baru jadi head.
self.tail = new_node
Sekaligus jadi tail karena hanya satu elemen.
else:
Jika antrian sudah ada isi.
self.tail.next = new_node
Node terakhir menunjuk ke node baru.
self.tail = new_node
Memperbarui tail ke node baru.
print(...)
Menampilkan konfirmasi.


BAGIAN 4. LAYANI PELANGGAN

def layani_pelanggan(self):
Fungsi untuk melayani pelanggan paling depan.
if self.head is None:
Mengecek apakah antrian kosong.
print("Antrian kosong")
Tidak ada yang bisa dilayani.
else:
Jika ada isi.
nama = self.head.nama
Ambil data pelanggan paling depan.
self.head = self.head.next
Geser head ke node berikutnya. Node lama otomatis terlepas.
if self.head is None:
Mengecek apakah setelah penghapusan antrian jadi kosong.
self.tail = None
Reset tail agar konsisten.
print(...)
Menampilkan pelanggan yang dilayani.


BAGIAN 5. TAMPILKAN ANTRIAN

def tampilkan_antrian(self):
Fungsi untuk melihat isi antrian.
if self.head is None:
Cek apakah kosong.
print("Antrian kosong")
Jika tidak ada data.
return
Hentikan fungsi.
current = self.head
Mulai traversal dari depan.
while current:
Loop sampai node terakhir.
print(current.nama)
Menampilkan data tiap node.
current = current.next
Pindah ke node berikutnya.


BAGIAN 6. MAIN PROGRAM

def main():
Fungsi utama program.
antrian = Antrian()
Membuat objek antrian.
while True:
Loop agar program terus berjalan.
print menu
Menampilkan pilihan fitur.
pilih = input(...)
Mengambil input user.
if pilih == "1":
Tambah pelanggan.
nama = input(...)
Input nama.
antrian.tambah_pelanggan(nama)
Memanggil fungsi insert.
elif pilih == "2":
Melayani pelanggan.
antrian.layani_pelanggan()
Memanggil fungsi delete.
elif pilih == "3":
Menampilkan antrian.
antrian.tampilkan_antrian()
Memanggil fungsi traversal.
elif pilih == "4":
break
Keluar dari loop.
else:
print("Pilihan tidak valid")
Validasi input.

BAGIAN 7. ENTRY POINT

if name == "main":
Mengecek apakah file dijalankan langsung.
main()
Menjalankan program utama.


d. Output Program: <img width="468" height="343" alt="Cuplikan layar 2026-04-28 204552" src="https://github.com/user-attachments/assets/944716c0-ea2a-4890-8ad9-de42f30df0a9" />
<img width="345" height="213" alt="Cuplikan layar 2026-04-28 204559" src="https://github.com/user-attachments/assets/1c548c09-3399-48c2-952a-e59693006bf0" />
<img width="336" height="108" alt="Cuplikan layar 2026-04-28 204618" src="https://github.com/user-attachments/assets/eb527f2b-255a-4129-8718-a8414eb218e8" />
<img width="371" height="366" alt="Cuplikan layar 2026-04-28 204634" src="https://github.com/user-attachments/assets/15bb9d05-8fbd-4618-9513-1cce22f17bb1" />
<img width="326" height="181" alt="Cuplikan layar 2026-04-28 204644" src="https://github.com/user-attachments/assets/8ef4dd22-b619-4f0b-ad9d-35e947e4a3c6" />
<img width="260" height="207" alt="Cuplikan layar 2026-04-28 204652" src="https://github.com/user-attachments/assets/1e1b9f3d-d408-48a9-b84c-2c7fe9df6c24" />

Program akan menampilkan menu interaktif setiap kali dijalankan. User memilih angka untuk menjalankan fitur. Output berubah sesuai aksi yang dipilih.

Saat program mulai:

Muncul menu:
Tambah pelanggan
Layani pelanggan
Lihat antrian
Keluar

Jika pilih 1:

Program meminta input nama pelanggan
Setelah input, tampil pesan:
“Nama masuk antrian”
Data masuk ke posisi paling belakang
seperti pada gambar saya memasukkan rijal dan karim sebagai contoh ke dalam antrean

Jika pilih 2:

Jika antrian kosong:
tampil “Antrian kosong”
Jika ada isi:
tampil “Nama sedang dilayani”
Data paling depan dihapus dari antrian
dari percobaan saya, fifo membuat sistem disini sebagai antrian di dunia nyata sehingga yang pertama masuk adalah yang pertama dilayani

Jika pilih 3:

Jika kosong:
tampil “Antrian kosong”
Jika ada isi:
tampil daftar nama dari depan ke belakang
Contoh:
Antrian sekarang:
rijal
karim

Jika pilih 4:

Program berhenti


e. https://youtu.be/alLX4AzLKaw
