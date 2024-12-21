import psycopg2

conn = psycopg2.connect(
        database='projectsbd',
        user='postgres',
        password='uvvu76',
        host='localhost',
        port='5432'
    )
cur = conn.cursor()