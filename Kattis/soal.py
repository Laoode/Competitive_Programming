class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        
    def perbarui_nilai(self, nama_baru, umur_baru, alamat_baru):
        self.nama = nama_baru
        self.umur = umur_baru
        self.alamat = alamat_baru
        
    def getStatus(self):
        if self.umur <= 30:
            return 'muda'
        elif 30 < self.umur <= 50:
            return 'paruh baya'
        else:
            return 'tua'

def main():
    manusia_list = []

    while True:
        print("\nPilih opsi:")
        print("1. Tambah Data")
        print("2. Tampil Data")
        print("3. Update Data")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")  
    
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            umur = int(input("Masukkan umur: "))
            alamat = input("Masukkan alamat: ")
            manusia = Manusia(nama, umur, alamat)
            manusia_list.append(manusia)
        elif pilihan == "2":
            if not manusia_list:
                print("Belum ada manusia yang ditambahkan.")
            else:
                for manusia in manusia_list:
                    print(f"Nama: {manusia.nama}, Umur: {manusia.umur},Status: {manusia.getStatus()}, Alamat: {manusia.alamat}")
                    print('-' * 30)
        elif pilihan == "3":
            nama = input("Masukkan nama yang akan diupdate: ")
            for manusia in manusia_list:
                if manusia.nama == nama:
                    nama_baru = input("Masukkan nama baru: ")
                    umur_baru = int(input("Masukkan umur baru: "))
                    alamat_baru = input("Masukkan alamat baru: ")
                    
                    manusia.perbarui_nilai(nama_baru, umur_baru, alamat_baru)
                    print("Nilai berhasil diperbarui.")
                    break
            else:
                print("Nama tidak ditemukan.")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
