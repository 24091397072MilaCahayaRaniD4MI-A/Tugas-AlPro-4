masukkan = int(input("Banyak mahasiswa: "))
for i in range(masukkan):
    print ("Mahasiswa ke-" + str(i+1))
    banyakMatkul = int(input("Banyak mata kuliah yang diambil : "))
    totalNilai = 0
    for i in range(banyakMatkul):
        nilaiMatkul = int(input("Input nilai matkul ke-" + str(i+1) + ": "))
        totalNilai += nilaiMatkul
    rataRata = totalNilai / banyakMatkul
    print ("Rata-rata: ", rataRata)
    print("-" * 20)