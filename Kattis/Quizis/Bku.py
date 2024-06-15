class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True
    
    def pinjam_buku(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False
    
    def kembalikan_buku(self):
        self.tersedia = True

def main():
    koleksi_buku = []

    while True:
        print("\nPilih opsi:")
        print("1. Tambah buku baru")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Tampilkan daftar buku")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan penulis buku: ")
            buku_baru = Buku(judul, penulis)
            koleksi_buku.append(buku_baru)
            print("Buku berhasil ditambahkan.")
        
        elif pilihan == "2":
            judul = input("Masukkan judul buku yang akan dipinjam: ")
            for buku in koleksi_buku:
                if buku.judul == judul:
                    if buku.pinjam_buku():
                        print("Buku berhasil dipinjam.")
                    else:
                        print("Buku sedang tidak tersedia.")
                    break
            else:
                print("Buku dengan judul tersebut tidak ditemukan.")
        
        elif pilihan == "3":
            judul = input("Masukkan judul buku yang akan dikembalikan: ")
            for buku in koleksi_buku:
                if buku.judul == judul:
                    buku.kembalikan_buku()
                    print("Buku berhasil dikembalikan.")
                    break
            else:
                print("Buku dengan judul tersebut tidak ditemukan.")
        
        elif pilihan == "4":
            if not koleksi_buku:
                print("Belum ada buku yang ditambahkan.")
            else:
                for buku in koleksi_buku:
                    status = "Tersedia" if buku.tersedia else "Dipinjam"
                    print(f"Judul: {buku.judul}, Penulis: {buku.penulis}, Status: {status}")
        
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
