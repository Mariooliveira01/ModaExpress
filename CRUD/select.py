import sqlite3
import conexao

'''def exibirCliente():
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
        print("cor:",result[6])'''
def consultaCliente():
    conexao.conectar()
    cpf = input("Qual o CPF deseja consultar: ")
    try:
        resultado = conexao.conn.execute('''SELECT * FROM cliente WHERE cpf = ?''', (cpf,)).fetchall()
        if not resultado:  # Verifica se o resultado está vazio
            print("CPF não encontrado.")
        else:
            for result in resultado:
                print("Nome:", result[0])
                print("Sobrenome:", result[1])
                print("CPF:", result[2])
                print("Telefone:", result[3])
                print("Rua:", result[4])
                print("Número:", result[5])
                print("Cidade:", result[6])
                print("Estado:", result[7])
    except sqlite3.Error as erro:
        print("Erro ao tentar encontrar o CPF:", erro)
    finally:
        conexao.conn.close()  # Certifique-se de desconectar

def consultaVendedor():
    conexao.conectar()
    id = input("Qual o ID deseja consultar: ")
    try:
        resultado = conexao.conn.execute('''SELECT * FROM vendedor WHERE id = ?''', (id,)).fetchall()
        if not resultado:  # Verifica se o resultado está vazio
            print("ID não encontrado.")
        else:
            for result in resultado:
                print("ID:", result[0])
                print("Nome:", result[1])
                print("Sobrenome:", result[2])
                print("CPF:", result[3])
    except sqlite3.Error as erro:
        print("Erro ao tentar encontrar o ID:", erro)
    finally:
        conexao.conn.close()  # Certifique-se de desconectar

def consultaEstoque():
    conexao.conectar()
    id = input("Qual o ID deseja consultar: ")
    try:
        resultado = conexao.conn.execute('''SELECT * FROM produto WHERE id = ?''', (id,)).fetchall()
        if not resultado:  # Verifica se o resultado está vazio
            print("ID não encontrado.")
        else:
            for result in resultado:
                print("ID:", result[0])
                print("Nome:", result[1])
                print("Quantidade:", result[2])
                print("Tamanho:", result[3])
                print("Valor:", result[4])
                print("Material:", result[5])
                print("Cor:", result[6])
    except sqlite3.Error as erro:
        print("Erro ao tentar encontrar o ID:", erro)
    finally:
        conexao.conn.close()  # Certifique-se de desconectar

