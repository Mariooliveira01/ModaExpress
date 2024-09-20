import sqlite3
import conexao

def exibirCliente():
    conexao.conectar()
    resultado=conexao.cursor.execute("SELECT * FROM cliente").fetchall()
    for result in resultado:
        print("nome:",result[0])
        print("sobrenome:",result[1])
        print("cpf:",result[2])
        print("telefone:",result[3])
        print("rua:",result[4])
        print("numero:",result[5])
        print("cidade:",result[6])
        print("estado:",result[7])

def exibirVendedor():
    conexao.conectar()
    resultado=conexao.cursor.execute("SELECT * FROM venndedor").fetchall()
    for result in resultado:
        print("id:",result[0])
        print("nome:",result[1])
        print("sobrenome:",result[2])
        print("cpf:",result[3])

def exibirEstoque():
    conexao.conectar()
    resultado=conexao.cursor.execute("SELECT * FROM prduto").fetchall()
    for result in resultado:
        print("id:",result[0])
        print("nome:",result[1])
        print("quantidade:",result[2])
        print("tamanho:",result[3])
        print("valor:",result[4])
        print("material:",result[5])
        print("cor:",result[6])

def consultaCliente():
    conexao.conectar()
    cpf = input("qual o CPF deseja consultar: ")
    try:
        resultado=conexao.conn.execute('''SELECT * FROM cliente WHERE cpf = ?''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado")
            
        else:
            for result in resultado:
                print("nome:",result[0])
                print("sobrenome:",result[1])
                print("cpf:",result[2])
                print("telefone:",result[3])
                print("rua:",result[4])
                print("numero:",result[5])
                print("cidade:",result[6])
                print("estado:",result[7])
    except sqlite3.Error as erro:
        print("erro ao tentar encontrar o CPF ",erro)

def consultaVendedor():
    conexao.conectar()
    id = input("qual o id deseja consultar: ")
    try:
        resultado=conexao.conn.execute('''SELECT * FROM vendedor WHERE id = ?''',(id,)).fetchall()
        if(resultado == []):
            print("id não encontrado")
            
        else:
            for result in resultado:
                print("id:",result[0])
                print("nome:",result[1])
                print("sobrenome:",result[2])
                print("cpf:",result[3])
    except sqlite3.Error as erro:
        print("erro ao tentar encontrar o id ",erro)

def consultaEstoque():
    conexao.conectar()
    id = input("qual o id deseja consultar: ")
    try:
        resultado=conexao.conn.execute('''SELECT * FROM produto WHERE id = ?''',(id,)).fetchall()
        if(resultado == []):
            print("id não encontrado")
            
        else:
            for result in resultado:
                print("id:",result[0])
                print("nome:",result[1])
                print("quantidade:",result[2])
                print("tamanho:",result[3])
                print("valor:",result[4])
                print("material:",result[5])
                print("cor:",result[6])
    except sqlite3.Error as erro:
        print("erro ao tentar encontrar o id ",erro)