import sqlite3
import conexao
import cadastroProdutos
import selectCliente
def deleteCliente():
    conexao.conectar()
    global clienteApaga
    clienteApaga = selectCliente.consultaCliente
    try:
        if(clienteApaga !=[]):
            conexao.cursor.execute("DELETE FROM cliente WHERE cpf = ?",(clienteApaga))
            conexao.conn.commit()
            print("cliente removido com sucesso")
        elif(clienteApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)
def deleteVendedor():
    conexao.conectar()
    global vendedorApaga
    vendedorApaga = selectCliente.consultaVendedor
    try:
        if(vendedorApaga !=[]):
            conexao.cursor.execute("DELETE FROM vendedor WHERE id = ?",(vendedorApaga))
            conexao.conn.commit()
            print("vendedor demitido")
        elif(vendedorApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)
def deleteProduto():
    global produtoApaga
    produtoApaga = selectCliente.consultaEstoque
    try:
        if(produtoApaga !=[]):
            conexao.cursor.execute("DELETE FROM produto WHERE id = ?",(produtoApaga))
            conexao.conn.commit()
            print("produto removido do estoque")
        elif(produtoApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)