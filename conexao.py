import sqlite3
def conectar():
    global com
    com=sqlite3.conecta("Gestao_Moda_Express")
    global cursor
    cursor=com.cursor()