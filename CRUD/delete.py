import sqlite3
import conexao
import consultaEstoque
def deleteCliente():
    conexao.conectar()
    global clienteApaga
    clienteApaga = 
    try:
        if(clienteApaga !=[]):
            conexao.cursor.execute("DELETE FROM cliente WHERE cpf = ?",(clienteApaga))
            conexao.com.commit()
            print("cliente removido com sucesso")
        elif(clienteApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)

def deleteVendedor():
    conexao.conectar()
    global vendedorApaga
    vendedorApaga =
    try:
        if(vendedorApaga !=[]):
            conexao.cursor.execute("DELETE FROM vendedor WHERE id = ?",(vendedorApaga))
            conexao.com.commit()
            print("vendedor demitido")
        elif(vendedorApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)
def deleteProduto():
    global produtoApaga
    produtoApaga =
    try:
        if(produtoApaga !=[]):
            conexao.cursor.execute("DELETE FROM produto WHERE id = ?",(produtoApaga))
            conexao.com.commit()
            print("produto removido do estoque")
        elif(produtoApaga == []):
            print("campo não preenchido")
    except sqlite3.Error as erro:
        print("erro ",erro)