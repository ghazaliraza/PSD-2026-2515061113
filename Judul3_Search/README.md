## A. Judul Program
Pencarian Nomor Urut Mahasiswa UNILA Menggunakan Binary Search

## B. Deskripsi Singkat
Program ini digunakan untuk mencari nomor NPM mahasiswa Universitas Lampung menggunakan algoritma Binary Search. Data NPM disimpan dalam bentuk array yang sudah terurut secara menaik agar proses pencarian dapat dilakukan dengan cepat dan efisien.

Algoritma Binary Search bekerja dengan membagi data menjadi dua bagian secara terus menerus sampai data yang dicari ditemukan. Program ini menerapkan konsep searching pada struktur data dengan kompleksitas waktu O(log n), sehingga lebih cepat dibandingkan Sequential Search untuk data berukuran besar.

## C. Source Code
<img width="1752" height="3870" alt="tugas_akhir_judul3 py" src="https://github.com/user-attachments/assets/55c76d89-c610-4041-9ba8-21b6121cfeaa" />
FUNGSI binary_search(data, target)

Baris: def binary_search(data, target):
Mendefinisikan fungsi bernama binary_search dengan 2 parameter, yaitu data (list yang akan dicari) dan target (nilai yang ingin ditemukan).

Baris: kiri = 0
Menetapkan variabel kiri sebagai batas pencarian sebelah kiri, dimulai dari indeks 0 yaitu elemen pertama list.

Baris: kanan = len(data) - 1
Menetapkan variabel kanan sebagai batas pencarian sebelah kanan, yaitu indeks terakhir list yang dihitung dari panjang list dikurangi 1.

Baris: while kiri <= kanan:
Memulai perulangan yang akan terus berjalan selama batas kiri belum melewati batas kanan, artinya masih ada elemen yang bisa diperiksa.

