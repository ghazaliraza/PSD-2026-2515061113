def tukar(arr, i, j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort_ascending(arr, n):
   
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos_min]:
                pos_min = j
        if pos_min != i:
            tukar(arr, i, pos_min)


def selection_sort_descending(arr, n):
    
    for i in range(n - 1):
        pos_max = i
        for j in range(i + 1, n):
            if arr[j] > arr[pos_max]:
                pos_max = j
        if pos_max != i:
            tukar(arr, i, pos_max)


def tampilkan_data(mahasiswa, tinggi, label=""):
    
   
    if label:
        print(f"  {label}")
        
    print(f"  {'No'} {'Nama Mahasiswa'} {'Tinggi (cm)'}")
    for i in range(len(mahasiswa)):
        print(f"  {i + 1} {mahasiswa[i]} {tinggi[i]} cm")
   


def urutkan_bersama(mahasiswa, tinggi):
 
    n = len(tinggi)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if tinggi[j] < tinggi[pos_min]:
                pos_min = j
        if pos_min != i:
            tinggi[i], tinggi[pos_min] = tinggi[pos_min], tinggi[i]
            mahasiswa[i], mahasiswa[pos_min] = mahasiswa[pos_min], mahasiswa[i]


def main():
    print("  SISTEM PENGURUTAN TINGGI BADAN MAHASISWA")
    print("       UNIVERSITAS LAMPUNG - 2026")
   

  
    while True:
        try:
            n = int(input("Masukkan jumlah mahasiswa: "))
            if n <= 0:
                print("Jumlah mahasiswa harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka bulat.")

   
    nama_list   = []
    tinggi_list = []

    print("Masukkan data mahasiswa:")

    for i in range(n):
        print(f"Mahasiswa ke-{i + 1}:")

        nama = input("  Nama: ").strip()
        while not nama:
            print("  Nama tidak boleh kosong!")
            nama = input("  Nama: ").strip()

        while True:
            try:
                tinggi = float(input("  Tinggi badan (cm): "))
                if tinggi <= 0:
                    print("  Tinggi badan tidak boleh negaif atau nol")
                    continue
                break
            except ValueError:
                print("  Input tidak valid! Masukkan angka.")

        nama_list.append(nama)
        tinggi_list.append(tinggi)

   
    tampilkan_data(nama_list, tinggi_list,
                   label="DATA SEBELUM DIURUTKAN")

   
    print("Pilih metode pengurutan:")
    print("  1. Ascending  (terpendek ke tertinggi)")
    print("  2. Descending (tertinggi ke terpendek)")
    while True:
        pilihan = input("Masukkan pilihan (1/2): ").strip()
        if pilihan in ("1", "2"):
            break
        print("Pilihan tidak valid! Masukkan 1 atau 2.")

   
    nama_sorted   = nama_list[:]
    tinggi_sorted = tinggi_list[:]

    if pilihan == "1":
        
        n_data = len(tinggi_sorted)
        for i in range(n_data - 1):
            pos_min = i
            for j in range(i + 1, n_data):
                if tinggi_sorted[j] < tinggi_sorted[pos_min]:
                    pos_min = j
            if pos_min != i:
                tinggi_sorted[i], tinggi_sorted[pos_min] = \
                    tinggi_sorted[pos_min], tinggi_sorted[i]
                nama_sorted[i], nama_sorted[pos_min] = \
                    nama_sorted[pos_min], nama_sorted[i]
        label_hasil = "HASIL PENGURUTAN ASCENDING (Terpendek → Tertinggi)"
    else:
        
        n_data = len(tinggi_sorted)
        for i in range(n_data - 1):
            pos_max = i
            for j in range(i + 1, n_data):
                if tinggi_sorted[j] > tinggi_sorted[pos_max]:
                    pos_max = j
            if pos_max != i:
                tinggi_sorted[i], tinggi_sorted[pos_max] = \
                    tinggi_sorted[pos_max], tinggi_sorted[i]
                nama_sorted[i], nama_sorted[pos_max] = \
                    nama_sorted[pos_max], nama_sorted[i]
        label_hasil = "HASIL PENGURUTAN DESCENDING (Tertinggi → Terpendek)"

   
    tampilkan_data(nama_sorted, tinggi_sorted, label=label_hasil)

   
 
    print("  Program selesai. Terima kasih!")
    


if __name__ == "__main__":
    main()