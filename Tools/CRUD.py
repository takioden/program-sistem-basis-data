# from Tools.koneksi import *
from Aktor import admin
from Aktor import dokter
from Aktor import pasien
import psycopg2
import os 
import pandas as pd

def clearconsole():
     os.system('cls')

# ADMIN
# read
def keseluruhan():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter, a.nomor 
                    FROM reservasi_pemeriksaan r
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    JOIN antrian a ON (r.id_reservasi=a.reservasi_pemeriksaan_id_reservasi)
                    ORDER BY r.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    riwayatantr()
def umumsj():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter 
                    FROM reservasi_pemeriksaan r
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    JOIN antrian a ON (r.id_reservasi=a.reservasi_pemeriksaan_id_reservasi) 
                    WHERE po.nama_poli = 'Poli Umum'
                    ORDER BY r.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    riwayatantr()
def gigisj():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter 
                    FROM reservasi_pemeriksaan r
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    JOIN antrian a ON (r.id_reservasi=a.reservasi_pemeriksaan_id_reservasi) 
                    WHERE po.nama_poli = 'Poli Gigi'
                    ORDER BY r.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    riwayatantr()
def riwayatantr():
    print("1. Keseluruhan")
    print("2. Poli Umum")
    print("3. Poli Gigi")
    print("4. Kembali")
    pilihan = int(input("Masukkan pilihan\t: "))
    if pilihan == 1:
            clearconsole()
            keseluruhan()
    elif pilihan == 2:
            clearconsole()
            umumsj()
    elif pilihan == 3:
            clearconsole()
            gigisj()
    elif pilihan == 4:
            clearconsole()
            readreserv()
    else:
            input("Tidak ada pilihan..Enter untuk melanjutkan")
            clearconsole()

def readreserv():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    print("1. Riwayat Antrian")
    print("2. Antrian Poli Umum")
    print("3. Antrian Poli Gigi")
    print("4. Kembali")
    pilih = int(input("Masukkan pilihan\t: "))
    if pilih == 1:
        clearconsole()
        riwayatantr()
    elif pilih == 2:
        clearconsole()
        cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter, a.nomor 
                    FROM reservasi_pemeriksaan r
                    LEFT JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien) 
                    WHERE po.nama_poli = 'Poli Umum' AND r.tanggal = CURRENT_DATE""")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan..")
        clearconsole()
        readreserv()
    elif pilih == 3:
        clearconsole()
        cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter, a.nomor
                    FROM reservasi_pemeriksaan r
                    LEFT JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien) 
                    WHERE po.nama_poli = 'Poli Gigi' AND r.tanggal = CURRENT_DATE""")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan..")
        clearconsole()
        readreserv()
    elif pilih == 4:
        clearconsole()
        admin.reservasi()
    
    cur.close()
    conn.close()
    admin.reservasi()

def readdokter():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun,a.username, a.password, d.nama, d.no_str, d.nomorhp 
                FROM dokter d JOIN akun a on (d.akun_id_akun=a.id_akun)""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    admin.dokter()

def readpasien():
    print("1. Mahasiswa")
    print("2. Dosen")
    print("3. Staff")
    print("4. Umum")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan..\t: "))
    if pilih == 1:
         clearconsole()
         readpasienmahasiswa()
    elif pilih == 2:
         clearconsole()
         readpasiendosen()
    elif pilih == 3:
         clearconsole()
         readpasienstaff()
    elif pilih == 4:
         clearconsole()
         readpasienumum()
    elif pilih == 5:
         clearconsole()
         admin.pasien()
    else:
        input("Pilihan tidak valid silahkan enter..")
        clearconsole()
        readpasien()       
def readpasienmahasiswa():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    readpasien()
def readpasiendosen():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nip, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p 
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas2=f.id_fakultas) 
                WHERE p.nip IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    readpasien()
def readpasienstaff():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.no_staff, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p 
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas1=f.id_fakultas) 
                WHERE p.no_staff IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    readpasien()
def readpasienumum():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nik, al.jalan, al.kota, al.kode_pos 
                FROM pasien p 
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                WHERE p.nik IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    readpasien()

