## A. Judul Program: Sistem Kasir Minimarket Berbasis Hash Map

## B. Deskripsi Singkat:
Program ini adalah sistem manajemen kasir minimarket sederhana yang dirancang untuk melakukan penyimpanan, pembaruan, pencarian, dan penghapusan data barang secara efisien. Masalah utama dalam sistem kasir konvensional sering kali terletak pada kecepatan pencarian item barang ketika transaksi sedang berlangsung. Dengan menggunakan struktur data Hash Map, program ini mampu mengoptimalkan waktu pencarian data barang menjadi lebih cepat dibandingkan pencarian linear biasa.

Algoritma struktur data yang diterapkan dalam program ini adalah Hash Map dengan metode penanganan kolisi (collision handling) berupa Chaining menggunakan Singly Linked List. Fungsi hash memetakan ID barang (key_id) ke dalam indeks array (slot memori) tertentu. Jika terjadi kolisi atau beberapa ID barang menghasilkan indeks slot yang sama, data akan ditambahkan sebagai node baru dalam rantai linked list pada slot tersebut.

## C. Source Code:
<img width="2366" height="8406" alt="tugas_akhir_judul6 py" src="https://github.com/user-attachments/assets/92855a38-9497-45d8-b85d-c1f0e323772a" />
class Node: 
Mendeklarasikan sebuah kelas baru bernama Node. Kelas ini bertindak sebagai kontainer cetak biru (blueprint) untuk menyimpan objek data barang terpisah di dalam memori.

def __init__(self, key_id, nama_barang, harga): 
Fungsi  yang otomatis berjalan saat objek Node baru dibuat. Fungsi ini menerima tiga buah parameter masukan: ID barang, nama barang, dan harganya.

self.key_id = key_id 
Menyimpan nilai parameter key_id (berupa angka unik) ke dalam variabel internal atribut objek node tersebut sebagai kunci pengidentifikasi.

self.nama_barang = nama_barang 
Menyimpan string nama produk ke dalam variabel internal atribut nama_barang.

self.harga = harga Menyimpan 
nilai nominal harga produk ke dalam variabel internal atribut harga.

self.next = None 
Menginisialisasi pointer penunjuk next dengan nilai awal None (kosong). Pointer ini nantinya berfungsi memegang alamat node barang berikutnya yang berada di dalam slot tabel hash yang sama.

class Hash_Map_Minimarket: 
Mendeklarasikan kelas utama tempat seluruh logika operasi Hash Map (tambah, cari, hapus, tampilkan) dikelola.

def __init__(self, size=10): 
Konstruktor objek tabel hash dengan parameter opsional size yang bernilai default 10 jika pengguna tidak mendefinisikan ukurannya secara manual.

self.SIZE = size 
Menyimpan ukuran kapasitas array tabel ke dalam atribut internal global kelas (self.SIZE).

self.table = [None] * self.SIZE 
Membuat struktur array (list Python) kosong sepanjang ukuran self.SIZE (10 elemen) yang diisi seluruhnya dengan nilai None. Array ini bertindak sebagai wadah internal memori.

def hash_function(self, key_id): 
Mendefinisikan fungsi matematika komputasi untuk mengubah angka ID produk acak menjadi indeks array lokal yang valid.

return (key_id % self.SIZE + self.SIZE) % self.SIZE 
Rumus matematika fungsi hash. Operasi modulo pertama (key_id % self.SIZE) mencari sisa hasil bagi. Penambahan + self.SIZE dan modulo kedua dilakukan sebagai langkah preventif (defensive programming) untuk memastikan hasil indeks selalu bernilai positif dan berada di rentang angka indeks array 0 sampai size - 1 (0 hingga 9), sekalipun input ID bernilai negatif.

def tambah_atau_update_barang(self, key_id, nama_barang, harga): 
Mendeklarasikan fungsi entri data baru yang menerima parameter berupa ID, nama barang, dan harga.

index = self.hash_function(key_id) 
Memanggil hash_function untuk menghitung dan menentukan di nomor indeks array mana (0-9) data barang ini seharusnya diletakkan atau dicari.

current = self.table[index]
Membuat pointer bantuan bernama current yang diarahkan langsung menunjuk ke baris pertama elemen linked list yang ada pada self.table[index].

while current is not None: 
Melakukan perulangan kondisi. Selama current tidak menunjuk ke ruang kosong (None), program akan terus menelusuri rantai linked list di dalam slot tersebut satu per satu.

if current.key_id == key_id: 
Melakukan validasi pengecekan. Jika ID produk pada node yang sedang diperiksa saat ini (current.key_id) sama persis dengan key_id masukan pengguna, berarti data ini sudah pernah terdaftar sebelumnya.

