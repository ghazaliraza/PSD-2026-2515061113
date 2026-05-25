## A. Judul Program: Pencarian Data Mahasiswa UNILA Berdasarkan NPM

## B. Deskripsi Singkat:
Program ini mengimplementasikan struktur data Binary Search Tree untuk menyimpan dan mencari data mahasiswa Universitas Lampung berdasarkan NPM.

BST digunakan karena memiliki efisiensi pencarian, penambahan, dan penghapusan data dengan kompleksitas rata-rata O(log n).

## C. Source Code:
<img width="1772" height="7272" alt="tugas_akhir_judul5 py" src="https://github.com/user-attachments/assets/4bff26df-8bfd-42bf-8cd2-ea9321940a76" />

class Node:
Mendefinisikan class bernama Node, yang merepresentasikan satu simpul awal (node) dalam pohon BST.

def __init__(self, npm, nama):
Method konstruktor yang dipanggil otomatis saat membuat objek Node baru. Menerima dua parameter: npm dan nama.

 self.npm = npm
Menyimpan nilai npm (Nomor Pokok Mahasiswa) ke dalam atribut node.

python        self.nama = nama
Menyimpan nilai nama mahasiswa ke dalam atribut node.

 self.left = None
Menyiapkan pointer ke anak kiri, awalnya kosong (None).

self.right = None
Menyiapkan pointer ke anak kanan, awalnya kosong (None).


class BinarySearchTree:
Mendefinisikan class utama yang berisi semua operasi BST.

def __init__(self):
Konstruktor untuk inisialisasi BST.

self.root = None
Menyiapkan root (akar pohon), awalnya kosong karena pohon belum berisi data.


pdef insert(self, root, npm, nama):
Method untuk menyisipkan node baru. Menerima root (node saat ini), npm, dan nama.

 if root is None:
return Node(npm, nama)
Jika posisi saat ini kosong, buat node baru dan kembalikan sebagai node di posisi itu.

if npm < root.npm:
root.left = self.insert(root.left, npm, nama)
Jika NPM lebih kecil dari node saat ini maka masuk ke cabang kiri (rekursif).

elif npm > root.npm:
root.right = self.insert(root.right, npm, nama)
Jika NPM lebih besar maka masuk ke cabang kanan (rekursif).

return root
Kembalikan node saat ini setelah proses insert selesai.


def search(self, root, npm):
Method untuk mencari node berdasarkan NPM.

if root is None:
return None
Jika node kosong (tidak ditemukan), kembalikan None.

if root.npm == npm:
return root
Jika NPM cocok dengan node saat ini, kembalikan node tersebut (ditemukan).

if npm < root.npm:
return self.search(root.left, npm)

Jika NPM lebih kecil maka cari di cabang kiri.

return self.search(root.right, npm)
Jika NPM lebih besar maka cari di cabang kanan.


 def inorder(self, root):
Method untuk menampilkan semua data secara terurut ascending 

if root:
Hanya diproses jika node tidak kosong.

self.inorder(root.left)
Kunjungi dulu semua node di kiri secara rekursif.

print("NPM: {root.npm}, Nama: {root.nama}")
Cetak data node saat ini.

self.inorder(root.right)
mengunjungi semua node di kanan secara rekursif.


def find_min(self, root):
Mencari node dengan NPM terkecil (paling kiri dalam pohon). Digunakan saat proses hapus.

while root.left:
 root = root.left
Terus geser ke kiri selama masih ada anak kiri.

return root
Kembalikan node paling kiri yang ditemukan (nilai terkecil).

def delete(self, root, npm):
Method untuk menghapus node berdasarkan NPM.

if root is None:
 return root
Jika node tidak ditemukan, kembalikan None.

if npm < root.npm:
root.left = self.delete(root.left, npm)
NPM lebih kecil jadi menghapus di cabang kiri.

 elif npm > root.npm:
root.right = self.delete(root.right, npm)
NPM lebih besar → hapus di cabang kanan.

else:
NPM cocok → node ini yang akan dihapus.

if root.left is None:
 return root.right
jika Node tidak punya anak kiri maka ganti dengan anak kanan.

elif root.right is None:
return root.left
jika Node tidak punya anak kanan maka ganti dengan anak kiri.

 temp = self.find_min(root.right)
jika terdapat punya dua anak maka Cari node terkecil di subtree kanan (pengganti).

root.npm = temp.npm
root.nama = temp.nama
Salin data node pengganti ke node yang dihapus.

root.right = self.delete(root.right, temp.npm)
Hapus node pengganti dari posisi aslinya di subtree kanan.

return root
Kembalikan node setelah proses hapus.


def menu():
    bst = BinarySearchTree()
Membuat objek BST baru.

 data_awal = [
        ("2515061001", "yudi"),]

Mendefinisikan data mahasiswa awal dalam bentuk list of tuple.

for npm, nama in data_awal:
        bst.root = bst.insert(bst.root, npm, nama)
Memasukkan semua data awal ke dalam BST satu per satu.

 while True:
Loop menu utama yang terus berjalan sampai user memilih keluar.

 pilih = input("Pilih menu: ")
Meminta input pilihan dari user.

if pilih == "1": ...   # Tambah data
elif pilih == "2": ... # Cari data
elif pilih == "3": ... # Hapus data
elif pilih == "4": ... # Tampilkan semua
elif pilih == "5":
break              # Keluar dari loop
else:
print("Pilihan tidak valid.")
Menjalankan operasi BST sesuai pilihan user.


pythonif __name__ == "__main__":
    menu()
Memastikan fungsi menu() hanya berjalan jika file ini dijalankan langsung (bukan di-import sebagai modul).


## D. Output:
<img width="609" height="160" alt="Cuplikan layar 2026-05-25 183709" src="https://github.com/user-attachments/assets/ee5f6013-327b-4c3a-a0e3-ceec47dd9f6b" />
<img width="545" height="237" alt="Cuplikan layar 2026-05-25 183648" src="https://github.com/user-attachments/assets/677d3a58-bf2f-45b6-879d-5631e6214483" />
<img width="694" height="240" alt="Cuplikan layar 2026-05-25 183624" src="https://github.com/user-attachments/assets/5cafdcaa-3e92-4c60-82b9-103990fa8a39" />
<img width="737" height="305" alt="Cuplikan layar 2026-05-25 183604" src="https://github.com/user-attachments/assets/3b1b4511-9166-4211-add2-a8af846680aa" />
Pada output dari program tersedia beberapa data awal npm mahasiswa. User dapat menginputkan angka 1-5

Pada output tersebut saya menambahkan data mahasiswa baru dan menghapus data salah satu mahasiswa dan juga menampilkan data setelah dihapus dan ditambah. Semua bekerja dengan baik tanpa ada error

## E. Link Youtube:




