class Siswa:
    def __init__(self, nama, nilai_matematika):
        self.nama = nama
        self.nilai_matematika = nilai_matematika
    
    def perbarui_nilai(self, nilai_baru):
        self.nilai_matematika = nilai_baru

def main():
    siswa_list = []

    while True:
        print("\nPilih opsi:")
        print("1. Tambah siswa baru")
        print("2. Perbarui nilai siswa")
        print("3. Tampilkan daftar siswa")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            nilai = int(input("Masukkan nilai matematika siswa: "))
            siswa_baru = Siswa(nama, nilai)
            siswa_list.append(siswa_baru)
            print("Siswa berhasil ditambahkan.")
        
        elif pilihan == "2":
            nama = input("Masukkan nama siswa yang akan diperbarui: ")
            for siswa in siswa_list:
                if siswa.nama == nama:
                    nilai_baru = int(input("Masukkan nilai matematika baru: "))
                    siswa.perbarui_nilai(nilai_baru)
                    print("Nilai berhasil diperbarui.")
                    break
            else:
                print("Siswa tidak ditemukan.")
        
        elif pilihan == "3":
            if not siswa_list:
                print("Belum ada siswa yang ditambahkan.")
            else:
                for siswa in siswa_list:
                    print(f"Nama: {siswa.nama}, Nilai Matematika: {siswa.nilai_matematika}")
        
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