Baris: tengah = (kiri + kanan) // 2
Menghitung indeks tengah dari rentang pencarian yang aktif saat ini menggunakan operasi pembagian bulat (//) agar hasilnya selalu berupa bilangan bulat.

Baris: print(f"Indeks tengah: {tengah}") dan print(f"Data tengah: {data[tengah]}")
Menampilkan posisi indeks tengah dan nilai elemen pada indeks tersebut ke layar. Baris ini berfungsi sebagai visualisasi proses pencarian agar dapat diikuti langkah demi langkah.

Baris: if data[tengah] == target:
Memeriksa apakah nilai elemen di indeks tengah sama persis dengan nilai target yang dicari.

Baris: return tengah
Jika kondisi di atas terpenuhi, fungsi langsung mengembalikan nilai indeks tengah sebagai tanda bahwa target berhasil ditemukan.

Baris: elif data[tengah] < target:
Jika nilai elemen tengah lebih kecil dari target, maka target dipastikan berada di bagian kanan dari posisi tengah saat ini.

Baris: print("Pindah ke bagian kanan")
Menampilkan informasi ke layar bahwa pencarian dilanjutkan ke bagian kanan.

Baris: kiri = tengah + 1
Memindahkan batas kiri ke satu posisi setelah indeks tengah, sehingga separuh kiri dari list diabaikan dan pencarian difokuskan ke bagian kanan.

Baris: else:
Jika nilai elemen tengah lebih besar dari target, maka target dipastikan berada di bagian kiri dari posisi tengah saat ini.

Baris: print("Pindah ke bagian kiri")
Menampilkan informasi ke layar bahwa pencarian dilanjutkan ke bagian kiri.

Baris: kanan = tengah - 1
Memindahkan batas kanan ke satu posisi sebelum indeks tengah, sehingga separuh kanan dari list diabaikan dan pencarian difokuskan ke bagian kiri.

Baris: return -1
Jika perulangan selesai dan target tidak pernah ditemukan, fungsi mengembalikan nilai -1 sebagai penanda bahwa target tidak ada di dalam list.

FUNGSI main()

Baris: npm_mahasiswa = [2515061001, ..., 2515061139]
Mendefinisikan list bernama npm_mahasiswa yang berisi 15 data NPM mahasiswa. Data ini sudah tersusun secara terurut dari kecil ke besar (ascending), yang merupakan syarat mutlak agar algoritma Binary Search dapat bekerja dengan benar.

Baris: print("DATA NPM MAHASISWA UNILA") dan print(npm_mahasiswa)
Menampilkan judul dan seluruh isi list NPM ke layar agar pengguna dapat melihat data yang tersedia.

Baris: while True:
Memulai perulangan tanpa batas yang akan terus berjalan sampai ada perintah break di dalamnya. Perulangan ini digunakan untuk memvalidasi input dari pengguna.

Baris: try:
Memulai blok percobaan. Kode di dalam blok ini akan dijalankan dan jika terjadi kesalahan, program tidak akan berhenti melainkan akan ditangani oleh blok except.

Baris: target = int(input("Masukkan NPM yang ingin dicari: "))
Menampilkan pesan ke layar dan meminta pengguna memasukkan NPM yang ingin dicari. Input yang diterima kemudian dikonversi menjadi tipe data integer menggunakan int().

Baris: break
Jika konversi ke integer berhasil tanpa error, maka perintah break dijalankan untuk keluar dari perulangan while True dan melanjutkan program.

Baris: except ValueError:
Jika konversi ke integer gagal karena pengguna memasukkan karakter selain angka, maka kesalahan ValueError ditangkap di sini sehingga program tidak crash.

Baris: print("Input harus berupa angka!")
Menampilkan pesan peringatan ke layar dan perulangan kembali ke atas untuk meminta input ulang dari pengguna.

Baris: hasil = binary_search(npm_mahasiswa, target)
Memanggil fungsi binary_search dengan mengirimkan list npm_mahasiswa dan nilai target sebagai argumen. Nilai yang dikembalikan oleh fungsi (berupa indeks atau -1) disimpan dalam variabel hasil.

Baris: if hasil != -1:
Memeriksa apakah nilai hasil bukan -1, yang berarti target berhasil ditemukan di dalam list.

Baris: print(f"NPM ditemukan pada indeks ke-{hasil}")
Jika target ditemukan, menampilkan pesan ke layar beserta posisi indeks tempat NPM tersebut berada.

Baris: else:
Kondisi yang dijalankan jika nilai hasil adalah -1.

Baris: print("NPM tidak ditemukan")
Menampilkan pesan ke layar bahwa NPM yang dicari tidak ada di dalam list.

Baris: if name == "main": main()
Baris ini memastikan bahwa fungsi main() hanya dijalankan ketika file ini dieksekusi langsung oleh Python, bukan ketika file ini diimpor sebagai modul oleh program lain.


## D. Output
<img width="1819" height="393" alt="Cuplikan layar 2026-05-11 214441" src="https://github.com/user-attachments/assets/46805b23-0062-48b0-9fa6-58551fcec5c8" />
<img width="1831" height="491" alt="Cuplikan layar 2026-05-11 214525" src="https://github.com/user-attachments/assets/40ab2d68-4d87-4013-9b42-4307be22b6e5" />

Setiap kali program dijalankan, program akan selalu menampilkan output berikut di awal:

DATA NPM MAHASISWA UNILA

[2515061001, 2515061007, 2515061012, 2515061021, 2515061033, 2515061045, 2515061058, 2515061064, 2515061072, 2515061088, 
2515061091, 2515061104, 2515061117, 2515061125, 2515061139]

Kemudian program akan meminta input dari pengguna:

Jika pengguna memasukkan input yang bukan angka, misalnya huruf atau simbol, maka program akan menampilkan pesan berikut dan meminta input ulang:
Input harus berupa angka!

Contoh saya sebagai pengguna memasukkan NPM 2515061045 (ada di indeks ke-5 dalam list).
Program akan menampilkan proses pencarian langkah demi langkah sebagai berikut:
Indeks tengah: 7
Data tengah: 2515061064
Pindah ke bagian kiri
Indeks tengah: 3
Data tengah: 2515061021
Pindah ke bagian kanan
Indeks tengah: 5
Data tengah: 2515061045
NPM ditemukan pada indeks ke-5


Iterasi pertama: indeks tengah dihitung dari (0+14)//2 = 7, nilai pada indeks 7 adalah 2515061064. Karena 2515061064 lebih besar dari target 2515061045, pencarian pindah ke bagian kiri.
Iterasi kedua: indeks tengah dihitung dari (0+6)//2 = 3, nilai pada indeks 3 adalah 2515061021. Karena 2515061021 lebih kecil dari target 2515061045, pencarian pindah ke bagian kanan.
Iterasi ketiga: indeks tengah dihitung dari (4+6)//2 = 5, nilai pada indeks 5 adalah 2515061045. Nilai cocok dengan target, maka program menampilkan bahwa NPM ditemukan pada indeks ke-5.


Contoh lagi saya memasukkan NPM 2515061099 (tidak ada dalam list).

Program akan menampilkan proses pencarian hingga area pencarian habis:
Indeks tengah: 7
Data tengah: 2515061064
Pindah ke bagian kanan
Indeks tengah: 11
Data tengah: 2515061104
Pindah ke bagian kiri
Indeks tengah: 9
Data tengah: 2515061088
Pindah ke bagian kanan
Indeks tengah: 10
Data tengah: 2515061091
Pindah ke bagian kanan
NPM tidak ditemukan
Penjelasan proses:

Program terus membagi area pencarian menjadi dua bagian di setiap iterasi.

Ketika batas kiri sudah melewati batas kanan, berarti seluruh area sudah diperiksa dan target tidak ada.

Program kemudian menampilkan pesan NPM tidak ditemukan.


