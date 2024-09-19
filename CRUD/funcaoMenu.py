def funcao_menu():
  print("BEM VINDO AO MODAEXPRESS!")
  print("______________")
  print("ESCOLHA SEU PERFIL: ")
  print("______________")
  print("1 - Sou Funcionário: \n2 - Sou Cliente:")
  
  global opcao 
  opcao = input()
  return opcao

def menu_estoque():
  print("_O QUE DESEJA FAZER?_")
  print("__________")
  print("""1 - Cadastrar Produto: \n 2 - Excluir Produto: \n 3 - Vendas: \n 4 - Atualizar Estoque: """)
  
  global opcao 
  opcao = input()
  return opcao

def menu_funcionario():
  print("O QUE DESEJA FAZER? ")
  print("""1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n 3 - Consultar Estoque: \n4 - Excluir minha conta:""")
  
  global opcao 
  opcao = input()
  return opcao

def menu_cliente():
  print("O QUE DESEJA FAZER? ")
  print("""1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n3 - Compras: \n 4 - Excluir minha conta:""" )
  
  global opcao
  opcao=input()
  return opcao