def readprofadm():
    from start import UserSession
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    session = UserSession()
    user_id = session.user_id
    cur = conn.cursor()
    cur.execute(f"""SELECT ak.username, ak.password, ad.nama 
                    FROM admin ad 
                    JOIN akun ak on (ad.akun_id_akun=ak.id_akun)
                    WHERE ak.id_akun = {user_id}""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    admin.profil()

# create
def tambahresadm():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter, a.nomor 
                        FROM reservasi_pemeriksaan r
                        LEFT JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                        JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                        JOIN poli po ON (r.poli_id_poli=po.id_poli)
                        JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                        WHERE r.tanggal = CURRENT_DATE""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print("ANTRIAN RESERVASI SAAT INI")
    print(df.to_markdown(index=False))
    print("DAFTAR DOKTER JAGA SAAT INI")
    dokterjaga()
    cur.execute(f"""SELECT p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas, p.no_staff, fa.nama_fakultas, p.nip, fak.nama_fakultas, p.nik
                    FROM pasien p
                    LEFT JOIN fakultas f ON (f.id_fakultas=p.fakultas_id_fakultas)
                    LEFT JOIN fakultas fa ON (fa.id_fakultas=p.fakultas_id_fakultas1)
                    LEFT JOIN fakultas fak ON (fak.id_fakultas=p.fakultas_id_fakultas2)
                    ORDER BY p.id_pasien""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print("DAFTAR PASIEN SAAT INI")
    print(df.to_markdown(index=False))
    print("DAFTAR POLI")
    readpoli()
    id_dokter = int(input("Masukkan id dokter\t: "))
    id_pasien = int(input("Masukkan id pasien\t: "))
    id_poli = int(input("Masukkan id poli\t: "))
    cur.execute(f"""INSERT INTO reservasi_pemeriksaan(pasien_id_pasien, dokter_id_dokter, poli_id_poli)
                    VALUES ({id_pasien}, {id_dokter}, {id_poli}) RETURNING id_reservasi""")
    id_resv=cur.fetchone()[0]
    nomorantri = int(input("Masukkan nomor antrian\t: "))
    cur.execute(f"""INSERT INTO antrian(nomor, reservasi_pemeriksaan_id_reservasi)
                        VALUES ({nomorantri}, {id_resv})""")
    conn.commit()
    print("Reservasi Berhasil Ditambahkan")
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter, a.nomor 
                    FROM reservasi_pemeriksaan r
                    LEFT JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    WHERE id_reservasi={id_resv}""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Tekan enter untuk kembali")
    cur.close()
    conn.close()
    clearconsole()
    tambahantri()
def tambahnomor():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter 
                        FROM reservasi_pemeriksaan r
                        JOIN dokter d on (r.dokter_id_dokter=d.id_dokter)
                        JOIN poli po on (r.poli_id_poli=po.id_poli)
                        JOIN pasien pa on (r.pasien_id_pasien=pa.id_pasien)
                        WHERE r.tanggal = CURRENT_DATE  """)
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_reserv = int(input("Masukkan id reservasi untuk menambah antrian\t: "))
    nomorantri = int(input("Masukkan no antri\t: "))
    cur.execute(f"""INSERT INTO antrian (nomor, reservasi_pemeriksaan_id_reservasi)
                        VALUES ({nomorantri}, {id_reserv})""")
    conn.commit()
    print("Nomor Berhasil Ditambahkan")
    cur.execute(f"""SELECT a.id_antrian, p.nama as pasien ,a.nomor, s.nama_status as status, r.tanggal 
                    FROM reservasi_pemeriksaan r
                    JOIN pasien p ON (p.id_pasien=r.pasien_id_pasien) 
                    JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN status s ON (a.status_id_status=s.id_status) 
                    WHERE r.tanggal = CURRENT_DATE AND r.id_reservasi={id_reserv}""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Tekan enter untuk kembali")
    cur.close()
    conn.close()
    clearconsole()
    tambahantri()
def tambahantri():
    print("1. Tambah Reservasi Pasien")
    print("2. Tambah Nomor Antrian Pasien")
    print("3. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole() 
        tambahresadm()
    elif pilih == 2:
        clearconsole()
        tambahnomor()
    elif pilih == 3:
        clearconsole()
        admin.show()
    else:    
        input("Pilihan tidak valid..Enter untuk kembali..")
        tambahantri()

def tambahdokter():
        conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
        cur = conn.cursor()
        username = input("Buat Username\t\t: ")
        password = input("Buat Password\t\t: ")
        nama = input("Masukkan Nama\t\t: ")
        nostr = input("Masukkan No STR\t\t: ")
        nohp = input("Masukkan Nomor Hp\t: ")
        role = 2
        cur.execute(f"""INSERT INTO akun(username, password, role_id_role) 
                    VALUES ('{username}','{password}',{role}) RETURNING id_akun""")
        id_akun=cur.fetchone()[0]
        cur.execute(f"""INSERT INTO dokter(nama, no_str, nomorhp, akun_id_akun) 
                    VALUES ('{nama}', '{nostr}', '{nohp}',{id_akun})""")
        conn.commit()
        print("Dokter berhasil ditambahkan..")
        input("Enter Untuk Kembali")
        clearconsole()
        admin.dokter()
        cur.close()
        conn.close()

def tambahpasien():
    print("1. Mahasiswa")
    print("2. Dosen")
    print("3. Staff")
    print("4. Umum")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan..\t: "))
    if pilih == 1:
        clearconsole()
        tambahmahasiswa()
    elif pilih == 2:
        clearconsole()
        tambahdosen()
    elif pilih ==  3:
        clearconsole()
        tambahstaff()
    elif pilih == 4:
        clearconsole()
        tambahumum()
    elif pilih == 5:
        clearconsole()
        admin.pasien()
    else:
        input("Tidak ada pilihan enter tuk lanjutkan")
        clearconsole()
        tambahpasien()
def tambahmahasiswa():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur = conn.cursor()
    nama=input("Masukkan Nama\t: ")
    nomorhp=input("Masukkan Nomor HP\t: ")
    umur=input("Masukkan Umur\t: ")
    gender= get_gender_input()
    jalan = input("Masukkan Alamat Jalan\t: ")
    kota = input("Masukkan Alamat Kota\t: ")
    kdp = input("Masukkan Alamat Kode Pos\t: ")
    nim=input("Masukkan NIM\t: ")
    fakultas()
    fks = int(input("Masukkan Nomor Fakultas\t: "))
    cur.execute(f"""INSERT INTO alamat(jalan, kota, kode_pos) 
                    VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, alamat_id_alamat, nim, fakultas_id_fakultas) 
                    VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_alamat}, '{nim}', {fks})""")
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil Ditambah...Enter untuk melanjutkan")
    clearconsole()
    tambahpasien()
def tambahdosen():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur = conn.cursor()
    nama=input("Masukkan Nama\t: ")
    nomorhp=input("Masukkan Nomor HP\t: ")
    umur=input("Masukkan Umur\t: ")
    gender= get_gender_input()
    jalan = input("Masukkan Alamat Jalan\t: ")
    kota = input("Masukkan Alamat Kota\t: ")
    kdp = input("Masukkan Alamat Kode Pos\t: ")
    nip = input("Masukkan NIP\t: ")
    fakultas()
    fks = int(input("Masukkan Nomor Fakultas\t: "))
    cur.execute(f"""INSERT INTO alamat(jalan, kota, kode_pos) 
                VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, alamat_id_alamat, nip, fakultas_id_fakultas2) 
                VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_alamat}, '{nip}', {fks})""")
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil Ditambah...Enter untuk melanjutkan")
    clearconsole()
    tambahpasien()
def tambahstaff():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur = conn.cursor()
    nama=input("Masukkan Nama\t: ")
    nomorhp=input("Masukkan Nomor HP\t: ")
    umur=input("Masukkan Umur\t: ")
    gender= get_gender_input()
    jalan = input("Masukkan Alamat Jalan\t: ")
    kota = input("Masukkan Alamat Kota\t: ")
    kdp = input("Masukkan Alamat Kode Pos\t: ")
    nostaff = input("Masukkan No Staff\t: ")
    fakultas()
    fks = int(input("Masukkan Nomor Fakultas\t: "))
    cur.execute(f"""INSERT INTO alamat(jalan, kota, kode_pos) 
                VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, alamat_id_alamat, no_staff, fakultas_id_fakultas1) 
                VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_alamat}, '{nostaff}', {fks})""")
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil Ditambah...Enter untuk melanjutkan")
    clearconsole()
    tambahpasien()
def tambahumum():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur = conn.cursor()
    nama=input("Masukkan Nama\t: ")
    nomorhp=input("Masukkan Nomor HP\t: ")
    umur=input("Masukkan Umur\t: ")
    gender= get_gender_input()
    jalan = input("Masukkan Alamat Jalan\t: ")
    kota = input("Masukkan Alamat Kota\t: ")
    kdp = input("Masukkan Alamat Kode Pos\t: ")
    nik = input("Masukkan NIK\t: ")
            
    cur.execute(f"""INSERT INTO alamat(jalan, kota, kode_pos) 
                VALUES ('{jalan}', '{kota}', '{kdp}') RETURNING id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""INSERT INTO pasien(nama, nomorhp, umur, jenis_kelamin, alamat_id_alamat, nik) 
                VALUES ('{nama}', '{nomorhp}', {umur}, '{gender}', {id_alamat}, '{nik}')""")
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil Ditambah...Enter untuk melanjutkan")
    clearconsole()
    tambahpasien()    

    

         
# update
def updatestatusantri():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_antrian ,r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter,a.nomor, a.status_id_status, s.nama_status 
                    FROM reservasi_pemeriksaan r
                    JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    JOIN status s ON (a.status_id_status=s.id_status)
                    WHERE r.tanggal = CURRENT_DATE""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_ant = int(input("Masukkan id antrian yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_antrian ,r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter,a.nomor, a.status_id_status, s.nama_status 
                    FROM reservasi_pemeriksaan r
                    JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien)
                    JOIN status s ON (a.status_id_status=s.id_status)
                    WHERE r.tanggal = CURRENT_DATE AND a.id_antrian = {id_ant} """)
    data = cur.fetchone()
    if data :
        print("Status saat ini: ")
        print(f"id antrian\t: {data[0]}")
        print(f"id reservasi\t: {data[1]}")
        print(f"nama poli\t: {data[4]}")
        print(f"nomor antri\t: {data[6]}")
        print(f"id status\t: {data[7]}")
        print(f"status\t: {data[8]}")
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    print("1. Menunggu")
    print("2. Sedang Ditangani")
    status = int(input("Masukkan id status baru\t: ")) or data[7]
    cur.execute(f"""UPDATE antrian SET status_id_status = {status}
                WHERE id_antrian = {id_ant} """)
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    cur.close()
    conn.close()
    admin.reservasi()

def updatedokter():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun,a.username, a.password, d.id_dokter, d.nama, d.no_str, d.nomorhp 
                FROM dokter d 
                JOIN akun a on (d.akun_id_akun=a.id_akun)""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_akun = int(input("Masukkan id akun yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_akun,a.username, a.password, d.id_dokter, d.nama, d.no_str, d.nomorhp 
                FROM dokter d JOIN akun a on (d.akun_id_akun=a.id_akun) 
                WHERE a.id_akun = {id_akun} """)
    data = cur.fetchone()
    
    if data :
        print("Data saat ini: ")
        print(f"id akun\t\t: {data[0]}")
        print(f"username\t: {data[1]}")
        print(f"password\t: {data[2]}")
        print(f"id dokter\t: {data[3]}")
        print(f"nomor str\t: {data[5]}")
        print(f"nama\t\t: {data[4]}")
        print(f"nomor hp\t: {data[6]}")
        
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input(f"Masukkan username baru\t: ") or data[1]
    password = input(f"Masukkan password baru\t: ") or data[2]
    nama = input(f"Masukkan nama baru\t: ") or data[4]
    nohp = input(f"Masukkan nohp baru\t: ") or data[6]
    nostr = input(f"Masukkan nomor str baru\t: ") or data[5]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}' 
                WHERE id_akun = {id_akun}""")
    cur.execute(f"""UPDATE dokter SET nama = '{nama}', nomorhp = '{nohp}', no_str = '{nostr}' 
                WHERE akun_id_akun = {id_akun} """)
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    admin.dokter()
    cur.close()
    conn.close()
    
def updatedokterjaga():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT  d.id_dokter, d.nama as "Nama Dokter", d.keadaan_id_keadaan as id_status, k.nama_keadaan as Status 
                    FROM dokter d 
                    JOIN keadaan k ON (d.keadaan_id_keadaan=k.id_keadaan)""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_dokter = int(input("Masukkan id dokter yang ingin di update statusnya\t: "))
    cur.execute(f"""SELECT d.id_dokter, d.nama as "Nama Dokter", d.keadaan_id_keadaan as id_status, k.nama_keadaan as Status 
                    FROM dokter d 
                    JOIN keadaan k ON (d.keadaan_id_keadaan=k.id_keadaan)
                    WHERE d.id_dokter = {id_dokter} """)
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id dokter\t\t: {data[0]}")
        print(f"nama dokter\t: {data[1]}")
        print(f"id status\t: {data[2]}")
        print(f"status dokter\t: {data[3]}")
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    print("1. Tidak Bertugas")
    print("2. Sedang Bertugas")
    status = int(input("Masukkan id status baru\t: ")) or data[2]
    cur.execute(f"""UPDATE dokter SET keadaan_id_keadaan = {status}
                WHERE id_dokter = {id_dokter} """)
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    cur.close()
    conn.close()
    admin.reservasi()

def updatepasien():
    print("1. Mahasiswa")
    print("2. Dosen")
    print("3. Staff")
    print("4. Umum")
    print("5. Kembali")
    pilih = int(input("Masukkan pilihan..\t: "))
    if pilih == 1:
        clearconsole()
        updatemahasiswa()
    elif pilih == 2:
        clearconsole()
        updatedosen()
    elif pilih ==  3:
        clearconsole()
        updatestaff()
    elif pilih == 4:
        clearconsole()
        updateumum()
    elif pilih == 5:
        clearconsole()
        admin.pasien()
    else:
        input("Tidak ada pilihan enter tuk lanjutkan")
        clearconsole()
        tambahpasien()
def updatemahasiswa():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos, id_pasien 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_akun = int(input("Masukkan id pasien yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos, p.fakultas_id_fakultas, id_pasien 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null AND id_pasien ={id_akun}""")
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id akun\t\t: {data[0]}")
        print(f"username\t: {data[1]}")
        print(f"password\t: {data[2]}")
        print(f"nama\t\t: {data[3]}")
        print(f"nomor hp\t: {data[4]}")
        print(f"umur\t\t: {data[5]}")
        print(f"jenis kelamin\t: {data[6]}")
        print(f"nim\t\t: {data[7]}")
        print(f"fakultas\t: {data[8]}")
        print(f"jalan\t\t: {data[9]}")
        print(f"kota\t\t: {data[10]}")
        print(f"kode pos\t: {data[11]}")

    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input(f"Masukkan username baru\t: ") or data[1]
    password = input(f"Masukkan password baru\t: ") or data[2]
    nama = input(f"Masukkan nama baru\t: ") or data[3]
    nohp = input(f"Masukkan nohp baru\t: ") or data[4]
    umur = input(f"Masukkan umur baru\t: ") or data[5]
    print("1. Laki laki")
    print("2. Perempuan")
    jeniskelamin = input(f"Ketikkan jenis kelamin baru\t: ") or data[6]
    nim = input(f"Masukkan NIM baru\t: ") or data[7]
    fakultas()
    fks = input(f"Masukkan fakultas baru\t: ") or data[12]
    jalan = input(f"Masukkan alamat jalan baru\t: ") or data[9]
    kota = input(f"Masukkan alamat kota baru\t: ") or data[10]
    kodepos = input(f"Masukkan alamat kode pos baru\t: ") or data[11]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}' 
                    WHERE id_akun = {id_akun}""")
    cur.execute(f"""UPDATE pasien SET nama = '{nama}', nomorhp = '{nohp}', umur = '{umur}', 
                    jenis_kelamin = '{jeniskelamin}', nim = '{nim}', fakultas_id_fakultas = '{fks}'
                    WHERE akun_id_akun = {id_akun}
                    RETURNING alamat_id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""UPDATE alamat SET jalan = '{jalan}', kota = '{kota}', kode_pos = '{kodepos}'
                    WHERE id_alamat = {id_alamat} """)
    
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    updatepasien()
    cur.close()
    conn.close()
def updatedosen():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nip, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas2=f.id_fakultas) 
                WHERE p.nip IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_akun = int(input("Masukkan id akun yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nip, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos, p.fakultas_id_fakultas 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas2=f.id_fakultas) 
                WHERE p.nim IS NOT null AND id_akun ={id_akun}""")
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id akun\t\t: {data[0]}")
        print(f"username\t: {data[1]}")
        print(f"password\t: {data[2]}")
        print(f"nama\t\t: {data[3]}")
        print(f"nomor hp\t: {data[4]}")
        print(f"umur\t\t: {data[5]}")
        print(f"jenis kelamin\t: {data[6]}")
        print(f"nip\t\t: {data[7]}")
        print(f"fakultas\t: {data[8]}")
        print(f"jalan\t\t: {data[9]}")
        print(f"kota\t\t: {data[10]}")
        print(f"kode pos\t: {data[11]}")

    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input(f"Masukkan username baru\t: ") or data[1]
    password = input(f"Masukkan password baru\t: ") or data[2]
    nama = input(f"Masukkan nama baru\t: ") or data[3]
    nohp = input(f"Masukkan nohp baru\t: ") or data[4]
    umur = input(f"Masukkan umur baru\t: ") or data[5]
    print("1. Laki laki")
    print("2. Perempuan")
    jeniskelamin = input(f"Ketikkan jenis kelamin baru\t: ") or data[6]
    nip = input(f"Masukkan NIP baru\t: ") or data[7]
    fakultas()
    fks = input(f"Masukkan fakultas baru\t: ") or data[12]
    jalan = input(f"Masukkan alamat jalan baru\t: ") or data[9]
    kota = input(f"Masukkan alamat kota baru\t: ") or data[10]
    kodepos = input(f"Masukkan alamat kode pos baru\t: ") or data[11]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}' 
                    WHERE id_akun = {id_akun}""")
    cur.execute(f"""UPDATE pasien SET nama = '{nama}', nomorhp = '{nohp}', umur = '{umur}', 
                    jenis_kelamin = '{jeniskelamin}', nip = '{nip}', fakultas_id_fakultas = '{fks}'
                    WHERE akun_id_akun = {id_akun}
                    RETURNING alamat_id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""UPDATE alamat SET jalan = '{jalan}', kota = '{kota}', kode_pos = '{kodepos}'
                    WHERE id_alamat = {id_alamat} """)
    
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    updatepasien()
    cur.close()
    conn.close()
def updatestaff():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_akun = int(input("Masukkan id akun yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos, p.fakultas_id_fakultas 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null AND id_akun ={id_akun}""")
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id akun\t\t: {data[0]}")
        print(f"username\t: {data[1]}")
        print(f"password\t: {data[2]}")
        print(f"nama\t\t: {data[3]}")
        print(f"nomor hp\t: {data[4]}")
        print(f"umur\t\t: {data[5]}")
        print(f"jenis kelamin\t: {data[6]}")
        print(f"nim\t\t: {data[7]}")
        print(f"fakultas\t: {data[8]}")
        print(f"jalan\t\t: {data[9]}")
        print(f"kota\t\t: {data[10]}")
        print(f"kode pos\t: {data[11]}")

    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input(f"Masukkan username baru\t: ") or data[1]
    password = input(f"Masukkan password baru\t: ") or data[2]
    nama = input(f"Masukkan nama baru\t: ") or data[3]
    nohp = input(f"Masukkan nohp baru\t: ") or data[4]
    umur = input(f"Masukkan umur baru\t: ") or data[5]
    print("1. Laki laki")
    print("2. Perempuan")
    jeniskelamin = input(f"Ketikkan jenis kelamin baru\t: ") or data[6]
    nim = input(f"Masukkan NIM baru\t: ") or data[7]
    fakultas()
    fks = input(f"Masukkan fakultas baru\t: ") or data[12]
    jalan = input(f"Masukkan alamat jalan baru\t: ") or data[9]
    kota = input(f"Masukkan alamat kota baru\t: ") or data[10]
    kodepos = input(f"Masukkan alamat kode pos baru\t: ") or data[11]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}' 
                    WHERE id_akun = {id_akun}""")
    cur.execute(f"""UPDATE pasien SET nama = '{nama}', nomorhp = '{nohp}', umur = '{umur}', 
                    jenis_kelamin = '{jeniskelamin}', nim = '{nim}', fakultas_id_fakultas = '{fks}'
                    WHERE akun_id_akun = {id_akun}
                    RETURNING alamat_id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""UPDATE alamat SET jalan = '{jalan}', kota = '{kota}', kode_pos = '{kodepos}'
                    WHERE id_alamat = {id_alamat} """)
    
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    updatepasien()
    cur.close()
    conn.close()
def updateumum():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_akun = int(input("Masukkan id akun yang ingin di update\t: "))
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, p.nim, f.nama_fakultas as fakultas, al.jalan, al.kota, al.kode_pos, p.fakultas_id_fakultas 
                FROM pasien p  
                LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun) 
                JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat) 
                JOIN fakultas f ON (p.fakultas_id_fakultas=f.id_fakultas) 
                WHERE p.nim IS NOT null AND id_akun ={id_akun}""")
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id akun\t\t: {data[0]}")
        print(f"username\t: {data[1]}")
        print(f"password\t: {data[2]}")
        print(f"nama\t\t: {data[3]}")
        print(f"nomor hp\t: {data[4]}")
        print(f"umur\t\t: {data[5]}")
        print(f"jenis kelamin\t: {data[6]}")
        print(f"nim\t\t: {data[7]}")
        print(f"fakultas\t: {data[8]}")
        print(f"jalan\t\t: {data[9]}")
        print(f"kota\t\t: {data[10]}")
        print(f"kode pos\t: {data[11]}")

    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input(f"Masukkan username baru\t: ") or data[1]
    password = input(f"Masukkan password baru\t: ") or data[2]
    nama = input(f"Masukkan nama baru\t: ") or data[3]
    nohp = input(f"Masukkan nohp baru\t: ") or data[4]
    umur = input(f"Masukkan umur baru\t: ") or data[5]
    print("1. Laki laki")
    print("2. Perempuan")
    jeniskelamin = input(f"Ketikkan jenis kelamin baru\t: ") or data[6]
    nim = input(f"Masukkan NIM baru\t: ") or data[7]
    fakultas()
    fks = input(f"Masukkan fakultas baru\t: ") or data[12]
    jalan = input(f"Masukkan alamat jalan baru\t: ") or data[9]
    kota = input(f"Masukkan alamat kota baru\t: ") or data[10]
    kodepos = input(f"Masukkan alamat kode pos baru\t: ") or data[11]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}' 
                    WHERE id_akun = {id_akun}""")
    cur.execute(f"""UPDATE pasien SET nama = '{nama}', nomorhp = '{nohp}', umur = '{umur}', 
                    jenis_kelamin = '{jeniskelamin}', nim = '{nim}', fakultas_id_fakultas = '{fks}'
                    WHERE akun_id_akun = {id_akun}
                    RETURNING alamat_id_alamat""")
    id_alamat = cur.fetchone()[0]
    cur.execute(f"""UPDATE alamat SET jalan = '{jalan}', kota = '{kota}', kode_pos = '{kodepos}'
                    WHERE id_alamat = {id_alamat} """)
    
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    updatepasien()
    cur.close()
    conn.close()

def updateprofadm():
    from start import UserSession
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    session = UserSession()
    user_id = session.user_id
    cur = conn.cursor()
    cur.execute(f"""SELECT ak.username, ak.password, ad.nama 
                    FROM admin ad 
                    JOIN akun ak on (ad.akun_id_akun=ak.id_akun)
                    WHERE ak.id_akun = {user_id}""")
    data = cur.fetchone()
    if data:
        print("Data saat ini: ")
        print(f"username\t: {data[0]}")
        print(f"password\t: {data[1]}")
        print(f"nama\t\t: {data[2]}")
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    username = input("Masukkan username baru\t: ") or data[0]
    password = input("Masukkan password baru\t:  ") or data[1]
    nama = input("Masukkan nama baru\t: ") or data[2]
    cur.execute(f"""UPDATE akun SET username = '{username}', password = '{password}'
                    WHERE id_akun = {user_id} """)
    cur.execute(f"""UPDATE admin SET nama = '{nama}'
                    WHERE akun_id_akun = {user_id} """)
    print("Berhasil diupdate")
    conn.commit()
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    admin.profil()
# delete

def hapusdokter():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"SELECT a.id_akun, a.username, a.password, d.nama, d.no_str, d.nomorhp FROM dokter d JOIN akun a on (d.akun_id_akun=a.id_akun)")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalhapus = int(input("Mau menghapus berapa data?"))
    for i in range(totalhapus):
        hapus = int(input("Masukkan id akun dokter yang ingin dihapus\t:"))
        cur.execute(f"DELETE FROM akun WHERE id_akun = {hapus}")
        conn.commit()
        print("Berhasil dihapus..")
    print("1. Pilih 1 Lihat Dokter")
    print("2. Pilih 2 Kembali")
    pilih = int(input("Pilih pilihan anda\t: "))
    if pilih == 1:
        cur = conn.cursor()
        cur.execute(f"SELECT a.id_akun, a.username, a.password, d.nama, d.no_str, d.nomorhp FROM dokter d JOIN akun a on (d.akun_id_akun=a.id_akun)")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan")
        clearconsole()
        admin.dokter()
    elif pilih == 2:
        clearconsole()
        admin.dokter()
    else:
        input("Pilihan tidak valid. Enter Untuk Melanjutkan")
        clearconsole()
        admin.dokter()
    conn.commit()
    cur.close()
    conn.close()

def hapuspasien():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, al.kode_pos
                    FROM pasien p
                    JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat)
                    LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun)""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    print("1. Yang ada akun")
    print("2. Tanpa ada akun")
    pilihan = int(input("Masukkan pilihan\t: "))
    if pilihan == 1:
        pasienakun()
    elif pilihan == 2:
        pasiennon()
    else: 
        input("Pilihan tidak ada.. enter")
        hapuspasien()
    print("1. Pilih 1 Lihat Pasien")
    print("2. Pilih 2 Kembali")
    pilih = int(input("Pilih pilihan anda\t: "))
    if pilih == 1:
        cur = conn.cursor()
        cur.execute(f"""SELECT a.id_akun, a.username, a.password, p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin, al.jalan, al.kota, al.kode_pos
                        FROM pasien p
                        JOIN alamat al ON (p.alamat_id_alamat=al.id_alamat)
                        LEFT JOIN akun a ON (p.akun_id_akun=a.id_akun)""")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan")
        clearconsole()
        admin.pasien()
    elif pilih == 2:
        admin.dokter()
    else:
        input("Pilihan tidak valid. Enter Untuk Melanjutkan")
        clearconsole()
        admin.pasien()
    conn.commit()
    cur.close()
    conn.close()    
def pasienakun():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    totalhapus = int(input("Mau menghapus berapa data?"))
    for i in range(totalhapus):
        hapus = int(input("Masukkan id pasien yang ingin dihapus\t:"))
        cur.execute(f"SELECT akun_id_akun FROM pasien WHERE id_pasien = {hapus}")
        akun_id = cur.fetchone()[0]
        cur.execute(f"DELETE FROM pasien WHERE id_pasien = {hapus}")
        cur.execute(f"DELETE FROM akun WHERE id_akun = {akun_id}")
        conn.commit()
def pasiennon():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    totalhapus = int(input("Mau menghapus berapa data?"))
    for i in range(totalhapus):
        hapus = int(input("Masukkan id pasien yang ingin dihapus\t:"))
        cur.execute(f"DELETE FROM pasien WHERE id_pasien = {hapus}")
        conn.commit()

# PASIEN
# read
def fakultas():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM fakultas")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
        
    cur.close()
    conn.close()

def readantrianps():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT a.id_antrian, p.nama as pasien ,a.nomor, s.nama_status as status, r.tanggal 
                FROM reservasi_pemeriksaan r
                JOIN pasien p ON (p.id_pasien=r.pasien_id_pasien) 
                JOIN antrian a ON (a.reservasi_pemeriksaan_id_reservasi=r.id_reservasi)
                JOIN status s ON (a.status_id_status=s.id_status) 
                WHERE r.tanggal = CURRENT_DATE""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()
    pasien.reservasi()

def dokterjaga():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT d.id_dokter ,d.nama as "Nama Dokter", k.nama_keadaan as Status
                    FROM dokter d 
                    JOIN keadaan k on (k.id_keadaan=d.keadaan_id_keadaan)
                    WHERE keadaan_id_keadaan = 2""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))

def readpoli():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM poli""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))

def readhspemeriksaan():
    from start import UserSession
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    session = UserSession()
    user_id = session.user_id
    cur.execute(f"""SELECT hp.id_hasil, rp.id_reservasi, rp.tanggal, d.nama as dokter, pa.nama as pasien, po.nama_poli, p.nama_penyakit, o.nama_obat, hp.catatan_dokter as catatan
                    FROM hasil_pemeriksaan hp
                    JOIN reservasi_pemeriksaan rp ON (hp.reservasi_pemeriksaan_id_reservasi=rp.id_reservasi)
                    JOIN dokter d ON (d.id_dokter=rp.dokter_id_dokter)
                    JOIN pasien pa ON (pa.id_pasien=rp.pasien_id_pasien)
                    JOIN akun a ON (a.id_akun=pa.akun_id_akun)
                    JOIN poli po ON (po.id_poli=rp.poli_id_poli)
					JOIN kondisi_kesehatan kk ON (hp.id_hasil =kk.hasil_pemeriksaan_id_hasil)
					JOIN penyakit p ON (kk.penyakit_id_penyakit=p.id_penyakit)
					JOIN resep_obat ro ON (hp.id_hasil=ro.hasil_pemeriksaan_id_hasil)
					JOIN obat o ON (ro.obat_id_obat=o.id_obat)
                    WHERE a.id_akun = {user_id}
                    ORDER BY rp.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    pasien.hasil()

