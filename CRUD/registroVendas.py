import sqlite3
import conexao

def consultarVenda():
        com = sqlite3.connect('moda_express.db')
        cursor = com.cursor()
        vendas = cursor.fetchall()
        com.close()
        return vendas