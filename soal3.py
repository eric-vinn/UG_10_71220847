print ("Selamat Datang Di Program Pengurutan Bilangan")
print ("")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("1. Ascending")
print ("2. Descending")
print ("")
pilihan1 = int(input(">> "))
print ("")
if pilihan1 == 1:
    bilangan1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    bilangan2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    bilangan3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    bilangan4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    l1 = [bilangan1 , bilangan2 , bilangan3 , bilangan4]
    print ("Urutan angka anda ", sorted(l1))
elif pilihan1 == 2:
    bilangan1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    bilangan2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    bilangan3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    bilangan4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    l1 = [bilangan1 , bilangan2 , bilangan3 , bilangan4]
    print ("Urutan angka anda ", sorted(l1,reverse=True))
else:
    print ("Input anda salah")
