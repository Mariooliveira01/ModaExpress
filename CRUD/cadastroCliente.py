import sqlite3
import conexao

def cadastro_cliente():
  try:
    conexao.conectar()
    nome = input("Informe seu Nome: ")
    sobrenome = input("Informe seu Sobrenome: ")
    cpf= input("Informe seu CPF: ")
    telefone = input("Informe seu Nº de Telefone: ")
    rua = input("Informe sua rua: ")
    numero = input("Informe o numero da sua casa: ")
    cidade = input("Informe sua Cidade: ")
    estado = input("Informe seu Estado: ")

    inserir_cliente = "INSERT INTO cliente VALUES ('"+nome+"', '"+sobrenome+"', '"+str(cpf)+"', '"+str(telefone)+"', '"+rua+"','"+str(numero)+"', '"+cidade+"', '"+estado+"')"
    conexao.cursor.execute(inserir_cliente)
    conexao.conn.commit()
    conexao.conn.close()
    print("CADASTRO FINALIZADO!")
  except sqlite3.Error as erro:
    print("Falha ao cadastrar")