import sqlite3
import criar_tabela
#Criando a Função para conctar ao banco de dados.
def conectar():
    try:
        global conn
        conn = sqlite3.connect("Gestao_Moda_Express.db")
        global cursor
        cursor = conn.cursor()
        
        print("Conexão com o Banco realizada!")
    except sqlite3.Error as erro:
        print("Falha ao conectar com o Banco.")