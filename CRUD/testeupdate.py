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

import sqlite3
import conexao
import select

def deleteCliente():
    conexao.conectar()  # Certifique-se de que essa função estabelece a conexão e o cursor
    clienteApaga = select.consultaCliente()  # Chame a função consultaCliente
    try:
        if clienteApaga:
            conexao.cursor.execute("DELETE FROM cliente WHERE cpf = ?", (clienteApaga,))
            conexao.conn.commit()
            print("Cliente removido com sucesso")
        else:
            print("Campo não preenchido")
    except sqlite3.Error as erro:
        print("Erro ao remover cliente:", erro)
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação

def deleteVendedor():
    conexao.conectar()
    vendedorApaga = select.consultaVendedor()  # Chame a função consultaVendedor
    try:
        if vendedorApaga:
            conexao.cursor.execute("DELETE FROM vendedor WHERE id = ?", (vendedorApaga,))
            conexao.conn.commit()
            print("Vendedor demitido com sucesso")
        else:
            print("Campo não preenchido")
    except sqlite3.Error as erro:
        print("Erro ao demitir vendedor:", erro)
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação

def deleteProduto():
    conexao.conectar()
    produtoApaga = select.consultaEstoque()  # Chame a função consultaEstoque
    try:
        if produtoApaga:
            conexao.cursor.execute("DELETE FROM produto WHERE id = ?", (produtoApaga,))
            conexao.conn.commit()
            print("Produto removido do estoque com sucesso")
        else:
            print("Campo não preenchido")
    except sqlite3.Error as erro:
        print("Erro ao remover produto:", erro)
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação