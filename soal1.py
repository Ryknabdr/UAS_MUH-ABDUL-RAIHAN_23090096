def input_mahasiswa():
    data_mahasiswa = []
    while True:
        nim = input("Masukkan NIM anda: ")
        nama = input("Masukkan Nama anda: ")
        data_mahasiswa.append({"NIM": nim, "Nama": nama})
        
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi == 'tidak':
            break
    return data_mahasiswa

def tampilkan_data(data_mahasiswa):
    print("Data Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

def main():
    print("==== Program untuk memasukan Data Mahasiswa ====")
    data_mahasiswa = input_mahasiswa()
    tampilkan_data(data_mahasiswa)
    print("==== Program Selesai ====")

if __name__ == "__main__":
    main()
