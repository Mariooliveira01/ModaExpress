import sqlite3
import conexao
import funcaoMenu
import cadastrarFuncionario
import cadastroCliente
import cadastroProdutos
import criar_tabela
import registroVendas
import delete
import update

#MENU INICIAL(1- FUNCIONARIO / 2 - CLIENTE)#

opcao = funcaoMenu()
if(opcao =='1'):
  cadastrarFuncionario.menu_funcionario()
elif(opcao =='2'):
  cadastroCliente.menu_cliente()
else:
  print("Opção Indisponível!")

#O QUE DESEJA FAZER? PARA CLIENTE#

opcao = menu_cliente()
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

opcao = menu_funcionario()
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

opcao = menu_estoque()
if (opcao == '1'):
  cadastroProdutos.cadastro_produtos()
elif(opcao =='2'):
  delete.deleteProduto
elif(opcao == '3'):
  vendas.vendas
elif (opcao =='4'):
  update.atualizarProduto
else:
  print("Opção Indisponível!")