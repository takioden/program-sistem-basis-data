import Tools.CRUD as crud
import psycopg2
import os
from start import UserSession

def clearconsole():
    os.system('cls')

class dokter():
    def register():
        conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
        cur = conn.cursor()
        cur = conn.cursor()
        username = input("Buat Username\t: ")
        password = input("Buat Password\t: ")
        nama = input("Masukkan Nama\t: ")
        nostr = input("Masukkan No STR\t: ")
        nohp = input("Masukkan Nomor Hp\t: ")
        role = 2
        cur.execute(f"""INSERT INTO akun(username, password, role_id_role) 
                        VALUES ('{username}','{password}',{role}) RETURNING id_akun""")
        id_akun=cur.fetchone()[0]
        cur.execute(f"""INSERT INTO dokter(nama, no_str, nomorhp, akun_id_akun) 
                        VALUES ('{nama}', '{nostr}', '{nohp}',{id_akun})""")
        conn.commit()
        print("Registrasi Berhasil...")
        cur.close()
        conn.close()
        

    
    def login():
        conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
        cur = conn.cursor()
        username = input("Masukkan Username\t: ")
        password = input("Masukkan Password\t: ")
        query = """SELECT a.id_akun, a.username, a.password, d.id_dokter, d.no_str, d.nama, d.nomorhp, a.role_id_role 
                    FROM akun a 
                    JOIN dokter d ON (a.id_akun=d.akun_id_akun) 
                    WHERE a.username = %s AND a.password = %s AND a.role_id_role = 2"""
        cur.execute(query, (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session = UserSession()
            session.user_id = user[0]  # Set user_id to the id_akun
            print("Login Berhasil..")
            clearconsole()
            show()
        else:
            input("Login gagal. Username atau password salah.")
            crud.logout()
def show():
    print("1. Hasil Pemeriksaan")
    print("2. Penyakit")
    print("3. Obat")
    print("4. Logout")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        hasil()
    elif pilih == 2:
        clearconsole()
        penyakit()
    elif pilih == 3:
        clearconsole()
        obat()
    elif pilih == 4:
        clearconsole()
        crud.logout()
    else: 
        input("Pilihan tidak ada ")

def hasil():
    print("1. Lihat Hasil")
    print("2. Tambah Hasil Pemeriksaan")
    print("3. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        crud.readhasil()
    elif pilih == 2:
        clearconsole()
        crud.tambahhasil()
    elif pilih == 3:
        clearconsole()
        show()
    else:
        input("Pilihan tidak valid..")
        clearconsole()
        hasil()

def penyakit():
    print("1. Lihat penyakit")
    print("2. Tambah Penyakit")
    print("3. Edit Penyakit")
    print("4. Hapus Penyakit")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        crud.readpenyakit()
    elif pilih == 2:
        clearconsole()
        crud.tambahpenyakit()
    elif pilih == 3:
        clearconsole()
        crud.updatepenyakit()
    elif pilih == 4:
        clearconsole()
        crud.hapuspenyakit()
    elif pilih == 5:
        clearconsole()
        show()

def obat():
    print("1. Lihat Obat")
    print("2. Tambah Obat")
    print("3. Edit Obat")
    print("4. Hapus Obat")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        crud.readobat()
    elif pilih == 2:
        clearconsole()
        crud.tambahobat()
    elif pilih == 3:
        clearconsole()
        crud.updateobat()
    elif pilih == 4:
        clearconsole()
        crud.hapusobat()
    elif pilih == 5:
        clearconsole()
        show()
