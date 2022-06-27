import sys
import os


def main_aksesoris():

    print("""
    ===============================

    DOTA COMPUTER

    ===============================
    LIST AKSESORIS
    ===============================
    A. MOUSE
    B. KEYBOARD
    C. HEADPHONE
    ===============================
    """)
    pesan = str(input("Pilih AKSESORIS yang di inginkan :"))
    if pesan == "a" or pesan == "A":
        print("""
        ===========================
        LIST MOUSE
        ===========================
        A. LOGITECH : RP 500.000
        B. RAZER : RP 850.000
        C. SADES : RP 300.000
        ===========================
        """)
        pesan = str(input("Pililah MOUSE yang di inginkan :"))
        jumlahpesan = int(
            input("Masukkan Jumlah MOUSE yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "LOGITECH "
            harga = 500000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "b" or pesan == "B":
            listnama = "RAZER"
            harga = 850000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "c" or pesan == "C":
            listnama = "SADES"
            harga = 300000
            totalharga = int(jumlahpesan*harga)

        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    elif pesan == "b" or pesan == "B":
        print("""
        ===========================
        LIST KEYBOARD
        ===========================
        A. LOGITECH : RP 1.100.000
        B. ROYAL KLUDG : RP 1.500.000
        C. NOIR : RP 1.150.000
        ===========================
        """)
        pesan = str(input("Pililah KEYBOARD yang di inginkan :"))
        jumlahpesan = int(
            input("Masukkan Jumlah KEYBOARD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "LOGITECH"
            harga = 1100000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "b" or pesan == "B":
            listnama = "ROYAL KLUDG"
            harga = 1500000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "c" or pesan == "C":
            listnama = "NOIR"
            harga = 1150000
            totalharga = int(jumlahpesan*harga)

        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    elif pesan == "c" or pesan == "C":
        print("""
        ===========================
        LIST HEADPHONE
        ===========================
        A. HYPER X : RP 1.100.000
        B. REXUS : RP 450.000
        C. RAZER : RP 2.500.000
        ===========================
        """)
        pesan = str(input("Pililah SSD yang di inginkan :"))
        jumlahpesan = int(
            input("Masukkan Jumlah SSD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "HYPER X"
            harga = 1100000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "b" or pesan == "B":
            listnama = "REXUS"
            harga = 450000
            totalharga = int(jumlahpesan*harga)

        elif pesan == "c" or pesan == "C":
            listnama = "RAZER"
            harga = 2500000
            totalharga = int(jumlahpesan*harga)

        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    os.system('cls')
    print("=====================")
    print("DOTA COMPUTER")
    print("=====================")
    print("Nama Barang :",listnama)
    print("Jumlah Pesan :",jumlahpesan)
    print("Harga :",harga)
    print("Total Harga :",totalharga)
    print("=====================")

# aksesoris()
