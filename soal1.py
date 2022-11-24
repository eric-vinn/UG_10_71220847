print ("~~~~~~~~~~~~~~~ /('V')\ ~~~~~~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~~~~~~ /('V')\ ~~~~~~~~~~~~~~~")
print ("")
print ("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
print ("")

p = int(input("Masukkan pilihan Anda: "))
if p == 1:
    aLimas = int(input("Masukkan panjang sisi alas limas: "))
    tLimas = int(input("Masukkan tinggi limas: "))
    print("Volume limas tersebut adalah ", aLimas * aLimas * tLimas * 1/3)
elif p == 2:
    jBola = int(input("Masukkan panjang jari-jari bola: "))
    print ("Voluma bola tersebut adalah", 4/3*3.14*jBola*jBola*jBola)
elif p == 3:
    print("Pilihlah salah satu darii pilihan di bawah:")
    print("1. Prisma Segitiga")
    print("2. Prisma Segiempat")
    print("3. Prisma Segilima")
    pDua = int(input("Masukkan pilihan Anda: "))
    if pDua == 1:
        tigaPrisA = int(input("Masukkan panjang sisi alas prisma: "))
        tigaPrisTA = int(input("Masukkan tinggi alas prisma: "))
        tigaPrisT = int(input("Masukkan tinggi prisma segititga: "))
        print ("Voluma prisma segitiga tersebut adalah ", (1/2*tigaPrisA*tigaPrisTA)*tigaPrisT)
    elif pDua == 2:
        empatPrisA = int(input("Masukkan panjang sisi alas prisma: "))
        empatPrisTA = int(input("Masukkan tinggi alas prisma: "))
        empatPrisT = int(input("Masukkan tinggi prisma segiempat: "))  
        print ("Volume prisma segiempat tersebut adalah ", (empatPrisA*empatPrisTA)*empatPrisT)
    elif pDua == 3:
        limaPrisA = int(input("Masukkan panjang sisi alas prisma: "))
        limaPrisTA = int(input("Masukkan tinggi alas prisma: "))
        limaPrisT = int(input("Masukkan tinggi prisma segilima: "))
        print ("Volume prisma segilima tersebut adalah ", 1/2*(5*limaPrisA*limaPrisTA)*limaPrisT)
    else:
        print ("Prismayang Anda car belum tersedia di Kalkulator ini")
elif p == 4:
    jKerucut = int(input("Masukkan jari-jari kerucut: "))
    tKerucut = int(input(""))




