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
    global vendedorApaga

def deleteProduto():
    global produtoApaga