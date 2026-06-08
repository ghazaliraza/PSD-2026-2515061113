class Node:
    def __init__(self, key_id, nama_barang, harga):
        self.key_id = key_id          
        self.nama_barang = nama_barang
        self.harga = harga
        self.next = None

class Hash_Map_Minimarket:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key_id):
        return (key_id % self.SIZE + self.SIZE) % self.SIZE

    def tambah_atau_update_barang(self, key_id, nama_barang, harga):
        index = self.hash_function(key_id)
        current = self.table[index]
        
    
        while current is not None:
            if current.key_id == key_id:
                current.nama_barang = nama_barang
                current.harga = harga
                print(f" Data produk ID {key_id} berhasil diperbarui!")
                return
            current = current.next
        
        
        new_node = Node(key_id, nama_barang, harga)
        new_node.next = self.table[index]
        self.table[index] = new_node
        print(f" Produk '{nama_barang}' berhasil ditambahkan ke sistem!")

    def cek_harga_barang(self, key_id):
        index = self.hash_function(key_id)
        current = self.table[index]
        
        while current is not None:
            if current.key_id == key_id:
                return current  
            current = current.next
        return None  

    def hapus_barang(self, key_id):
        index = self.hash_function(key_id)
        current = self.table[index]
        prev = None
        
        while current is not None:
            if current.key_id == key_id:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def tampilkan_database_kasir(self):
        print(" INTERNAL MEMORI HASH TABLE ")
        for i in range(self.SIZE):
            print(f"Slot [{i}]: ", end="")
            current = self.table[i]
            if current is None:
                print("EMPTY")
            else:
                while current is not None:
                    print(f"[ID:{current.key_id} | {current.nama_barang} (Rp {current.harga})] -> ", end="")
                    current = current.next
                print("NONE")
        print("=" * 68)


def main():
    
    kasir_store = Hash_Map_Minimarket(size=10)
    
    
    kasir_store.tambah_atau_update_barang(101, "Susu Kotak UHT", 6500)
    kasir_store.tambah_atau_update_barang(102, "Mie Instan Goreng", 3500)
    
    while True:
        print( " MENU KASIR MINIMARKET " )
        print("1. Tambah / Update Barang")
        print("2. Scan / Cek Harga Barang (Pencarian)")
        print("3. Hapus Barang dari Sistem")
        print("4. Lihat data barang")
        print("5. Keluar dari Program")
        print("=" * 55)
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            print("TAMBAH / UPDATE BARANG ")
            try:
                key_id = int(input("Masukkan ID Barang (Angka): "))
                nama_barang = input("Masukkan Nama Barang       : ").strip()
                harga = int(input("Masukkan Harga Barang (Rp) : "))
                
                if nama_barang == "":
                    print(" Nama barang tidak boleh kosong!")
                    continue
                    
                kasir_store.tambah_atau_update_barang(key_id, nama_barang, harga)
            except ValueError:
                print("ID dan Harga harus berupa angka valid!")
                
        elif pilihan == "2":
            print("SCAN / CEK HARGA PRODUK ")
            try:
                id_dicari = int(input("Scan / Masukkan ID Barang yang dicari: "))
                barang = kasir_store.cek_harga_barang(id_dicari)
                
                if barang is not None:
                    print(f"PRODUK DITEMUKAN")
                    print(f"ID Produk   : {barang.key_id}")
                    print(f"Nama Produk : {barang.nama_barang}")
                    print(f"Harga       : Rp {barang.harga}")
                else:
                    print(f" Produk dengan ID {id_dicari} tidak ditemukan di sistem!")
            except ValueError:
                print("[ERROR] ID Barang harus berupa angka!")
                
        elif pilihan == "3":
            print("HAPUS BARANG")
            try:
                id_hapus = int(input("Masukkan ID Barang yang ingin dihapus: "))
                if kasir_store.hapus_barang(id_hapus):
                    print(f" [SUKSES] Produk ID {id_hapus} berhasil dihapus dari sistem.")
                else:
                    print(f" [ERROR] Produk ID {id_hapus} tidak ditemukan!")
            except ValueError:
                print("-> [ERROR] ID Barang harus berupa angka!")
                
        elif pilihan == "4":
            kasir_store.tampilkan_database_kasir()
            
        elif pilihan == "5":
            print("Terima kasih! Keluar dari sistem kasir minimarket.")
            break
            
        else:
            print("[ERROR] Pilihan menu tidak valid! Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    main()