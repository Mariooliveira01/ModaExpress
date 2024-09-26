def funcao_menu():
  print("BEM VINDO AO MODAEXPRESS!")
  print("______________")
  print("ESCOLHA SEU PERFIL:")
  print("______________")
  print("1 - Sou Funcionário:\n2 - Sou Cliente:")
  
  global opcao 
  opcao = input()
  return opcao

def menu_estoque():
  print("_O QUE DESEJA FAZER NO ESTOQUE?_")
  print("__________")
  print("""1 - Cadastrar Produto: \n 2 - Excluir Produto: \n 3 - Atualizar Estoque: """)
  
  global opcao 
  opcao = input()
  return opcao

def menu_funcionario():
  print("O QUE DESEJA FAZER FUNCIONARIO? ")
  print("1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n 3 - Consultar Estoque: \n4 - Excluir minha conta: \n5 - voltar")
  
  global opcao 
  opcao = input()
  return opcao

def menu_cliente():
  print("O QUE DESEJA FAZER CLIENTE? ")
  print("1 - Cadastre-se: \n2 - Alterar dados Cadastrais: \n 3 - Excluir minha conta: \n4 - voltar")
  
  global opcao
  opcao=input()
  return opcao