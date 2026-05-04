##a. Judul Program: pengurutan tinggi badan mahasiswa universitas lampung


##b. Deskripsi Singkat: Program ini merupakan implementasi algoritma **Selection Sort** yang diterapkan pada studi kasus pengurutan tinggi badan mahasiswa Universitas Lampung. Pengguna dapat memasukkan sejumlah data mahasiswa beserta tinggi badannya, kemudian program akan mengurutkan seluruh data tersebut baik secara **Ascending** (dari yang terpendek ke tertinggi) maupun **Descending** (dari yang tertinggi ke terpendek) sesuai pilihan pengguna.


##c. Source Code: <img width="2010" height="8730" alt="tugas_ akhir_judul2 py" src="https://github.com/user-attachments/assets/0b592572-d1d9-4c7a-82e0-218095688c74" />

def tukar(arr, i, j):
Mendefinisikan fungsi untuk menukar dua elemen dalam array berdasarkan indeks.
temp = arr[i]  
Menyimpan sementara nilai di indeks i.

arr[i] = arr[j]  
Mengisi posisi i dengan nilai dari indeks j.

arr[j] = temp  
Mengisi posisi j dengan nilai yang tadi disimpan.

def selection_sort_ascending(arr, n):
Fungsi untuk mengurutkan array dari kecil ke besar dengan selection sort.

for i in range(n - 1):  
Loop dari awal sampai elemen kedua terakhir.

for i in range(n - 1):  
Loop dari awal sampai elemen kedua terakhir.

for i in range(n - 1):  
Loop dari awal sampai elemen kedua terakhir.

pos_min = i
Anggap indeks i sebagai nilai terkecil

for j in range(i+1,n):
cek semua elemen setelah

if arr[j] < arr[pos_min]:
apabila ditemukan nilai yang lebih kecil nanti pos_min =j akan disimpan sebagai nilai terkecil

if pos_min != i:
jika nilai terkecil bukan di i maka terjadi pertukaran nilainya

def selection_sort_descending(arr, n):
Fungsi untuk mengurutkan dari besar ke kecil.

for i in range(n - 1):  
Loop utama.

pos_max = i  
Anggap i sebagai posisi terbesar.

dan logikanya sama seperti yang ascending hanya berbeda di pos nya 

def tampilkan_data(mahasiswa, tinggi, label=""):
Fungsi untuk menampilkan data mahasiswa.

if label:  
Jika ada label,

  print(f"  {label}")  
  Tampilkan judul.

print(f"  {'No'} {'Nama Mahasiswa'} {'Tinggi (cm)'}")  
Cetak header tabel.

for i in range(len(mahasiswa)):  
Loop semua data.

  print(f"  {i + 1} {mahasiswa[i]} {tinggi[i]} cm")  
  Tampilkan nomor, nama, dan tinggi.

  def urutkan_bersama(mahasiswa, tinggi):
Mengurutkan tinggi sekaligus nama agar tetap sinkron.

n = len(tinggi)  
Ambil jumlah data.

for i in range(n - 1):  
Loop utama.

   pos_min = i  
    Anggap i paling kecil.

  for j in range(i + 1, n):  
  Bandingkan dengan elemen lain.

  if tinggi[j] < tinggi[pos_min]:  
  Jika lebih kecil,

  pos_min = j  
  Simpan indeksnya.

  if pos_min != i:  
  Jika perlu tukar,

  tinggi[i], tinggi[pos_min] = tinggi[pos_min], tinggi[i]  
  Tukar tinggi.

  mahasiswa[i], mahasiswa[pos_min] = mahasiswa[pos_min], mahasiswa[i]  
  Tukar nama agar tetap sesuai.

  while True:  
Loop validasi input jumlah mahasiswa.

  try:  
        n = int(input("Masukkan jumlah mahasiswa: "))  
        Input jumlah mahasiswa.

  if n <= 0:  
            print("Jumlah mahasiswa harus lebih dari 0!")  
            continue  
        Cek agar tidak nol atau negatif.
      break  
        Keluar loop jika valid.
    except ValueError:  
        print("Input tidak valid! Masukkan angka bulat.")  
        Tangani input bukan angka.


nama_list   = []  
tinggi_list = []  
Siapkan list kosong.

print("Masukkan data mahasiswa:")  
Instruksi input.

