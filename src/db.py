# Importadno pymysql
from sqlite3 import Cursor
import pymysql

#Verificando conexão e conectando 
try: 
  con = pymysql.connect(host="localhost", user="root", password="root")
  cursor = con.cursor()
  print("Database Successfully Connected...")
except Exception as e: 
  print("Connection Error: ", e)

# Tabelas e banco
with con: 
  cursor.execute("CREATE DATABASE if not exists consulta;")
  cursor.execute("use consulta;")
  cursor.execute("CREATE TABLE if not exists Piece(id INTEGER PRIMARY KEY AUTO_INCREMENT, Saga VARCHAR(50), Arcos VARCHAR(50), Ep VARCHAR(4), filler char(3), Data DATE, Descricao VARCHAR(150) DEFAULT '');")
  