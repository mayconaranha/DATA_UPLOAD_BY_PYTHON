import pandas as pd
import numpy
import time
import sqlalchemy
from conectar_banco import conectar_banco
from conversao_minutos import convert

# COMEÇO DA CONTAGEM DO TEMPO DE PROCESSAMENTO
start_time = time.time()

# CONEXÃO COM O BANCO
conn = conectar_banco()
print("Conexão com o banco de dados bem-sucedida.")

# DEFINIÇÃO DE TIPO DE DADOS
tipos_colunas = {'ID': int,
                 'NOME': str,
                 'IDADE': int,
                 'SEXO': str,
                 'DATA': str
                 }

# SELEÇÃO DE COLUNAS PARA IMPORT
lista_colunas = {
                'ID',
                'NOME',
                'IDADE',
                'SEXO',
                'DATA'

}

df = pd.DataFrame (lista_colunas)

# LEITURA DO ARQUIVO EM EXCEL
df = pd.read_excel('C:\\Users\\mayco\\Desktop\\PROJETOS PYTHON\\BASES\\IMPORT_NOME.xlsx'
                 , sheet_name = "Planilha1"
                 , usecols = lista_colunas
                , dtype = tipos_colunas
                )

# CONVERSÃO PARA DATA
df['DATA'] = pd.to_datetime(df['DATA'])
print(f"Leitura do arquivo bem-sucedida")

# IDENTIFICANDO DATA MIN/MAX
data_min = df['DATA'].min()
data_max = df['DATA'].max()

# DELETANDO NO SQL PARA NÃO TER DUPLICIDADE
query_delete = f"DELETE FROM TBL_D_PESSOAS WHERE DATA >= '{data_min}' AND DATA <= '{data_max}'"

# EXECUTANDO QUERY
cursor = conn.cursor()
cursor.execute(query_delete)
conn.commit()

#insiro dataframe ao banco
for index, row in df.iterrows():
    cursor.execute("INSERT INTO TBL_D_PESSOAS (ID,NOME,IDADE,SEXO,DATA) VALUES (?,?,?,?,?)", row.ID, row.NOME, row.IDADE, row.SEXO, row.DATA)
conn.commit()
print("Importação ao banco bem-sucedida!")

# ENCERRAR CONEXÃO COM O BANCO
conn.close()
print("Conexão com o banco encerrada.")

# FIM DA CONTAGEM DO TEMPO DE PROCESSAMENTO
end_time = time.time()

# CALCULO PARA SABER O TEMPO DE PROCESSAMENTO
elapsed_time = end_time - start_time

df = len(df)
print(f"Quantidade de linhas importadas: {df}")
print("Tempo para importar: ", convert(elapsed_time))


