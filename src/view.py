# Importando SQLite
import sqlite3 as lite

# Criando conexão 
con = lite.connect("dados.db")

# Acessar Informações
def show_information():
  lista = []
  with con:
    cursor = con.cursor()
    query = "SELECT * FROM Piece"  
    cursor.execute(query)
    info = cursor.fetchall()
    
    for i in info: 
      lista.append(i)
  return lista
  
# Inserindo Informação
def insert_info(i): 
  with con:
    cursor = con.cursor()
    query = "INSERT INTO Piece (Saga, Arcos, Ep, Filler, Data, Descricao) VALUES (?, ?, ?, ?, ?, ?)"  
    cursor.execute(query, i)


# Alterando Informação
def update_info(i):
  with con:
    cursor = con.cursor()
    query = "UPDATE Piece SET saga=?, arcos=?, ep=?, filler=?, data=?, descricao=? where id=?"  
    cursor.execute(query, i)

# Deletando Informação
def delete_info(i):
  with con:
    cursor = con.cursor()
    query = "DELETE FROM piece WHERE id=?"  
    cursor.execute(query, i)