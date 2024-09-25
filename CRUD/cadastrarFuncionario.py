import sqlite3
import conexao
import criar_tabela

def cadastro_funcionario():
    try:
        conexao.conectar()
        criar_tabela.tabelaVendedor()  # Certifique-se de que a tabela existe

        nome = input("Informe seu Nome: ")
        sobrenome = input("Informe seu Sobrenome: ")
        cpf = input("Informe seu CPF: ")

        # Consulta com placeholders para prevenir injeção de SQL
        inserir_funcionario = "INSERT INTO vendedor (nome, sobrenome, cpf) VALUES (?, ?, ?)"
        
        # Executa a consulta com os dados como parâmetros
        conexao.cursor.execute(inserir_funcionario, (nome, sobrenome, cpf))
        conexao.conn.commit()  # Confirma as alterações
        conexao.conn.close()   # Fecha a conexão

        print("CADASTRO FINALIZADO!")
    
    except sqlite3.Error as erro:
        print("###### ERRO AO CADASTRAR ######", erro)

