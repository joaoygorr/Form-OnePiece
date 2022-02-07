# Importando Bibliotecas e Bases de Dados
import pandas as pd
import pathlib

meses = {"jan":1, "fev":2, "mar":3, "abr":4, "mai":5, "jun":6, "jul":7, "ago":8, "set":9, "out":10, "nov":11, "dez":12}

caminho_base = pathlib.Path("dataset")
base_airbnb = pd.DataFrame()

for arquivo in caminho_base.iterdir(): 
    nome_mes = arquivo.name[:3]
    mes = meses[nome_mes]
    
    ano = arquivo.name[-8:]
    ano = int(ano.replace(".csv", ""))
    
    df = pd.read_csv(caminho_base / arquivo.name)
    df["ano"] = ano
    df["mes"] = mes
    base_airbnb = base_airbnb.append(df)
print(base_airbnb)