current.nama_barang = nama_barang 
(Kondisi True) Memperbarui string nama barang lama dengan nama barang baru yang diinput.

current.harga = harga 
(Kondisi True) Memperbarui nilai nominal harga produk lama dengan nilai harga baru.


return 
Mencetak pesan sukses ke layar dan langsung keluar menghentikan eksekusi fungsi seluruhnya agar tidak melanjutkan baris kode di bawahnya.

current = current.next 
Jika ID tidak cocok pada node tersebut, geser posisi pointer current maju selangkah ke node berikutnya di dalam rantai.

new_node = Node(key_id, nama_barang, harga) 
Baris ini hanya dieksekusi jika perulangan while selesai dan tidak menemukan ID yang sama (data benar-benar baru). Program membuat objek instansiasi Node baru di memori.

new_node.next = self.table[index] 
Menghubungkan pointer next dari data baru tersebut agar menunjuk ke elemen yang saat ini sedang menempati posisi terdepan di dalam slot array tersebut. Ini mengimplementasikan teknik penyisipan di depan (insert at head).

self.table[index] = new_node 
Memindahkan posisi kepala slot array self.table[index] agar sekarang resmi menunjuk ke objek new_node yang baru saja dimasukkan. Data baru kini berada di urutan terdepan.

def cek_harga_barang(self, key_id): 
Mendefinisikan fungsi pencarian yang menerima input parameter key_id barang yang dicari.

index = self.hash_function(key_id) 
Mencari lokasi pasti di slot indeks mana barang tersebut disimpan menggunakan fungsi hash secara instan.

current = self.table[index] 
Mengatur pointer current untuk mulai memeriksa dari ujung paling depan rantai linked list pada indeks hasil kalkulasi hash.

while current is not None: 
Melakukan perulangan untuk menelusuri rantai linked list dari depan ke belakang selama isi node tidak kosong.

if current.key_id == key_id: 
Memeriksa apakah node yang sedang dilewati memiliki ID yang dicari.

return current 
Jika ID cocok, kembalikan (return) seluruh objek Node tersebut ke pemanggil fungsi agar data nama dan harganya bisa dibaca. Eksekusi fungsi selesai.

current = current.next 
Jika tidak cocok, geser penunjuk objek current ke rantai berikutnya.

return None 
Jika perulangan while berakhir tetapi program tidak menemukan ID yang cocok hingga ujung rantai, fungsi mengembalikan nilai None (artinya barang tidak ditemukan).

def hapus_barang(self, key_id): 
Mendefinisikan fungsi penghapusan item barang berdasarkan variabel key_id.

index = self.hash_function(key_id) 
Mendapatkan nomor indeks slot array tempat barang tersebut berada melalui fungsi kalkulasi hash.

current = self.table[index] 
Pointer current diletakkan di kepala rantai linked list pada indeks tersebut untuk memulai pelacakan.

prev = None 
Membuat pointer bantuan kedua bernama prev (singkatan dari previous) dengan nilai awal None. Pointer ini berfungsi merekam jejak alamat node tepat di belakang current.


while current is not None: 
Melakukan iterasi penyusuran sepanjang rantai linked list pada slot indeks tersebut.

if current.key_id == key_id: 
Mengecek apakah ID pada node current adalah target ID yang ingin dihapus.

if prev is None: 
(Kondisi True) Jika prev masih bernilai None, artinya data yang akan dihapus berada di urutan paling pertama/kepala dari linked list di slot tersebut.

self.table[index] = current.next 
Memindahkan pointer utama slot tabel langsung menunjuk ke node kedua (current.next), sehingga node pertama terputus dari tabel (terhapus).

else: 
(Kondisi False) Jika prev tidak bernilai None, artinya data yang akan dihapus berada di tengah atau di ujung akhir rantai linked list.

prev.next = current.next 
Memutus node current dari rantai dengan cara melompati current. Pointer next dari node sebelumnya (prev.next) dihubungkan langsung ke node setelah current (current.next).

return True 
Mengembalikan nilai boolean True ke fungsi utama sebagai indikator bahwa proses penghapusan berhasil dilakukan, sekaligus menghentikan fungsi.

prev = current dan current = current.next 
Jika belum cocok, geser kedua pointer secara beriringan: prev menempati posisi current saat ini, lalu current maju ke node berikutnya.

return False 
Dijalankan jika perulangan selesai tanpa menemukan data. Mengembalikan nilai False yang berarti data gagal dihapus karena tidak ada di sistem.

