import sqlite3
import conexao

def menu_funcionario():
  print("O QUE DESEJA FAZER? ")
  print("""1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n 3 - Consultar Estoque: \n4 - Excluir minha conta:""")
  
  global opcao 
  opcao = input()
  return opcao


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