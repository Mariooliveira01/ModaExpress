import sqlite3  # Importa o módulo sqlite3 para lidar com o banco de dados
import conexao  # Importa o módulo de conexão (deve conter a função para conectar ao banco)
import criar_tabela  # Importa o módulo que cria as tabelas (deve conter a função criarTabelaProduto)

def cadastro_produto():
    try:
        # Conecta ao banco de dados
        conexao.conectar()
        
        # Chama a função para criar a tabela (caso ainda não tenha sido criada)
        criar_tabela.tabelaProduto()

        # Coleta as informações do produto
        nome = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade: "))
        tamanho = input("Informe o tamanho: ")
        valor = float(input("Informe o valor: "))
        material = input("Informe o material: ")
        cor = input("Informe a cor: ")

        # Consulta para inserir os dados na tabela
        inserir_produto = """
        INSERT INTO tabelaProduto ( nome TEXT, quantidade INTEGER, tamanho TEXT, valor INTEGER, material TEXT, cor TEXT)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # Executa a consulta de inserção com os valores fornecidos
        conexao.cursor.execute(inserir_produto, (nome, quantidade, tamanho, valor, material, cor))
        
        # Confirma a transação no banco de dados
        conexao.conn.commit()
        print("Produto cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar produto:", erro)

    finally:
        # Fecha a conexão com o banco de dados
        conexao.conn.close()
