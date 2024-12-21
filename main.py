from Aktor import admin as ad
from Aktor import dokter as do
from Aktor import pasien as pa
import os

def clearconsole():
    os.system('cls')

def display():
            clearconsole()
            print("SELAMAT DATANG")
            input("Enter Untuk Masuk")
            clearconsole()
            masuk()

def masuk():
    print("1. Admin")
    print("2. Dokter")
    print("3. Pasien")
    # try:    
    masuk = int(input("Masuk Sebagai? pilih nomornya... "))
    clearconsole()

    if masuk == 1:
            print("SELAMAT DATANG ADMIN...")
            print("1. Registrasi")
            print("2. Login")
            print("3. Kembali")
            admin = int(input("Pilih pilihan anda... "))
            clearconsole()
            if admin == 1:
                ad.admin.register()
                input("Enter untuk melanjutkan")
                clearconsole()
                display()
            elif admin == 2:
                clearconsole()
                ad.admin.login()
            elif admin == 3:
                clearconsole()
                display()
            else:
                input("Pilihan tidak valid Enter tuk lanjutkan...")
                clearconsole()
                display()
    elif masuk == 2:
            print("SELAMAT DATANG DOKTER")
            print("1. Registrasi")
            print("2. Login")
            print("3. Kembali")
            dokter = int(input("Pilih pilihan anda... "))
            clearconsole()
            if dokter == 1:
                do.dokter.register()
                input("Enter untuk melanjutkan")
                clearconsole()
                display()
            elif dokter == 2:
                clearconsole()
                do.dokter.login()
            elif dokter == 3:
                clearconsole()
                display()
            else:
                input("Pilihan tidak valid Enter tuk lanjutkan...")
                clearconsole()
                display()
    elif masuk == 3:
            print("SELAMAT DATANG PASIEN")
            print("1. Registrasi")
            print("2. Login")
            print("3. Kembali")
            pasien = int(input("Pilih pilihan anda... "))
            clearconsole()
            if pasien == 1:
                pa.pasien.register()
                input("Enter untuk melanjutkan")
                clearconsole()
                display()
            elif pasien == 2:
                clearconsole()
                pa.pasien.login()
            elif pasien == 3:
                clearconsole()
                display()
            else:
                input("Pilihan tidak valid Enter tuk lanjutkan...")
                clearconsole()
                display()
        
    else:
            input("Pilihan tidak valid Enter tuk lanjutkan...")
            display()
    # except Exception as error:
    #     input("Terjadi kesalahan...Enter tuk melanjutkan")
    #     display()

display()


