import sqlite3
import conexao

#MENU INICIAL PARA CLIENTE (se ele escolher o perfil 'Sou cliente')#

def menu_cliente():
  print("O QUE DESEJA FAZER? ")
  print("""1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n3 - Compras: \n 4 - Excluir minha conta:""" )
  
  global opcao
  opcao=input()
  return opcao


#CADASTRO DE CLENTE(se ele FOR SE CADASTRAR)#

def cadastro_cliente():
  try:
    conexao.conectar()
    nome = input("Informe seu Nome: ")
    sobrenome = input("Informe seu Sobrenome: ")
    idade = input("Informe sua Idade: ")
    cpf= input("Informe seu CPF: ")
    telefone = input("Informe seu Nº de Telefone: ")
    endereco = input("Informe seu Endereço: ")
    cidade = input("Informe sua Cidade: ")
    estado = input("Informe seu Estado: ")

    inserir_cliente = "INSERT INTO cliente VALUES ('"+nome+"', '"+sobrenome+"','"+str(idade)+"'"
    conexao.cursor.execute(inserir_cliente)
    conexao.conn.commit()
    conexao.conn.close()
    print("CADASTRO FINALIZADO!")
  except sqlite3.Error as erro:
    print(" ###### ERRO AO CADASTRAR ######")