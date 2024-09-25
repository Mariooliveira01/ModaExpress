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
        # MENU FUNCIONÁRIO
        opcao_funcionario = menu_funcionario()
        while opcao_funcionario != '6':
            if opcao_funcionario == '1':
                cadastrarFuncionario.cadastro_funcionario()
            elif opcao_funcionario == '2':
                update.atualizarVendedor()
            elif opcao_funcionario == '3':
                # CONSULTA ESTOQUE
                opcao_estoque = menu_estoque()
                while opcao_estoque != '5':
                    if opcao_estoque == '1':
                        cadastroProdutos.cadastro_produtos()
                    elif opcao_estoque == '2':
                        delete.deleteProduto()
                    elif opcao_estoque == '3':
                        registroVendas.vendas()
                    elif opcao_estoque == '4':
                        update.atualizarProduto()
                    opcao_estoque = menu_estoque()  # Atualiza a opção do menu de estoque
            elif opcao_funcionario == '5':
                delete.deleteVendedor()
            opcao_funcionario = menu_funcionario()  # Atualiza a opção do menu de funcionário
    elif opcao == '2':
        # MENU CLIENTE
        opcao_cliente = menu_cliente()
        while opcao_cliente != '4':
            if opcao_cliente == '1':
                cadastroCliente.cadastro_cliente()
            elif opcao_cliente == '2':
                update.atualizarCliente()
            elif opcao_cliente == '3':
                delete.deleteCliente()
            opcao_cliente = menu_cliente()  # Atualiza a opção do menu de cliente
    opcao = funcao_menu()  # Atualiza a opção do menu principal
