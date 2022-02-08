# Importadno pymysql
import pymysql
#Verificando conexão e conectando 

try: 
  con = pymysql.connect(host="localhost", user="root", password="root", database="consulta")
  print("Database Successfully Connected...")
except Exception as e: 
  print("Connection Error: ", e)


cursor = con.cursor()
  
with con: 
  cursor.execute("CREATE TABLE if not exists formulario(id INTEGER PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(50), email VARCHAR(100), telefone CHAR(11), dia_em DATE, estado VARCHAR(50), assunto TEXT)")
  