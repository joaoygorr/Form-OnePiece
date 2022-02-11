# Importando pyodbc
import pyodbc

# Conectando e verificando conexão
try: 
  con = pyodbc.connect("DRIVER={MySQL ODBC 8.0 ANSI Driver}; SERVER=localhost; UID=root; PWD=root") 
  print("Database Successfully Connected...")
except Exception as e: 
  print("Connection Error: ", e)

# Criando Banco e Tabela  
with con: 
  cursor = con.cursor()  
  cursor.execute("CREATE DATABASE IF NOT EXISTS consulta;")
  cursor.execute("USE consulta;")
  cursor.execute("CREATE TABLE if not exists Piece(id INTEGER PRIMARY KEY AUTO_INCREMENT, Saga VARCHAR(50), Arcos VARCHAR(50), Ep CHAR(4), filler char(3), Data DATE, Descricao VARCHAR(150) DEFAULT '');")

# Exibindo dados 
with con:
    cursor = con.cursor()
    query = "SELECT * FROM Piece"  
    cursor.execute(query)
    info = cursor.fetchall()
    print(info)



  
# with con:
#     cursor = con.cursor()
#     query = "INSERT INTO Piece (Saga, Arcos, Ep, Filler, Data, Descricao) VALUES (%s, %s, %s, %s, %s, %s)"  
#     dados = (str(lista))
#     cursor.execute(query, dados)