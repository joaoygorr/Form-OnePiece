# Importando SQLite
import sqlite3 as lite

# Criando conexão 
con = lite.connect("dados.db")

# Criando Banco e Tabela  
with con: 
  cursor = con.cursor()  
  cursor.execute("CREATE TABLE if not exists Piece(id INTEGER PRIMARY KEY AUTOINCREMENT, Saga VARCHAR(50), Arcos VARCHAR(50), Ep CHAR(4), filler char(3), Data DATE, Descricao VARCHAR(150) DEFAULT '');")
 
