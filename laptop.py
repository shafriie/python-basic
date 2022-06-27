import sys
import os

def main_laptop():
    listnama = ""
    harga = 0
    totalharga = 0

    print("""
    ===============================

    DOTA COMPUTER

    ===============================
    LIST LAPTOP
    ===============================
    A. ASUS
    B. ACER
    C. LENOVO
    ===============================
    """)
    pesan = str(input("Pilih LAPTOP yang di inginkan :"))
    if pesan == "a" or pesan == "A":
        print("""
        ===========================
        LIST ASUS
        ===========================
        A. TUF Gaming : RP 16.000.000
        B. ROG Gaming : RP 28.000.000
        ===========================
        """)
        pesan = str(input("Pililah MOUSE yang di inginkan :"))
        jumlahpesan = int(input("Masukkan Jumlah MOUSE yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "TUF Gaming"
            harga = 16000000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama,harga,totalharga])
        elif pesan == "b" or pesan == "B":
            listnama = "ROG Gaming"
            harga = 28000000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama,harga,totalharga])
        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    elif pesan == "b" or pesan == "B":
        print("""
        ===========================
        LIST ACER
        ===========================
        A. PREDATOR : RP 36.500.000
        B. NITRO : RP 12.500.000
        ===========================
        """)
        pesan = str(input("Pililah KEYBOARD yang di inginkan :"))
        jumlahpesan = int(
            input("Masukkan Jumlah KEYBOARD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "PREDATOR"
            harga = 36500000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama,harga,totalharga])
        elif pesan == "b" or pesan == "B":
            listnama = "NITRO"
            harga = 12500000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama,harga,totalharga])
        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    elif pesan == "c" or pesan == "C":
        print("""
        ===========================
        LIST LENOVO
        ===========================
        A. IDEPAD Gaming : RP 12.100.000
        B. LEGION : RP 18.450.000
        ===========================
        """)
        pesan = str(input("Pililah SSD yang di inginkan :"))
        jumlahpesan = int(input("Masukkan Jumlah SSD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "IDEPAD Gaming"
            harga = 12100000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama, harga, totalharga])
        elif pesan == "b" or pesan == "B":
            listnama = "LEGION"
            harga = 18450000
            totalharga = int(jumlahpesan*harga)
            # allpilihan.append([listnama, harga, totalharga])
        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    os.system('cls')
    print("=====================")
    print("DOTA COMPUTER")
    print("=====================")
    print("Nama Barang :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Total Harga :", totalharga)
    print("=====================")
