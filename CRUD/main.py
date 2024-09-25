import sqlite3
from funcaoMenu import funcao_menu, menu_cliente, menu_funcionario, menu_estoque
import conexao
from criar_tabela import tabelaVendedor, tabelaCliente
import cadastrarFuncionario
import cadastroCliente
import cadastroProdutos
import consultaEstoque
import registroVendas
import delete
import update
import select

# MENU INICIAL (1 - FUNCIONÁRIO / 2 - CLIENTE) #
opcao = funcao_menu()
while opcao != '3':
    if opcao == '1':
        menu_funcionario()
    elif opcao == '2':
        menu_cliente()

# MENU CLIENTE #
opcao = menu_cliente()
while opcao != '4':
    if opcao == '1':
        cadastroCliente.cadastro_cliente()
    elif opcao == '2':
        update.atualizarCliente()
    elif opcao == '3':
        delete.deleteCliente()

# MENU FUNCIONÁRIO #
opcao = menu_funcionario()
while opcao != '5':
    if opcao == '1':
        cadastrarFuncionario.cadastro_funcionario()
    elif opcao == '2':
        update.atualizarVendedor()
    elif opcao == '3':
        consultaEstoque.menu_estoque()
    elif opcao == '4':
        delete.deleteVendedor()

# CONSULTA ESTOQUE #
opcao = menu_estoque()
while opcao != '5':
    if opcao == '1':
        cadastroProdutos.cadastro_produtos()
    elif opcao == '2':
        delete.deleteProduto()
    elif opcao == '3':
        registroVendas.vendas()
    elif opcao == '4':
        update.atualizarProduto()