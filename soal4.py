class Buah:
    def __init__(self, nama_buah, warna_buah):
        self.nama_buah = nama_buah
        self.warna_buah = warna_buah

    def set_nama_buah(self, nama_buah):
        self.nama_buah = nama_buah

    def set_warna_buah(self, warna_buah):
        self.warna_buah = warna_buah

    def informasi_buah(self):
        print(f"Nama Buah: {self.nama_buah}, Warna Buah: {self.warna_buah}")

class Mangga(Buah):
    def __init__(self, nama_buah, warna_buah, rasa_mangga, vitamin_mangga):
        super().__init__(nama_buah, warna_buah)
        self.rasa_mangga = rasa_mangga
        self.vitamin_mangga = vitamin_mangga

    def set_rasa_mangga(self, rasa_mangga):
        self.rasa_mangga = rasa_mangga

    def set_vitamin_mangga(self, vitamin_mangga):
        self.vitamin_mangga = vitamin_mangga

    def informasi_mangga(self):
        super().informasi_buah()
        print(f"Rasa Mangga: {self.rasa_mangga}, Vitamin Mangga: {self.vitamin_mangga}")

mangga = Mangga("Mangga bosok", " coklat semu hitam", "sepet", "Vitamin b")
mangga.informasi_mangga()


