class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.lapar = True

    def beri_makan(self):
        self.lapar = False

class Herbivora(Hewan):
    def __init__(self, nama):
        super().__init__(nama, 'Herbivora')
        self.makanan = 'tumbuhan'

    def beri_makan(self, makanan):
        if makanan == self.makanan:
            super().beri_makan()
            print(f"{self.nama} telah diberi makan {makanan}.")
        else:
            print(f"{self.nama} hanya bisa makan tumbuhan.")

class Karnivora(Hewan):
    def __init__(self, nama):
        super().__init__(nama, 'Karnivora')
        self.makanan = 'daging'

    def beri_makan(self, makanan):
        if makanan == self.makanan:
            super().beri_makan()
            print(f"{self.nama} telah diberi makan {makanan}.")
        else:
            print(f"{self.nama} hanya bisa makan daging.")

def main():
    koleksi_hewan = []

    while True:
        print("\nPilih opsi:")
        print("1. Tambah hewan baru")
        print("2. Beri makan hewan")
        print("3. Tampilkan daftar hewan")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nama = input("Masukkan nama hewan: ")
            jenis = input("Masukkan jenis hewan (Herbivora/Karnivora): ").capitalize()
            if jenis == "Herbivora":
                hewan_baru = Herbivora(nama)
            elif jenis == "Karnivora":
                hewan_baru = Karnivora(nama)
            else:
                print("Jenis hewan tidak valid.")
                continue
            koleksi_hewan.append(hewan_baru)
            print(f"{jenis} bernama {nama} berhasil ditambahkan.")
        
        elif pilihan == "2":
            nama = input("Masukkan nama hewan yang akan diberi makan: ")
            makanan = input("Masukkan jenis makanan (tumbuhan/daging): ").lower()
            for hewan in koleksi_hewan:
                if hewan.nama == nama:
                    hewan.beri_makan(makanan)
                    break
            else:
                print("Hewan dengan nama tersebut tidak ditemukan.")
        
        elif pilihan == "3":
            if not koleksi_hewan:
                print("Belum ada hewan yang ditambahkan.")
            else:
                for hewan in koleksi_hewan:
                    status = "Lapar" if hewan.lapar else "Tidak Lapar"
                    print(f"Nama: {hewan.nama}, Jenis: {hewan.jenis}, Status: {status}")
        
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