#create
def get_gender_input():
    print("1. Laki laki")
    print("2. Perempuan")
    gender = int(input("Masukkan Nomor Gender\t: "))
    if gender == 1:
            return "Laki laki"
    elif gender == 2:
             return "Perempuan"
    else:
            print("Input tidak valid. Angkanya saja yaa")
            get_gender_input()


def tambahresvps():
    from start import UserSession
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    session = UserSession()
    user_id = session.user_id
    print("DATA ANDA")
    cur.execute(f"""SELECT p.id_pasien, p.nama, p.nomorhp, p.umur, p.jenis_kelamin
                    FROM pasien p
                    JOIN akun a ON (a.id_akun=p.akun_id_akun)
                    WHERE a.id_akun = {user_id}""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_pasien = int(input("Masukkan id pasien anda\t: "))
    print("DAFTAR DOKTER JAGA")
    dokterjaga()
    id_dokter = int(input("Pilih id dokter\t: "))
    print("DAFTAR POLI")
    readpoli()
    id_poli = int(input("Pilih id poli\t: "))
    cur.execute(f"""INSERT INTO reservasi_pemeriksaan (pasien_id_pasien, dokter_id_dokter, poli_id_poli)
                    VALUES ({id_pasien}, {id_dokter}, {id_poli}) RETURNING id_reservasi""")
    id_resv=cur.fetchone()[0]
    conn.commit()
    print("Reservasi Berhasil Ditambahkan")
    cur.execute(f"""SELECT rp.id_reservasi, rp.tanggal, pa.nama as "Nama Pasien", d.nama as "Nama Dokter", po.nama_Poli 
                    FROM reservasi_pemeriksaan rp
                    JOIN pasien pa ON (rp.pasien_id_pasien = pa.id_pasien)
                    JOIN dokter d ON (rp.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (rp.poli_id_poli=po.id_poli)
                    WHERE id_reservasi={id_resv}""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Tekan enter untuk kembali")
    clearconsole()
    pasien.reservasi()

# DOKTER
# read
def readpenyakit():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()  
    dokter.penyakit()

def readobat():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    cur.close()
    conn.close()
    input("Enter untuk kembali..")
    clearconsole()  
    dokter.obat()

def readhasil():
    print("1. Hasil Keseluruhan")
    print("2. Poli Umum")
    print("3. Poli Gigi")
    print("4. Kembali")
    pilih = int(input("Masukkan pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        hasilseluruh()
    elif pilih == 2:
        clearconsole()
        hasilumum()
    elif pilih == 3: 
        clearconsole()
        hasilgigi()
    elif pilih == 4:
        clearconsole()
        dokter.hasil()
    else:
        input("Tidak ada pilihan..Enter untuk keembali")
        clearconsole()
        dokter.hasil()
def hasilseluruh():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT hp.id_hasil, rp.id_reservasi, rp.tanggal, d.nama as dokter, pa.nama as pasien, po.nama_poli, kk.id_kondisi, p.nama_penyakit, ro.id_resep, o.nama_obat, hp.catatan_dokter
                    FROM hasil_pemeriksaan hp
                    JOIN reservasi_pemeriksaan rp ON (hp.reservasi_pemeriksaan_id_reservasi=rp.id_reservasi)
                    JOIN dokter d ON (d.id_dokter=rp.dokter_id_dokter)
                    JOIN pasien pa ON (pa.id_pasien=rp.pasien_id_pasien)
                    JOIN poli po ON (po.id_poli=rp.poli_id_poli)
					JOIN kondisi_kesehatan kk ON (hp.id_hasil =kk.hasil_pemeriksaan_id_hasil)
					JOIN penyakit p ON (kk.penyakit_id_penyakit=p.id_penyakit)
					JOIN resep_obat ro ON (hp.id_hasil=ro.hasil_pemeriksaan_id_hasil)
					JOIN obat o ON (ro.obat_id_obat=o.id_obat)
                    ORDER BY rp.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    readhasil()
def hasilumum():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT hp.id_hasil, rp.id_reservasi, rp.tanggal, d.nama as dokter, pa.nama as pasien, po.nama_poli, kk.id_kondisi, p.nama_penyakit, ro.id_resep, o.nama_obat, hp.catatan_dokter
                    FROM hasil_pemeriksaan hp
                    JOIN reservasi_pemeriksaan rp ON (hp.reservasi_pemeriksaan_id_reservasi=rp.id_reservasi)
                    JOIN dokter d ON (d.id_dokter=rp.dokter_id_dokter)
                    JOIN pasien pa ON (pa.id_pasien=rp.pasien_id_pasien)
                    JOIN poli po ON (po.id_poli=rp.poli_id_poli)
					JOIN kondisi_kesehatan kk ON (hp.id_hasil =kk.hasil_pemeriksaan_id_hasil)
					JOIN penyakit p ON (kk.penyakit_id_penyakit=p.id_penyakit)
					JOIN resep_obat ro ON (hp.id_hasil=ro.hasil_pemeriksaan_id_hasil)
					JOIN obat o ON (ro.obat_id_obat=o.id_obat)
                    WHERE po.nama_poli = 'Poli Umum'
                    ORDER BY rp.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    readhasil()
def hasilgigi():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT hp.id_hasil, rp.id_reservasi, rp.tanggal, d.nama as dokter, pa.nama as pasien, po.nama_poli, kk.id_kondisi, p.nama_penyakit, ro.id_resep, o.nama_obat, hp.catatan_dokter
                    FROM hasil_pemeriksaan hp
                    JOIN reservasi_pemeriksaan rp ON (hp.reservasi_pemeriksaan_id_reservasi=rp.id_reservasi)
                    JOIN dokter d ON (d.id_dokter=rp.dokter_id_dokter)
                    JOIN pasien pa ON (pa.id_pasien=rp.pasien_id_pasien)
                    JOIN poli po ON (po.id_poli=rp.poli_id_poli)
					JOIN kondisi_kesehatan kk ON (hp.id_hasil =kk.hasil_pemeriksaan_id_hasil)
					JOIN penyakit p ON (kk.penyakit_id_penyakit=p.id_penyakit)
					JOIN resep_obat ro ON (hp.id_hasil=ro.hasil_pemeriksaan_id_hasil)
					JOIN obat o ON (ro.obat_id_obat=o.id_obat)
                    WHERE po.nama_poli = 'Poli Gigi'
                    ORDER BY rp.tanggal DESC""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    input("Enter untuk kembali..")
    clearconsole()
    readhasil()
# create
def tambahpenyakit():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    penyakit = input("Masukkan nama penyakit\t: ")
    cur.execute(f"INSERT INTO penyakit(nama_penyakit) VALUES '{penyakit}'")
    cur.close()
    conn.close()
    input("Berhasil ditambahkan..Enter untuk kembali..")
    clearconsole()
    dokter.penyakit()

def tambahobat():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    obat = input("Masukkan nama obat\t: ")
    cur.execute(f"INSERT INTO obat(nama_obat) VALUES '{obat}'")
    cur.close()
    conn.close()
    input("Berhasil ditambahkan..Enter untuk kembali..")
    clearconsole()
    dokter.obat()

def tambahhasil():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    print("1. Poli Umum")
    print("2. poli Gigi")
    print("3. Kembali")
    pilih = int(input("Pilih pilihan anda\t: "))
    if pilih == 1:
        clearconsole()
        tambahumum()
    elif pilih == 2:
        clearconsole()
        tambahgigi()
    elif pilih == 3:
        clearconsole()
        dokter.hasil()
    else:
        input("Tidak ada pilihan silahkan enter untuk kembali")
        dokter.hasil()
def tambahumum():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter 
                    FROM reservasi_pemeriksaan r
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien) 
                    WHERE po.nama_poli = 'Poli Umum' AND r.tanggal = CURRENT_DATE""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_reservasi = int(input("Masukkan id reservasi yang ingin diberi hasil pemeriksaan: "))
    catatandok = input("Masukkan catatan dokter\t: ")
    cur.execute(f"""INSERT INTO hasil_pemeriksaan(catatan_dokter, reservasi_pemeriksaan_id_reservasi) 
                    VALUES ('{catatandok}', {id_reservasi}) RETURNING id_hasil""")
    id_hs=cur.fetchone()[0]
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalpenyakit = int(input("Ingin menambah berapa penyakit? "))
    for i in range(totalpenyakit):
        hasilkondisi = int(input("Masukkan id penyakit: "))
        cur.execute(f"""INSERT INTO kondisi_kesehatan(hasil_pemeriksaan_id_hasil, penyakit_id_penyakit)
                        VALUES ({id_hs}, {hasilkondisi})""")
        conn.commit()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalobat = int(input("ingin menambah berapa obat? "))
    for i in range (totalobat):
        hasilobat = int(input("Masukkan id obat: "))
        cur.execute(f"""INSERT INTO resep_obat(hasil_pemeriksaan_id_hasil, obat_id_obat)
                        VALUES ({id_hs}, {hasilobat}) """)
        conn.commit()
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil ditambahkan.. enter untuk kembali")
    clearconsole()
    tambahhasil()
def tambahgigi():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT r.id_reservasi, r.tanggal, pa.nama as nama_pasien, po.nama_poli, d.nama as nama_dokter 
                    FROM reservasi_pemeriksaan r
                    JOIN dokter d ON (r.dokter_id_dokter=d.id_dokter)
                    JOIN poli po ON (r.poli_id_poli=po.id_poli)
                    JOIN pasien pa ON (r.pasien_id_pasien=pa.id_pasien) 
                    WHERE po.nama_poli = 'Poli Gigi' AND r.tanggal = CURRENT_DATE""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_reservasi = int(input("Masukkan id reservasi yang ingin diberi hasil pemeriksaan: "))
    catatandok = input("Masukkan catatan dokter\t: ")
    cur.execute(f"""INSERT INTO hasil_pemeriksaan(catatan_dokter, reservasi_pemeriksaan_id_reservasi) 
                    VALUES ('{catatandok}', {id_reservasi}) RETURNING id_hasil""")
    id_hs=cur.fetchone()[0]
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalpenyakit = int(input("Ingin menambah berapa penyakit? "))
    for i in range(totalpenyakit):
        hasilkondisi = int(input("Masukkan id penyakit: "))
        cur.execute(f"""INSERT INTO kondisi_kesehatan(hasil_pemeriksaan_id_hasil, penyakit_id_penyakit)
                        VALUES ({id_hs}, {hasilkondisi})""")
        conn.commit()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalobat = int(input("ingin menambah berapa obat? "))
    for i in range (totalobat):
        hasilobat = int(input("Masukkan id obat: "))
        cur.execute(f"""INSERT INTO resep_obat(hasil_pemeriksaan_id_hasil, obat_id_obat)
                        VALUES ({id_hs}, {hasilobat}) """)
        conn.commit()
    conn.commit()
    cur.close()
    conn.close()
    input("Berhasil ditambahkan.. enter untuk kembali")
    clearconsole()
    
# update
def updatepenyakit():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_penyakit = int(input("Masukkan id penyakit yang ingin di update\t: "))
    cur.execute(f"""SELECT * FROM penyakit WHERE id_penyakit = {id_penyakit} """)
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id penyakit\t\t: {data[0]}")
        print(f"nama penyakit\t: {data[1]}")
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    nama = input(f"Masukkan nama penyakit baru\t: ") or data[1]
    cur.execute(f"""UPDATE penyakit SET nama_penyakit = '{nama}'
                WHERE id_penyakit = {id_penyakit}""")
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    cur.close()
    conn.close()
    dokter.penyakit()

def updateobat():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    id_obat = int(input("Masukkan id obat yang ingin di update\t: "))
    cur.execute(f"""SELECT * FROM obat WHERE id_obat = {id_obat} """)
    data = cur.fetchone()
    if data :
        print("Data saat ini: ")
        print(f"id penyakit\t\t: {data[0]}")
        print(f"nama penyakit\t: {data[1]}")
    print ("Isikan untuk mengganti dan kosongi jika tidak lalu enter")
    nama = input(f"Masukkan nama obat baru\t: ") or data[1]
    cur.execute(f"""UPDATE obat SET nama_obat = '{nama}'
                WHERE id_obat = {id_obat}""")
    print("Berhasil diupdate")
    input("Enter untuk kembali")
    conn.commit()
    clearconsole()
    cur.close()
    conn.close()
    dokter.obat()


# delete
def hapuspenyakit():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM penyakit""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalhapus = int(input("Mau menghapus berapa data?"))
    for i in range(totalhapus):
        hapus = int(input("Masukkan id penyakit yang ingin dihapus\t:"))
        cur.execute(f"DELETE FROM penyakit WHERE id_penyakit = {hapus}")
        conn.commit()
        print("Berhasil dihapus..")
    print("1. Pilih 1 Lihat Penyakit")
    print("2. Pilih 2 Kembali")
    pilih = int(input("Pilih pilihan anda\t: "))
    if pilih == 1:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM penyakit")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan")
        clearconsole()
        dokter.penyakit()
    elif pilih == 2:
        clearconsole()
        dokter.penyakit()
    else:
        input("Pilihan tidak valid. Enter Untuk Melanjutkan")
        clearconsole()
        dokter.penyakit()
    conn.commit()
    cur.close()
    conn.close()

def hapusobat():
    conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432')
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM obat""")
    data = cur.fetchall()
    nama_kolom = [desc[0] for desc in cur.description]
    df = pd.DataFrame(data, columns=nama_kolom)
    print(df.to_markdown(index=False))
    totalhapus = int(input("Mau menghapus berapa data?"))
    for i in range(totalhapus):
        hapus = int(input("Masukkan id obat yang ingin dihapus\t:"))
        cur.execute(f"DELETE FROM obat WHERE id_obat = {hapus}")
        conn.commit()
        print("Berhasil dihapus..")
    print("1. Pilih 1 Lihat Penyakit")
    print("2. Pilih 2 Kembali")
    pilih = int(input("Pilih pilihan anda\t: "))
    if pilih == 1:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM obat")
        data = cur.fetchall()
        nama_kolom = [desc[0] for desc in cur.description]
        df = pd.DataFrame(data, columns=nama_kolom)
        print(df.to_markdown(index=False))
        input("Enter untuk melanjutkan")
        clearconsole()
        dokter.obat()
    elif pilih == 2:
        clearconsole()
        dokter.obat()
    else:
        input("Pilihan tidak valid. Enter Untuk Melanjutkan")
        clearconsole()
        dokter.obat()
    conn.commit()
    cur.close()
    conn.close()


# LOGOUT
def logout():
    from main import display
    display()