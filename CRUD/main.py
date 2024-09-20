import sqlite3
import conexao
import funcaoMenu
import cadastrarFuncionario
import cadastroCliente
import cadastroProdutos
import consultaEstoque
import criar_tabela
import registroVendas
import delete
import update

<<<<<<< HEAD

=======
>>>>>>> c48c45e5fbdf94ea35055ba763cb3a4228764fe9
criar_tabela.tabelaCliente()
criar_tabela.tabelaProduto()
criar_tabela.tabelaVendedor()

#MENU INICIAL(1- FUNCIONARIO / 2 - CLIENTE)#
opcao = funcaoMenu.funcao_menu()
while (opcao!='3'):
  if(opcao =='1'):
    funcaoMenu.menu_funcionario()
  elif(opcao =='2'):
    funcaoMenu.menu_cliente()
  else:
    print("Opção Indisponível!")

<<<<<<< HEAD
#O QUE DESEJA FAZER? PARA CLIENTE#
opcao = funcaoMenu.menu_cliente()
=======
  #O QUE DESEJA FAZER? PARA CLIENTE#
opcao = cadastroCliente.cadastro_cliente()
>>>>>>> c48c45e5fbdf94ea35055ba763cb3a4228764fe9
while (opcao!='5'):
  if(opcao =='1'):
    cadastroCliente.cadastro_cliente()
  elif(opcao =='2'):
    update.atualizarCliente()
  elif(opcao =='3'):
    comprar.comprar()
  elif(opcao =='4'):
    delete.deleteCliente()
  else:
    print("Opção Indisponível!")
  
  
#O QUE DESEJA FAZER? PARA FUNCIONARIO#
opcao = cadastrarFuncionario.cadastro_funcionario()
while (opcao!='5'):
  if(opcao =='1'):
    cadastrarFuncionario.cadastro_funcionario()
  elif(opcao =='2'):
    update.atualizarVendedor()
  elif(opcao =='3'):
    consultaEstoque.menu_estoque()
  elif(opcao =='4'):
    delete.deleteVendedor()
  else:
    print("Opção Indisponível!")


#CASO O FUNCIONARIO  QUEIRA CONSULTAR O ESTOQUE (FUNÇÃO "consulta_estoque")#
opcao = funcaoMenu.menu_estoque()
while (opcao!='5'):
  if (opcao == '1'):
    cadastroProdutos.cadastro_produtos()
  elif(opcao =='2'):
    delete.deleteProduto
  elif(opcao == '3'):
    registroVendas.vendas
  elif (opcao =='4'):
    update.atualizarProduto
  else:
    print("Opção Indisponível!")