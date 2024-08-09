import sqlite3
import conexao
import consultaEstoque

conexao.conectar()
global itemApaga
itemApaga = consultaEstoque
try:
    if(itemApaga !=[]):
        conexao.cursor.execute("DELETE FROM ")
