import sqlite3
import conexao  # Módulo para lidar com a conexão ao banco de dados

# Função para deletar um cliente diretamente, fornecendo o CPF
def deleteCliente():
    conexao.conectar()  # Estabelece a conexão e o cursor
    cpf = input("Digite o CPF do cliente que deseja excluir: ")  # CPF fornecido pelo usuário

    try:
        # Executa a exclusão diretamente com base no CPF informado
        conexao.cursor.execute("DELETE FROM cliente WHERE cpf = ?", (cpf,))
        conexao.conn.commit()

        if conexao.cursor.rowcount > 0:  # Verifica se alguma linha foi afetada
            print(f"Cliente com CPF {cpf} removido com sucesso!")
        else:
            print(f"Nenhum cliente encontrado com o CPF {cpf}.")
    
    except sqlite3.Error as erro:
        print("Erro ao remover cliente:", erro)
    
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação


# Função para deletar um vendedor diretamente, fornecendo o ID
def deleteVendedor():
    conexao.conectar()  # Estabelece a conexão e o cursor
    id = input("Digite o ID do vendedor que deseja excluir: ")  # ID fornecido pelo usuário

    try:
        # Executa a exclusão diretamente com base no ID informado
        conexao.cursor.execute("DELETE FROM vendedor WHERE id = ?", (id,))
        conexao.conn.commit()

        if conexao.cursor.rowcount > 0:  # Verifica se alguma linha foi afetada
            print(f"Vendedor com ID {id} removido com sucesso!")
        else:
            print(f"Nenhum vendedor encontrado com o ID {id}.")
    
    except sqlite3.Error as erro:
        print("Erro ao remover vendedor:", erro)
    
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação


# Função para deletar um produto diretamente, fornecendo o ID
def deleteProduto():
    conexao.conectar()  # Estabelece a conexão e o cursor
    id = input("Digite o ID do produto que deseja excluir: ")  # ID fornecido pelo usuário

    try:
        # Executa a exclusão diretamente com base no ID informado
        conexao.cursor.execute("DELETE FROM produto WHERE id = ?", (id,))
        conexao.conn.commit()

        if conexao.cursor.rowcount > 0:  # Verifica se alguma linha foi afetada
            print(f"Produto com ID {id} removido do estoque com sucesso!")
        else:
            print(f"Nenhum produto encontrado com o ID {id}.")
    
    except sqlite3.Error as erro:
        print("Erro ao remover produto:", erro)
    
    finally:
        conexao.conn.close()  # Fecha a conexão após a operação
