import sys
import os


def main_sparepart():
    listnama = ""
    harga = 0
    totalharga = 0

    print("""
    ===============================

    DOTA COMPUTER

    ===============================
    LIST SPAREPART
    ===============================
    A. RAM
    B. HDD
    C. SSD
    ===============================
    """)
    pesan = input("Pilih Sparepart yang di inginkan : ")

    if pesan == "a" or pesan == "A":
        print("""
        ===========================
        LIST RAM
        ===========================
        A. 2 GB : RP 200.000
        B. 4 GB : RP 400.000
        C. 8 GB : RP 800.000
        D. 16 GB : RP 1.200.000
        ===========================
        """)
        pesan = str(input("Pililah RAM yang di inginkan : "))
        jumlahpesan = int(input("Masukkan Jumlah RAM yang ingin dipesan : "))
        if pesan == "a" or pesan == "A":
            listnama = "RAM 2 GB"
            harga = 200000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "b" or pesan == "B":
            listnama = "RAM 4 GB"
            harga = 400000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "c" or pesan == "C":
            listnama = "RAM 8 GB"
            harga = 800000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "d" or pesan == "D":
            listnama = "RAM 16 GB"
            harga = 1200000
            totalharga = int(jumlahpesan*harga)

    elif pesan == "b" or pesan == "B":
        print("""
        ===========================
        LIST HDD
        ===========================
        A. 256 GB : RP 400.000
        B. 512 GB : RP 800.000
        C. 1 TB : RP 1.200.000
        D. 2 TB : RP 1.600.000
        ===========================
        """)
        pesan = str(input("Pililah HDD yang di inginkan :"))
        jumlahpesan = int(input("Masukkan Jumlah HDD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "HDD 256 GB"
            harga = 400000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "b" or pesan == "B":
            listnama = "HDD 512 GB"
            harga = 800000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "c" or pesan == "C":
            listnama = "HDD 1 TB"
            harga = 1200000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "d" or pesan == "D":
            listnama = "HDD 2 TB"
            harga = 1600000
            totalharga = int(jumlahpesan*harga)
        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    elif pesan == "c" or pesan == "C":
        print("""
        ===========================
        LIST SSD
        ===========================
        A. 128 GB : RP 400.000
        B. 256 GB : RP 800.000
        C. 512 GB : RP 1.200.000
        D. 1 TB : RP 1.600.000
        ===========================
        """)
        pesan = str(input("Pililah SSD yang di inginkan :"))
        jumlahpesan = int(input("Masukkan Jumlah SSD yang ingin dipesan :"))
        if pesan == "a" or pesan == "A":
            listnama = "SSD 128 GB"
            harga = 400000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "b" or pesan == "B":
            listnama = "SSD 256 GB"
            harga = 800000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "c" or pesan == "C":
            listnama = "SSD 512 GB"
            harga = 1200000
            totalharga = int(jumlahpesan*harga)
        elif pesan == "d" or pesan == "D":
            listnama = "SSD 1 TB"
            harga = 1600000
            totalharga = int(jumlahpesan*harga)
        else:
            listnama = "-"
            harga = "0"
            totalharga = "0"

    os.system('cls')
    print("=====================")
    print("DOTA COMPUTER")
    print("=====================")
    print("Nama Barang : ", listnama)
    print("Jumlah Pesan : ", jumlahpesan)
    print("Harga :", harga)
    print("Total Harga : ", totalharga)
    print("=====================")
