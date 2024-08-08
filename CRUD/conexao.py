import sqlite3
#Criando a Função para conctar ao banco de dados.
def conectar():
    try:
        global com
        com = sqlite3.connect("Gestao_Moda_Express.db")
        global cursor
        cursor = com.cursor()
        print("Conexão com o Banco realizada!")
    except sqlite3.Error as erro:
        print("Falha ao conectar com o Banco.")