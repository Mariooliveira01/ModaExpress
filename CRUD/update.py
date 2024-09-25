import sqlite3
import conexao


# Função para atualizar os dados de um usuário com base no CPF
def atualizarCliente():
    conexao.conectar()

    cpf = input("Digite o CPF do usuário que deseja atualizar: ")

    # Verifica se o CPF existe no banco de dados
    conexao.cursor.execute('SELECT COUNT(*) FROM cliente WHERE cpf = ?', (cpf,))
    exists = conexao.cursor.fetchone()[0]  # Retorna a contagem

    if exists > 0:
        # Coleta as novas informações do usuário
        nomeNovo = input("Novo nome: ")
        sobrenomeNovo = input("Novo sobrenome: ")
        telefoneNovo = input("Novo telefone: ")
        ruaNovo = input("Nova rua: ")
        numeroDaRuaNovo = input("Novo número: ")
        cidadeNovo = input("Nova cidade: ")
        estadoNovo = input("Novo estado: ")

        # Monta a consulta de atualização
        consulta = 'UPDATE cliente SET '
        params = []

        if nomeNovo:
            consulta += 'nome = ?, '
            params.append(nomeNovo)
        if sobrenomeNovo:
            consulta += 'sobrenome = ?, '
            params.append(sobrenomeNovo)
        if telefoneNovo:
            consulta += 'telefone = ?, '
            params.append(telefoneNovo)
        if ruaNovo:
            consulta += 'rua = ?, '
            params.append(ruaNovo)
        if numeroDaRuaNovo:
            consulta += 'numero = ?, '
            params.append(numeroDaRuaNovo)
        if cidadeNovo:
            consulta += 'cidade = ?, '
            params.append(cidadeNovo)
        if estadoNovo:
            consulta += 'estado = ?, '
            params.append(estadoNovo)

        # Remove a última vírgula e espaço
        consulta = consulta.rstrip(', ')

        # Adiciona a cláusula WHERE para identificar o registro com o CPF
        consulta += ' WHERE cpf = ?'
        params.append(cpf)

        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.conn.commit()
        print("Dados atualizados com sucesso!")
    else:
        print("CPF não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.conn.close()


# Função para atualizar os dados de um Vendedor com base no ID
def atualizarVendedor():
    conexao.conectar()

    id = input("Digite o ID do vendedor que deseja atualizar: ")

    # Verifica se o ID existe no banco de dados
    conexao.cursor.execute('SELECT COUNT(*) FROM vendedor WHERE id = ?', (id,))
    exists = conexao.cursor.fetchone()[0]

    if exists > 0:
        # Coleta as novas informações do vendedor
        nomeNovo = input("Novo nome: ")
        sobrenomeNovo = input("Novo sobrenome: ")
        cpfNovo = input("Novo CPF: ")

        # Monta a consulta de atualização
        consulta = 'UPDATE vendedor SET '
        params = []

        if nomeNovo:
            consulta += 'nome = ?, '
            params.append(nomeNovo)
        if sobrenomeNovo:
            consulta += 'sobrenome = ?, '
            params.append(sobrenomeNovo)
        if cpfNovo:
            consulta += 'cpf = ?, '
            params.append(cpfNovo)

        # Remove a última vírgula e espaço
        consulta = consulta.rstrip(', ')

        # Adiciona a cláusula WHERE para identificar o registro com o ID
        consulta += ' WHERE id = ?'
        params.append(id)

        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.conn.commit()
        print("Dados do vendedor atualizados com sucesso!")
    else:
        print("ID não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.conn.close()


# Função para atualizar os dados de um Produto com base no ID
def atualizarProduto():
    conexao.conectar()

    id = input("Digite o ID do produto que deseja atualizar: ")

    # Verifica se o ID do produto existe no banco de dados
    conexao.cursor.execute('SELECT COUNT(*) FROM produto WHERE id = ?', (id,))
    exists = conexao.cursor.fetchone()[0]

    if exists > 0:
        # Coleta as novas informações do produto
        modeloNovo = input("Novo modelo: ")
        quantidadeNovo = int(input("Nova quantidade: "))  # Corrigido o input
        tamanhoNovo = input("Novo tamanho: ")
        valorNovo = input("Novo valor: ")
        materialNovo = input("Novo material: ")
        corNovo = input("Nova cor: ")

        # Monta a consulta de atualização
        consulta = 'UPDATE produto SET '
        params = []

        if modeloNovo:
            consulta += 'modelo = ?, '
            params.append(modeloNovo)
        if quantidadeNovo:
            consulta += 'quantidade = ?, '
            params.append(quantidadeNovo)
        if tamanhoNovo:
            consulta += 'tamanho = ?, '
            params.append(tamanhoNovo)
        if valorNovo:
            consulta += 'valor = ?, '
            params.append(valorNovo)
        if materialNovo:
            consulta += 'material = ?, '
            params.append(materialNovo)
        if corNovo:
            consulta += 'cor = ?, '
            params.append(corNovo)

        # Remove a última vírgula e espaço
        consulta = consulta.rstrip(', ')

        # Adiciona a cláusula WHERE para identificar o registro com o ID
        consulta += ' WHERE id = ?'
        params.append(id)

        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.conn.commit()
        print("Dados do produto atualizados com sucesso!")
    else:
        print("ID do produto não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.conn.close()