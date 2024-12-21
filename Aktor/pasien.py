import Tools.CRUD as crud
import psycopg2
import os
from start import UserSession

def clearconsole():
    os.system('cls')

class pasien():
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
        role = 3
        
        cur.execute(f"INSERT INTO akun(username, password, role_id_role) VALUES ('{username}','{password}',{role}) RETURNING id_akun")
        id_akun=cur.fetchone()[0]

        print("1. Mahasiswa")
        print("2. Dosen")
        print("3. Staff")
        print("4. Umum")
        pilih = int(input("Mau regist sebagai apa? "))
        if pilih == 1:
            nama=input("Masukkan Nama\t: ")
            nomorhp=input("Masukkan Nomor HP\t: ")
            umur=input("Masukkan Umur\t: ")
            gender= crud.get_gender_input()
            jalan = input("Masukkan Alamat Jalan\t: ")
            kota = input("Masukkan Alamat Kota\t: ")
            kdp = input("Masukkan Alamat Kode Pos\t: ")
            nim=input("Masukkan NIM\t: ")
            crud.fakultas()
            fks = int(input("Masukkan Nomor Fakultas\t: "))
            cur.execute(f"INSERT INTO alamat(jalan, kota, kode_pos) VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat")
            id_alamat = cur.fetchone()[0]
            cur.execute(f"INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, akun_id_akun, alamat_id_alamat, nim, fakultas_id_fakultas) VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_akun}, {id_alamat}, '{nim}', {fks})")

        elif pilih == 2:
            nama=input("Masukkan Nama\t: ")
            nomorhp=input("Masukkan Nomor HP\t: ")
            umur=input("Masukkan Umur\t: ")
            gender= crud.get_gender_input()
            jalan = input("Masukkan Alamat Jalan\t: ")
            kota = input("Masukkan Alamat Kota\t: ")
            kdp = input("Masukkan Alamat Kode Pos\t: ")
            nip = input("Masukkan NIP\t:: ")
            crud.fakultas()
            fks = int(input("Masukkan Nomor Fakultas\t: "))
            cur.execute(f"INSERT INTO alamat(jalan, kota, kode_pos) VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat")
            id_alamat = cur.fetchone()[0]
            cur.execute(f"INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, akun_id_akun, alamat_id_alamat, nip, fakultas_id_fakultas2) VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_akun}, {id_alamat}, '{nip}', {fks})")

        elif pilih == 3:
            nama=input("Masukkan Nama\t: ")
            nomorhp=input("Masukkan Nomor HP\t: ")
            umur=input("Masukkan Umur\t: ")
            gender= crud.get_gender_input()
            jalan = input("Masukkan Alamat Jalan\t: ")
            kota = input("Masukkan Alamat Kota\t: ")
            kdp = input("Masukkan Alamat Kode Pos\t: ")
            nostaff = input("Masukkan No Staff\t:: ")
            crud.fakultas()
            fks = int(input("Masukkan Nomor Fakultas\t: "))
            cur.execute(f"INSERT INTO alamat(jalan, kota, kode_pos) VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat")
            id_alamat = cur.fetchone()[0]
            cur.execute(f"INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, akun_id_akun, alamat_id_alamat, no_staff, fakultas_id_fakultas1) VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_akun}, {id_alamat}, '{nostaff}', {fks})")            

        elif pilih == 4:
            nama=input("Masukkan Nama\t: ")
            nomorhp=input("Masukkan Nomor HP\t: ")
            umur=input("Masukkan Umur\t: ")
            gender= crud.get_gender_input()
            jalan = input("Masukkan Alamat Jalan\t: ")
            kota = input("Masukkan Alamat Kota\t: ")
            kdp = input("Masukkan Alamat Kode Pos\t: ")
            nik = input("Masukkan NIP\t:: ")
            
            cur.execute(f"""INSERT INTO alamat(jalan, kota, kode_pos) 
                            VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat""")
            id_alamat = cur.fetchone()[0]
            cur.execute(f"""INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, akun_id_akun, alamat_id_alamat, nik) 
                            VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_akun}, {id_alamat}, '{nik}')""")
        else:
            input("Pilihan tidak tersedia... Enter untuk melanjutkan")
        
        conn.commit()
        print("Registrasi Berhasil..")
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
        print("1. Mahasiswa")
        print("2. Dosen")
        print("3. Staff")
        print("4. Umum")
        pilih = int(input("Mau login sebagai apa? "))
        query = None
        if pilih == 1:
            query = """SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, p.nim, f.nama_fakultas, a.role_id_role 
                        FROM akun a 
                        JOIN pasien p on (a.id_akun=p.akun_id_akun) 
                        JOIN alamat al on (p.alamat_id_alamat=al.id_alamat) 
                        JOIN fakultas f on (f.id_fakultas=p.fakultas_id_fakultas) 
                        WHERE p.nim IS NOT null AND a.username = %s AND a.password = %s AND role_id_role = 3"""
        elif pilih == 2:
            query = """SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, p.nip, f.nama_fakultas, a.role_id_role 
                        FROM akun a 
                        JOIN pasien p on (a.id_akun=p.akun_id_akun) 
                        JOIN alamat al on (p.alamat_id_alamat=al.id_alamat) 
                        JOIN fakultas f on (f.id_fakultas=p.fakultas_id_fakultas2) 
                        WHERE p.nip IS NOT null AND a.username = %s AND a.password = %s AND role_id_role = 3"""
        elif pilih == 3:
            query = """SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, p.no_staff, f.nama_fakultas, a.role_id_role 
                        FROM akun a 
                        JOIN pasien p on (a.id_akun=p.akun_id_akun) 
                        JOIN alamat al on (p.alamat_id_alamat=al.id_alamat) 
                        JOIN fakultas f on (f.id_fakultas=p.fakultas_id_fakultas1) 
                        WHERE p.no_staff IS NOT null AND a.username = %s AND a.password = %s AND role_id_role = 3"""
        elif pilih == 4:
            query = """SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, p.nik, a.role_id_role 
                        FROM akun a 
                        JOIN pasien p on (a.id_akun=p.akun_id_akun) 
                        JOIN alamat al on (p.alamat_id_alamat=al.id_alamat) 
                        WHERE p.nik IS NOT null AND a.username = %s AND a.password = %s AND role_id_role = 3"""
        
        if query:
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
    print("1. Reservasi Pemeriksaan ")
    print("2. Hasil Pemeriksaan")
    print("3.. Logout")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        reservasi()
    elif pilih == 2:
        clearconsole()
        hasil()
    elif pilih == 3:
        clearconsole()
        crud.logout()
    else:
        input("Tidak ada pilihan..enter untuk kembali..")
        clearconsole()
        show()

def reservasi():
    print("1. Lihat Antrian")
    print("2. Tambah Reservasi")
    print("3. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        crud.readantrianps()
    elif pilih == 2:
        clearconsole()
        crud.tambahresvps()
    elif pilih == 3:
        clearconsole()
        show()
    else:
        input
        ("Pilihan tidak valid...please enter")
        clearconsole()
        reservasi()

def hasil():
    print("!. Lihat Hasil Pemeriksaan")
    print("2. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        crud.readhspemeriksaan()
    elif pilih == 2:
        clearconsole()
        show()

