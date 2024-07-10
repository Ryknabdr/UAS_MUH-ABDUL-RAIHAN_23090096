from soal3Modul import warmindoer

def main():
    Soal_3Modul =warmindoer()

    while True:
        print("\nwarmindoer Menu:")
        print("1. Tambahkan pesanan (enqueue)")
        print("2. Sajikan pesanan (dequeue)")
        print("3. Menampilkan queue")
        print("4. Keluar")

        choice = input("Pilih satu opsi: ")

        if choice == "1":
            order = input("Masukan Pesanan: ")
            Soal_3Modul.enqueue(order)
        elif choice == "2":
            Soal_3Modul.dequeue()
        elif choice == "3":
            Soal_3Modul.display_queue()
        elif choice == "4":
            print("Terima Kasih :<.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
