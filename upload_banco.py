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


# SELEÇÃO DE COLUNAS PARA IMPORT
lista_colunas = ['ID',
                 'NOME',
                 'IDADE',
                 'SEXO',
                 'DATA'
                ]
# DEFINIÇÃO DE TIPO DE DADOS
tipos_colunas = {'ID': int,
                 'NOME': str,
                 'IDADE': int,
                 'SEXO': str,
                 'DATA':pd.Timestamp
                 }

# LEITURA DO ARQUIVO EM EXCEL
df = pd.read_excel('C:\\Users\\mayco\\Desktop\\PROJETOS PYTHON\\BASES\\IMPORT_NOME.xlsx'
                 , sheet_name = "Planilha1"
                 , usecols = lista_colunas
                , dtype = tipos_colunas
                )
print("Leitura do arquivo bem-sucedida!")

# ENCERRAR CONEXÃO COM O BANCO
conn.close()
print("Conexão com o banco encerrada.")

# FIM DA CONTAGEM DO TEMPO DE PROCESSAMENTO
end_time = time.time()

# CALCULO PARA SABER O TEMPO DE PROCESSAMENTO
elapsed_time = end_time - start_time

df = numero_de_linhas = len(df)
print(f"Quantidade de linhas importadas: {numero_de_linhas}")
print("Tempo para importar: ", convert(elapsed_time))


