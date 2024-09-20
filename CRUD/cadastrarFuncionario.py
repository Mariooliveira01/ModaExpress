import sqlite3
import conexao

def cadastro_funcionario():
  try:
    conexao.conectar()
    nome = input("Informe seu Nome: ")
    sobrenome = input("Informe seu Sobrenome: ")
    cpf= input("Informe seu CPF: ")

    inserir_funcionario = "INSERT INTO vendedor VALUES ('"+nome+"', '"+sobrenome+"','"+str(cpf)+"')"
    conexao.cursor.execute(inserir_funcionario)
    conexao.conn.commit()
    conexao.conn.close()
    print("CADASTRO FINALIZADO!")
  except sqlite3.Error as erro:
    print(" ###### ERRO AO CADASTRAR ######")