for i in range(n):  
Loop input data.

  print(f"Mahasiswa ke-{i + 1}:")  
    Tampilkan nomor.

  nama = input("  Nama: ").strip()  
    Ambil nama dan hapus spasi.
    while not nama:  
        print("  Nama tidak boleh kosong!")  
        nama = input("  Nama: ").strip()  
    Validasi nama.

  while True:  
        try:  
            tinggi = float(input("  Tinggi badan (cm): "))  
            Input tinggi.
         if tinggi <= 0:  
                print("  Tinggi badan tidak boleh negaif atau nol")  
                continue  
            Validasi tinggi.
            break  
        except ValueError:  
            print("  Input tidak valid! Masukkan angka.")  
            Tangani error.

   nama_list.append(nama)  
    Simpan nama.

  tinggi_list.append(tinggi)  
    Simpan tinggi.

tampilkan_data(nama_list, tinggi_list, label="DATA SEBELUM DIURUTKAN")  
Tampilkan data awal.


print("Pilih metode pengurutan:")  
print("  1. Ascending  (terpendek ke tertinggi)")  
print("  2. Descending (tertinggi ke terpendek)")  
Tampilkan pilihan.

while True:  
    pilihan = input("Masukkan pilihan (1/2): ").strip()  
    Input pilihan.

   if pilihan in ("1", "2"):  
        break  
    Validasi input.
    print("Pilihan tidak valid! Masukkan 1 atau 2.")  

nama_sorted   = nama_list[:]  
tinggi_sorted = tinggi_list[:]  
Copy data agar asli tidak berubah.



if pilihan == "1":  
Jika ascending:

  n_data = len(tinggi_sorted)  
    Ambil jumlah data.

  for i in range(n_data - 1):  
    Loop utama.
        pos_min = i  
        for j in range(i + 1, n_data):  
            if tinggi_sorted[j] < tinggi_sorted[pos_min]:  
                pos_min = j  
        if pos_min != i:  
            tinggi_sorted[i], tinggi_sorted[pos_min] = tinggi_sorted[pos_min], tinggi_sorted[i]  
            nama_sorted[i], nama_sorted[pos_min] = nama_sorted[pos_min], nama_sorted[i]  
    Tukar data agar tetap sinkron.

  label_hasil = "HASIL PENGURUTAN ASCENDING (Terpendek → Tertinggi)"  
  menunjukkan urutan ascendingnya


  else:  
Jika descending:

   n_data = len(tinggi_sorted)  

  for i in range(n_data - 1):  
        pos_max = i  
        for j in range(i + 1, n_data):  
            if tinggi_sorted[j] > tinggi_sorted[pos_max]:  
                pos_max = j  

  if pos_max != i:  
            tinggi_sorted[i], tinggi_sorted[pos_max] = tinggi_sorted[pos_max], tinggi_sorted[i]  
            nama_sorted[i], nama_sorted[pos_max] = nama_sorted[pos_min], nama_sorted[i]  

  label_hasil = "HASIL PENGURUTAN DESCENDING (Tertinggi → Terpendek)"  
  mengurutkan dari dari tinggi ke pendek sesuai dengan descendingnya

  tampilkan_data(nama_sorted, tinggi_sorted, label=label_hasil)  
Tampilkan hasil akhir.

print("\n  STATISTIK TINGGI BADAN")  
Judul statistik.

print(f"  {'Tertinggi'}: {max(tinggi_list)} cm  ({nama_sorted[0] if pilihan == '2' else nama_sorted[-1]})")  
Tampilkan tertinggi.

print(f"  {'Terendah'}: {min(tinggi_list)} cm  ({nama_sorted[-1] if pilihan == '2' else nama_sorted[0]})")  
Tampilkan terendah.

print("  Program selesai. Terima kasih!")  
Penutup.






##D. Output Program : <img width="713" height="681" alt="image" src="https://github.com/user-attachments/assets/f65cdaaf-5865-4a08-a7b4-512e5036cb0a" />

user menginputkan jumlah mahasiswanya lalu mengisi nama dan tinggi mahasiswa tersebut, outputnya adalah urutan data sebelum diurutkan. Lalu user memilih ingin diurutkan dengan ascending atau descending, dan hasilnya adalah urutan sesuai pilihan user.


##E. Link youtube