def tampilkan_database_kasir(self): 
Mendefinisikan fungsi cetak visualisasi database internal kasir.


for i in range(self.SIZE): 
Melakukan perulangan sebanyak ukuran tabel hash (0 hingga 9) untuk memproses tiap slot satu demi satu.

print(f"Slot [{i}]: ", end="") 
Mencetak label nomor urut slot memori yang sedang diproses. Argumen end="" menahan agar output cetakan berikutnya tetap berada di baris yang sama (tidak berpindah baris baru).

current = self.table[i] 
Meletakkan pointer current di awal rantai linked list pada indeks ke-i.

if current is None: 
Memeriksa jika isi slot tabel tersebut kosong tidak memiliki data terikat.

print("EMPTY") (Kondisi True) Mencetak kata "EMPTY" yang menandakan slot array tersebut bersih dari data barang.

else: 
(Kondisi False) Jika slot tersebut berisi satu atau lebih node data barang.

while current is not None: 
Melakukan perulangan untuk menelusuri rantai linked list dari awal hingga ujung akhir rantai pada slot tersebut.

print(f"[ID:{current.key_id} | ... ] ", end="") 
Mencetak spesifikasi data barang (ID, nama, dan harga) ke layar dalam format grafis rantai

current = current.next 
Menggeser pointer current maju ke node berikutnya dalam rantai agar perulangan terus berjalan.

print("NONE") Setelah keluar dari while (mencapai ujung rantai), cetak string "NONE" untuk menandakan akhir dari jalur linked list pada baris slot tersebut.


def main(): 
Mendefinisikan fungsi utama pengendali alur eksekusi aplikasi program saat pertama kali dihidupkan.

kasir_store = Hash_Map_Minimarket(size=10) 
Membuat objek instansiasi baru bernama kasir_store dari kelas Hash_Map_Minimarket dengan batasan memori 10 slot.

kasir_store.tambah_atau_update_barang(...) 
Memasukkan data barang bawaan awal pabrik secara otomatis ke dalam memori sistem (kasir_store) agar database tidak dalam kondisi kosong saat pertama kali dibuka.

while True:
Membuat struktur perulangan tak terbatas (infinite loop) agar menu kasir terus menerus muncul kembali di layar setelah user selesai menjalankan suatu aksi operasi, sampai user memilih menu keluar secara manual.

print(...) 
Mencetak teks daftar menu pilihan layanan kasir angka 1 sampai 5 ke terminal.

pilihan = input(...).strip() 
Menerima ketikan string masukan opsi dari pengguna melalui keyboard, lalu fungsi .strip() otomatis membersihkan spasi liar di ujung kiri dan kanan karakter inputan tersebut.

if pilihan == "1": 
Kondisi jika user memilih menu nomor 1 untuk menambah atau memperbarui data barang.

try: 
Membuka blok error handling untuk mengantisipasi kesalahan tipe data inputan dari user yang bisa membuat program crash.

key_id = int(input(...)) 
Meminta user menginput ID barang dan langsung mengonversinya dipaksa menjadi tipe integer (int).

nama_barang = input(...).strip() 
Meminta user menginput nama barang dalam bentuk teks biasa.

harga = int(input(...)) 
Meminta user menginput harga barang dan langsung mengonversinya menjadi tipe integer (int).

if nama_barang == "": 
Validasi pengaman. Jika user langsung menekan enter tanpa mengetik nama produk (string kosong).

print(...) dan continue
Menampilkan peringatan dan langsung melompati sisa kode di bawahnya menggunakan perintah continue untuk langsung kembali melompat ke awal perulangan while True (menu utama).

kasir_store.tambah_atau_update_barang(...) 
Jika input lolos validasi, panggil fungsi entri data pada objek kelas hash map.

except ValueError: 
 Jika proses konversi int() gagal (misal user mengetik huruf saat diminta memasukkan angka ID atau Harga). Program tidak akan mati, melainkan dialihkan ke baris cetak pesan error di bawahnya.

 elif pilihan == "2": 
 Kondisi jika pengguna memilih menu ke-2 untuk mencari data harga barang.

id_dicari = int(input(...)) Meminta input ID barang yang ingin dicari/di-scan dan dikonversi ke tipe data numerik integer.

barang = kasir_store.cek_harga_barang(id_dicari) 
Memanggil fungsi pencarian pada hash map dan menampung hasilnya ke dalam variabel lokal bernama barang. Hasilnya bisa berupa objek Node atau bernilai None.

if barang is not None: 
Pengecekan hasil. Jika variabel barang sukses membawa data objek Node.

