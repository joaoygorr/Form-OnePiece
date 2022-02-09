# Importadno pymysql
import pymysql

#Verificando conexão e conectando 
try: 
  con = pymysql.connect(host="localhost", user="root", password="root", database="consulta")
  cursor = con.cursor()
  print("Database Successfully Connected...")
except Exception as e: 
  print("Connection Error: ", e)

# Tabelas
with con: 
  cursor.execute("CREATE TABLE if not exists Piece(id INTEGER PRIMARY KEY AUTO_INCREMENT, Saga VARCHAR(50), Arcos VARCHAR(50), Ep VARCHAR(4), filler BINARY, Descricao TEXT)")
  