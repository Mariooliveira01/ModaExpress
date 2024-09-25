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