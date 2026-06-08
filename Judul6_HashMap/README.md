## A. Judul Program: Sistem Kasir Minimarket Berbasis Hash Map

## B. Deskripsi Singkat:
Program ini adalah sistem manajemen kasir minimarket sederhana yang dirancang untuk melakukan penyimpanan, pembaruan, pencarian, dan penghapusan data barang secara efisien. Masalah utama dalam sistem kasir konvensional sering kali terletak pada kecepatan pencarian item barang ketika transaksi sedang berlangsung. Dengan menggunakan struktur data Hash Map, program ini mampu mengoptimalkan waktu pencarian data barang menjadi lebih cepat dibandingkan pencarian linear biasa.

Algoritma struktur data yang diterapkan dalam program ini adalah Hash Map dengan metode penanganan kolisi (collision handling) berupa Chaining menggunakan Singly Linked List. Fungsi hash memetakan ID barang (key_id) ke dalam indeks array (slot memori) tertentu. Jika terjadi kolisi atau beberapa ID barang menghasilkan indeks slot yang sama, data akan ditambahkan sebagai node baru dalam rantai linked list pada slot tersebut.

## C. Source Code:

