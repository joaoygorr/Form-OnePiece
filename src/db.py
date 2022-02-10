# Importadno pymysql


try: 
  con = pymysql.connect(host="localhost", user="root", password="root")
  cursor = con.cursor()
  print("Database Successfully Connected...")
except Exception as e: 
  print("Connection Error: ", e)

lista = ['Ilha dos Homens-Peixe','Retorno a Sabaody', '517', "Não", '26/04/2002', 'teste']
  
# Tabelas 
with con: 
  cursor = con.cursor()
  cursor.execute("CREATE DATABASE if not exists consulta;")
  cursor.execute("use consulta;")
  cursor.execute("CREATE TABLE if not exists Piece(id INTEGER PRIMARY KEY AUTO_INCREMENT, Saga VARCHAR(50), Arcos VARCHAR(50), Ep CHAR(4), filler char(3), Data DATE, Descricao VARCHAR(150) DEFAULT '');")
  
with con:
    cursor = con.cursor()
    query = "INSERT INTO Piece (Saga, Arcos, Ep, Filler, Data, Descricao) VALUES (%s, %s, %s, %s, %s, %s)"  
    dados = (str(lista))
    cursor.execute(query, dados)