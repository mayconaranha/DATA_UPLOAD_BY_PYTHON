import pyodbc

# CONEXÃO COM O BANCO #

def conectar_banco():
    conn = pyodbc.connect('driver={SQL Server};'
                          'server=DESKTOP-SD7B5S4\\SQLEXPRESS;'
                          'database=Praticas;')
    return conn



