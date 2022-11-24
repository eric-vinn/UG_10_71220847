print ("========== PROGRAM PENGHITUNG PYTHAGORAS ==========")
bbPertama = int(input("Masukkan bilngan bulat pertama: "))
bbKedua = int(input("Masukkan bilangan bulat kedua: "))
bbKetiga = int(input("Masukkan bilangan bulat ketiga: "))
hasil = (bbPertama ** 2) + (bbKedua ** 2)
if hasil == (bbKetiga**2):
    print("Merupakan Pythagoras")
else:
    print("BUkan Merupakan Pythagoras")
