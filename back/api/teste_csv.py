import pandas as pd

#2. Lendo o CSV de autores
df = pd.read_csv("population/autores.csv")   # cabeçalhos: nome,sobrenome,data_nascimento,nacionalidade[,biografia]
print(df.head())                             # primeiras linhas
print(df.shape)                              # (linhas, colunas)
print(df.dtypes)                             # tipos das colunas


# Limpeza básica (o que SEMPRE aparece em planilhas)

# 3.1: Padronizar espaços e caixa
print('\n\n\nSem padrão: \n', df)
print('Padronizar espaços e caixa')
for col in ["nome", "sobrenome", "nacionalidade"]:
    df[col] = df[col].astype(str).str.strip()

print('\n\n\nCom padrão: \n',df)
    
# 3.2: Datas como datetime (parser seguro)
df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce", format="%Y-%m-%d")
print('\n\n\nDatas como datetime\n',df)

# 3.3: Corrigir capitalização
df["nacionalidade"] = df["nacionalidade"].str.capitalize()  # "Brasileira", "Portuguesa", etc.
print('\n\n\nCorrigir capitalização\n', df)

# 3.4: Remover linhas totalmente vazias (se houver)
df = df.dropna(how="all")
print('\n\n\nRemover linhas totalmente vazias (se houver)\n\n', df)


# 3.6: Preencher valores ausentes opcionais
if "biografia" not in df.columns:
    df["biografia"] = "---"
print('\n\n\nPreencher valores ausentes opcionais\n\n', df)


# Filtrar autores brasileiros
br = df[df["nacionalidade"] == "Brasileira"]
print('\n\n\nFiltrar autores brasileiros\n\n', br)

# Selecionar colunas
apenas_nomes = df[["nome", "sobrenome"]]
print('\n\n\nSelecionar colunas\n\n', apenas_nomes)

# Ordenar por data
df = df.sort_values("data_nascimento")
print('\n\n\nOrdenar por data\n\n', df)

# Contagens
print(df["nacionalidade"].value_counts())



# print('\n\n\n\n\n')