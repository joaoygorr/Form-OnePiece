# Importando Bibliotecas e Bases de Dados
import pandas as pd 
import pathlib

base_path = pathlib.Path("dataset")

base_airbnb = pd.DataFrame()

for archive in base_path.iterdir(): 
    df = pd.read_csv(base_path / archive.name)
    base_airbnb = base_airbnb.append(df)
print(base_airbnb)