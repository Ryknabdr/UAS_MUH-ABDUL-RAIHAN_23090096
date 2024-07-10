from queue import Queue

def main():
    antrian_pesanan = Queue()
    menu = ("\nMenu Antrian Pesanan:\n"
            "1. Tambah Pesanan\n"
            "2. Hapus Pesanan\n"
            "3. Tampilkan Antrian\n"
            "4. Tampilkan Jumlah Pesanan\n"
            "5. Keluar\n")
    
    while True:
        print(menu)
        pilihan = input("Masukkan pilihan Anda (1-5): ")
        
        if pilihan == "1":
            antrian_pesanan(input("Masukkan pesanan yang ingin ditambahkan: "))
        elif pilihan == "2":
            dihapus = antrian_pesanan()
            if dihapus:
                print(f"Pesanan '{dihapus}' telah dihapus dari antrian.")
        elif pilihan == "3":
            antrian_pesanan()
        elif pilihan == "4":
            print(f"Jumlah pesanan dalam antrian: {antrian_pesanan()}")
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