print(...) 
Mencetak atribut internal objek tersebut berupa ID produk, nama produk, dan harganya secara detail ke terminal kasir.

else: 
Jika isi variabel barang terbukti bernilai None, program mencetak informasi peringatan bahwa ID tersebut tidak terdaftar di sistem database minimarket.

except ValueError: 
Menangkap kesalahan penulisan jika input ID pencarian bukan merupakan karakter angka numerik yang valid.

elif pilihan == "3": 
Kondisi jika pengguna memilih opsi menu nomor 3 untuk menghapus data item barang dari sistem.

id_hapus = int(input(...)) 
Membaca input ID target yang ingin dimusnahkan dari memori, dikonversi menjadi tipe data integer.

if kasir_store.hapus_barang(id_hapus): 
Memanggil fungsi hapus_barang. Karena fungsi tersebut mengembalikan nilai boolean, baris ini sekaligus mengecek: jika menghasilkan nilai True, maka baris cetak [SUKSES] langsung dieksekusi.

else: 
Jika fungsi hapus mengembalikan nilai False (data tidak ada sejak awal), program mencetak notifikasi [ERROR] bahwa produk gagal dihapus karena tidak ditemukan.

except ValueError: 
Mengamankan program agar tidak mati seandainya user salah mengetik karakter non-angka pada kolom input penghapusan.

elif pilihan == "4": 
Kondisi jika user memilih menu ke-4. Program langsung memicu fungsi internal tampilkan_database_kasir() untuk membedah peta visual memori rantai tabel hash saat ini ke layar terminal.

elif pilihan == "5": 
Kondisi jika user memilih menu nomor 5 untuk menyudahi pemakaian program kasir.

print(...) dan break Mencetak salam penutup perpisahan, lalu perintah break menghentikan paksa perulangan utama while True. Program selesai berjalan secara bersih.

else: 
Kondisi pamungkas (fallback) jika string inputan menu dari user tidak cocok dengan opsi "1", "2", "3", "4", ataupun "5" (misalnya user menginput huruf "A" atau angka "9").

if __name__ == "__main__": 
Kondisi khusus di Python untuk memastikan bahwa file skrip kode program ini dieksekusi secara langsung oleh pengguna (direct run), bukan karena diimpor (import) sebagai modul oleh file skrip eksternal lain.

main() 
Jika kondisi terpenuhi, fungsi utama main() langsung dipanggil untuk menghidupkan seluruh ekosistem program kasir minimarket dari awal.



## D. Output
<img width="679" height="585" alt="Cuplikan layar 2026-06-08 085920" src="https://github.com/user-attachments/assets/5871049e-531e-4261-ac05-a2ff99d83875" />
<img width="776" height="546" alt="Cuplikan layar 2026-06-08 085856" src="https://github.com/user-attachments/assets/c1a7dfc8-7fc6-4941-9246-f169b29bfe73" />
<img width="1140" height="573" alt="Cuplikan layar 2026-06-08 085838" src="https://github.com/user-attachments/assets/2ad1ac4b-75b0-4137-a07b-d32de54dd9a3" />
<img width="689" height="579" alt="Cuplikan layar 2026-06-08 085750" src="https://github.com/user-attachments/assets/2ae36615-50ab-40b3-a65e-bd205fc09b03" />
<img width="781" height="553" alt="Cuplikan layar 2026-06-08 085716" src="https://github.com/user-attachments/assets/df7be770-1ac2-4607-bbf2-64e0c6167508" />

Inisialisasi & Menu Awal: Program akan langsung mendaftarkan dua barang awal secara otomatis ("Susu Kotak UHT" dan "Mie Instan Goreng") dan menampilkan menu utama kasir dengan 5 opsi pilihan.

Pilihan 1 (Tambah/Update): Ketika menginput data baru dengan ID yang menempati slot hash yang sama, program akan sukses menyimpannya dalam bentuk rantai (kolisi berhasil ditangani). Jika memasukkan ID baru maka data barang otomatis terupdate.

Pilihan 2 (Scan/Cek Harga): Memasukkan ID barang akan langsung memicu fungsi pencarian hash. Jika terdaftar, spesifikasi produk langsung dicetak ke layar komputer.

Pilihan 3 (Hapus): Menghapus data berdasarkan ID akan memperbarui susunan pointer rantai linked list di dalam slot memori internal.

Pilihan 4 (Lihat Data): Menampilkan visualisasi slot peta memori dari indeks Slot [0] hingga Slot [9] beserta status keterisiannya (EMPTY atau visualisasi rantai data [ID | Nama | Harga] -> NONE).



