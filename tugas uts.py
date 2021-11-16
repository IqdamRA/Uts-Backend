# while bertujuan untuk melakukan perulangan


cafe = "y"
while cafe == "y":
    print("--------------------")
    print("|   Warung sulid   |")
    print("--------------------")
    print("|   Makanan        |")
    print("|   Jus            |")
    print("|   Kopi           |")


    menu = input("Pilih menu: ")
    if menu == "makanan":
        makanan = ["=         mie          =", "=      nasi goreng     =",
                   "=      nasi pecel      =", "=     kentang goreng   =", "=      nasi kebuli     ="]
        print(makanan[0])
        print(makanan[1])
        print(makanan[2])
        print(makanan[3])
        print(makanan[4])
    elif menu == "jus":
        jus = ["=     jus alpukat      =",
               "=     jus mangga       =", "=     jus leci         =", "=     jus semangka     =", "=     jus duren        ="]
        print(jus[0])
        print(jus[1])
        print(jus[2])
        print(jus[3])
        print(jus[4])
    elif menu == "kopi":
        kopi = ["=    kopi kapal api    =",
                "=  luwak white coffee  =", "=     kopi tubruk      =", "=      kopi susu       =", "=      kopi ABC+       ="]
        print(kopi[0])
        print(kopi[1])
        print(kopi[2])
        print(kopi[3])
        print(kopi[4])
    else:
        print("Menu kosong")

    print(20*"=")
    pesan = input("Silahkan pilih yang ingin anda pesan: ")
    porsi = input("berapa porsi: ")
    print(20*"=")
    print("Menu yang anda pesan: ")
    print(20*"=")
    print(f"{pesan} | {porsi} porsi")
    cafe = input("apa ada yang dipesan lagi?(y/n)")

