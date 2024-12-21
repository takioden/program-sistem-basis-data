import Tools.CRUD as crud
import psycopg2
import os
from start import UserSession

def clearconsole():
    os.system('cls')

class admin():
    def register():
        
        conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
        cur = conn.cursor()
        username = input("Buat Username\t: ")
        password = input("Buat Password\t: ")
        nama = input("Masukkan nama\t: ")
        role = 1
        cur.execute(f"INSERT INTO akun(username, password, role_id_role) VALUES ('{username}','{password}',{role}) RETURNING id_akun")
        id_akun=cur.fetchone()[0]
        cur.execute(f"INSERT INTO admin(nama, akun_id_akun) VALUES ('{nama}', {id_akun})")

        print("Registrasi Berhasil...")
        conn.commit()
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
        query = """SELECT a.id_akun, a.username, a.password, ad.id_admin, ad.nama, a.role_id_role 
                    FROM akun a 
                    JOIN admin ad ON (a.id_akun=ad.akun_id_akun) 
                    WHERE a.username = %s AND a.password = %s AND a.role_id_role = 1"""
        cur.execute(query, (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session = UserSession()
            session.user_id = user[0]  # Set user_id to the id_akun
            input("Login Berhasil.. Enter untuk lanjutkan")
            clearconsole()
            show()
        else:
            input("Login gagal. Username atau password salah. Please enter")
            crud.logout()

def show():
    print("1. Reservasi")
    print("2. Dokter")
    print("3. Pasien")
    print("4. Profil")
    print("5. Logout")
    pilih = int(input("Pilihan anda? dalam int..\t: "))
    if pilih == 1:
        clearconsole()
        reservasi()
    elif pilih == 2:
        clearconsole()
        dokter()
    elif pilih == 3:
        clearconsole()
        pasien()
    elif pilih == 4:
        clearconsole()
        profil()
    elif pilih == 5:
        clearconsole()
        crud.logout()
    else:
        input("Pilihan tidak valid silahkan enter")
        show()

def reservasi():
    print("1. Lihat Reservasi")
    print("2. Tambah Antrian Reservasi")
    print("3. Update Status Antrian")
    print("4. Update Status Dokter")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan anda..\t: "))
    if pilih == 1:
        clearconsole()
        crud.readreserv()
    elif pilih == 2:
        clearconsole()
        crud.tambahantri()
    elif pilih == 3:
        clearconsole()
        crud.updatestatusantri()
    elif pilih == 4:
        clearconsole()
        crud.updatedokterjaga()
    elif pilih == 5:
        clearconsole()
        show()
    else:
        input("Pilihan tidak valid... silahkan enter")
        clearconsole()
        reservasi()
    
def dokter():
    print("1. Lihat Dokter")
    print("2. Tambah Dokter")
    print("3. Hapus Dokter")
    print("4. Edit Dokter")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan anda...\t: "))
    if pilih == 1:
        clearconsole()
        crud.readdokter()
    elif pilih == 2:
        clearconsole()
        crud.tambahdokter()
    elif pilih == 3:
        clearconsole()
        crud.hapusdokter()
    elif pilih == 4:
        clearconsole()
        crud.updatedokter()
    elif pilih == 5:
        clearconsole()
        show()
    else:
        input("Tidak ada pilihan. Tekan enter")
        clearconsole()
        dokter()
        
def profil():
    print("1. Lihat Profil")
    print("2. Update Profil")
    print("3. Kembali")
    pilih = int(input("Masukkan pilihan: "))
    if pilih == 1:
        clearconsole()
        crud.readprofadm()
    elif pilih == 2:
        clearconsole()
        crud.updateprofadm()
    elif pilih == 3:
        clearconsole()
        show()
    else:
        input("Tidak ada pilihan..enter untuk melanjutkan")
        clearconsole()
        profil()
        
def pasien():
    print("1. Lihat Pasien")
    print("2. Tambah Pasien")
    print("3. Hapus Pasien")
    print("4. Edit Pasien")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan anda...\t:"))
    if pilih == 1:
        clearconsole()
        crud.readpasien()
    elif pilih == 2:
        clearconsole()
        crud.tambahpasien()
    elif pilih == 3:
        clearconsole()
        crud.hapuspasien()
    elif pilih == 4:
        clearconsole()
        crud.updatepasien()
    elif pilih == 5:
        clearconsole()
        show()
    else:
        input("Pilihan tidak valid silahkan enter..")
        clearconsole()
        pasien()