from funcaoMenu import funcao_menu, menu_cliente, menu_funcionario, menu_estoque
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
                menu_funcionario()
            elif opcao_funcionario == '2':
                update.atualizarVendedor()
                menu_funcionario()
            elif opcao_funcionario == '3':
               # CONSULTA ESTOQUE
                opcao_estoque = menu_estoque()
                while opcao_estoque <= '4':
                    if opcao_estoque == '1':
                        cadastroProdutos.cadastro_produto()
                    elif opcao_estoque == '2':
                        delete.deleteProduto()
                    elif opcao_estoque == '3':
                        registroVendas.registrar_venda()
                    elif opcao_estoque == '4':
                        update.atualizarProduto()
                    else:
                        print("não funcionou")
                    opcao_estoque = menu_estoque()  # Atualiza a opção do menu de estoque
                menu_funcionario()

            elif opcao_funcionario == '4':
                delete.deleteVendedor()
                menu_funcionario()
            elif opcao_funcionario == '5':
                funcao_menu()


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
            elif opcao_funcionario == '5':
                funcao_menu()

            opcao_cliente = menu_cliente()  # Atualiza a opção do menu de cliente
    opcao = funcao_menu()  # Atualiza a opção do menu principal