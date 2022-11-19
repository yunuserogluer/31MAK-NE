print("""
*********************************
* GERÇEK Bİ HESAP MAKİNESİ *
*********************************
""")

sayi1 = int(input("İlk sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))
sor =   input("""Hangi işlemi yapacan slk?
A = Toplama
B = Çıkarma
C = Bölme
D = Çarpma
""")
toplam = sayi1+sayi2
cıkarma = sayi1-sayi2
bol = sayi1/sayi2
carp = sayi1*sayi2

if sor == "A":
    if toplam == 31:
        print("FSAFPAFKPOAEFKOPKSFSA ;)")

    else:
        print(toplam)

if sor == "B":
    if cıkarma == 31:
        print("FSAFPAFKPOAEFKOPKSFSA ;)")

    else:
        print(cıkarma)

if sor == "C":
    if bol == 31:
        print("FSAFPAFKPOAEFKOPKSFSA ;)")

    else:
        print(bol)

if sor == "D":
    if carp == 31:
        print("FSAFPAFKPOAEFKOPKSFSA ;)")

    else:
        print(carp)






