print("Program untuk menentukan bilangan ganjil")
masukkan1 = int(input("Masukkan bilangan awal: "))
masukkan2 = int(input("Masukkan bilangan akhir: "))

while masukkan1 < masukkan2:
    if masukkan1 % 2:
        print(masukkan1)
    masukkan1 += 1    
