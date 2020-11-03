import os
import psycopg2
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

conn_str = os.environ.get(URL)
conn = psycopg2.connect(conn_str)


