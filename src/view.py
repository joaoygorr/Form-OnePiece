import sqlite3 as lite 

# Criando Conexão
con = lite.connect("dados.db")

lista = ['Ilha dos Homens-Peixe','Retorno a Sabaody', '517', "Não", '26/04/2002', 'teste']


# # Inserindo Informação
# with con:
#     cursor = con.cursor()
#     query = "INSERT INTO Piece (Saga, Arcos, Ep, Filler, Data, Descricao) VALUES (?, ?, ?, ?, ?, ?)"  
#     cursor.execute(query, lista)

# with con:
#     cursor = con.cursor()
#     query = "SELECCT * FROM Piece"  
#     cursor.execute(query)
#     info = cursor.fetchall()

# with con:
#     cursor = con.cursor()
#     query = "UPDATE Piece SET saga=?, where id=?"  
#     cursor.execute(query, lista)

# with con:
#     cursor = con.cursor()
#     query = "DELETE FROM piece WHERE id=?"  
#     cursor.execute(query, lista)

