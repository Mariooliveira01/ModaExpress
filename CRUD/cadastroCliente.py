import sqlite3
import conexao
import criar_tabela

def cadastro_cliente():
    try:
        conexao.conectar()
        
        # Criar a tabela se não existir
        criar_tabela.tabelaCliente()
        
        # Coletando informações do cliente
        nome = input("Informe seu Nome: ")
        sobrenome = input("Informe seu Sobrenome: ")
        cpf = input("Informe seu CPF: ")
        telefone = input("Informe seu Nº de Telefone: ")
        rua = input("Informe sua Rua: ")
        numero = input("Informe o Número da sua Casa: ")
        cidade = input("Informe sua Cidade: ")
        estado = input("Informe seu Estado: ")

        # Consulta SQL utilizando placeholders
        inserir_cliente = """
        INSERT INTO cliente (nome, sobrenome, cpf, telefone, rua, numero, cidade, estado) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Executando a consulta com os dados do cliente
        conexao.cursor.execute(inserir_cliente, (nome, sobrenome, cpf, telefone, rua, numero, cidade, estado))
        
        # Comitando as alterações
        conexao.conn.commit()
        print("CADASTRO FINALIZADO!")
        
    except sqlite3.Error as erro:
        print("Falha ao cadastrar:", erro)
    finally:
        # Garantindo que a conexão será fechada
        if conexao.conn:
            conexao.conn.close()