def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        print(f"Indeks tengah: {tengah}")
        print(f"Data tengah: {data[tengah]}")

        if data[tengah] == target:
            return tengah

        elif data[tengah] < target:
            print("Pindah ke bagian kanan")
            kiri = tengah + 1

        else:
            print("Pindah ke bagian kiri")
            kanan = tengah - 1

    return -1


def main():
    npm_mahasiswa = [
        2515061001,
        2515061007,
        2515061012,
        2515061021,
        2515061033,
        2515061045,
        2515061058,
        2515061064,
        2515061072,
        2515061088,
        2515061091,
        2515061104,
        2515061117,
        2515061125,
        2515061139
    ]

    print("DATA NPM MAHASISWA UNILA")
    print(npm_mahasiswa)

    while True:
        try:
            target = int(input("Masukkan NPM yang ingin dicari: "))
            break

        except ValueError:
            print("Input harus berupa angka!")

    hasil = binary_search(npm_mahasiswa, target)

    if hasil != -1:
        print(f"NPM ditemukan pada indeks ke-{hasil}")

    else:
        print("NPM tidak ditemukan")


if __name__ == "__main__":
    main()