import sqlite3
import conexao
import CRUD.select as select

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
        print("Erro:", erro)

def deleteVendedor():
    conexao.conectar()
    vendedorApaga = select.consultaVendedor()  # Chame a função consultaVendedor
    try:
        if vendedorApaga:
            conexao.cursor.execute("DELETE FROM vendedor WHERE id = ?", (vendedorApaga,))
            conexao.conn.commit()
            print("Vendedor demitido")
        else:
            print("Campo não preenchido")
    except sqlite3.Error as erro:
        print("Erro:", erro)

def deleteProduto():
    conexao.conectar()
    produtoApaga = select.consultaEstoque()  # Chame a função consultaEstoque
    try:
        if produtoApaga:
            conexao.cursor.execute("DELETE FROM produto WHERE id = ?", (produtoApaga,))
            conexao.conn.commit()
            print("Produto removido do estoque")
        else:
            print("Campo não preenchido")
    except sqlite3.Error as erro:
        print("Erro:", erro)
