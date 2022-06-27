import sys
import os

from sparepart import main_sparepart
from laptop import main_laptop
from aksesoris import main_aksesoris

def ask_again():
    pesan = input("Apakah anda ingin mencoba kembali (y atau n) ? ")

    if pesan == "Y" or pesan == "y":
        os.system('cls')
        display_menu()
    else:
        os.system('cls')
        print("Terima kasih sudah mencoba program kami.")


def display_menu():
    os.system('cls')
    print("""
    #             ===============================

    #             SELAMAT DATANG DI DOTA COMPUTER

    #             ===============================
    #             KATEGORI BARANG YANG TERSEDIA DI DOTA COMPUTER
    #             ===============================
    #             A. SPAREPART
    #             B. AKSESORIS
    #             C. LAPTOP
    #             ===============================
    #             """)

    pesan = input("Pilih Barang yang di inginkan : ")

    if pesan == "a" or pesan == "A":
        main_sparepart()
        ask_again()
    elif pesan == "b" or pesan == "B":
        main_aksesoris()
        ask_again()
    elif pesan == "c" or pesan == "C":
        main_laptop()
        ask_again()
    else:
        print("Menu tidak tersedia, Silahkan mencoba kembali")

display_menu()
