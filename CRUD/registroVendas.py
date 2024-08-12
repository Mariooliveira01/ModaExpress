import sqlite3
import conexao

def consultarVenda():
        com = sqlite3.connect('moda_express.db')
        cursor = com.cursor()
        cursor.execute('SELECT * FROM cliente')
        vendas = cursor.fetchall()
        com.close()
        return vendas