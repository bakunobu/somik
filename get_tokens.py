import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SERVER = os.environ.get('SERVER')

print(SERVER)