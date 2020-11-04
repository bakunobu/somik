import os
import psycopg2
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

conn_str = os.environ.get('URL')
conn = psycopg2.connect(conn_str)


cursor = conn.cursor()

cursor.execute('CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);')

cursor.execute('INSERT INTO test (num, data) VALUES (%s, %s)',
               (100, "abc'def"))

cursor.execute('SELECT * FROM test;')

print(cursor.fetchone())