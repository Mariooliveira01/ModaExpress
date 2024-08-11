import sqlite3
import conexao


# Função para atualizar os dados de um usuário com base no CPF
def atualizarCliente():
    conexao.conectar()

    cpf = input("Digite o CPF do usuário que deseja atualizar: ")
    
    conexao.cursor.execute('SELECT COUNT(*) FROM cliente WHERE cpf = ?', (cpf,))

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

    # Verifica se o CPF existe no banco de dados
    exists = [0]

    if exists > 0:
        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.com.commit()
        print("Dados atualizados com sucesso!")
    else:
        print("CPF não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.com.close()


def atualizarVendedor():
    conexao.conectar()

    id = input("Digite o CPF do usuário que deseja atualizar: ")
    conexao.cursor.execute('SELECT COUNT(*) FROM vendedor WHERE id = ?', (id,))

    # Coleta as novas informações do usuário
    nomeNovo = input("Novo nome: ")
    sobrenomeNovo = input("Novo sobrenome: ")
    cpfNovo = input("Novo cpf: ")

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

    # Adiciona a cláusula WHERE para identificar o registro com o CPF
    consulta += ' WHERE id = ?'
    params.append(id)

    # Verifica se o CPF existe no banco de dados
    exists = [0]

    if exists > 0:
        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.com.commit()
        print("Dados atualizados com sucesso!")
    else:
        print("ID não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.com.close()


def atualizarProduto():
    conexao.conectar()

    id = input("Digite o CPF do usuário que deseja atualizar: ")
    conexao.cursor.execute('SELECT COUNT(*) FROM produto WHERE id = ?', (id,))

    # Coleta as novas informações do usuário
    modeloNovo = input("Novo modelo: ")
    quantidadeNovo = input(int("Nova quantidade: "))
    tamanhoNovo = input("Novo tamanho: ")
    valorNovo = input("Nova valor: ")
    materialNovo = input("Novo material: ")
    corNovo = input("Nova cor: ")

    # Monta a consulta de atualização
    consulta = 'UPDATE produto SET '
    params = []

    if modeloNovo:
        consulta += 'nome = ?, '
        params.append(modeloNovo)
    if quantidadeNovo:
        consulta += 'sobrenome = ?, '
        params.append(quantidadeNovo)
    if tamanhoNovo:
        consulta += 'telefone = ?, '
        params.append(tamanhoNovo)
    if valorNovo:
        consulta += 'rua = ?, '
        params.append(valorNovo)
    if materialNovo:
        consulta += 'numero = ?, '
        params.append(materialNovo)
    if corNovo:
        consulta += 'cidade = ?, '
        params.append(corNovo)

    # Remove a última vírgula e espaço
    consulta = consulta.rstrip(', ')

    # Adiciona a cláusula WHERE para identificar o registro com o CPF
    consulta += ' WHERE id = ?'
    params.append(id)

    # Verifica se o CPF existe no banco de dados
    exists = [0]

    if exists > 0:
        # Executa a consulta de atualização
        conexao.cursor.execute(consulta, tuple(params))
        conexao.com.commit()
        print("Dados atualizados com sucesso!")
    else:
        print("ID não encontrado. Nenhuma atualização foi feita.")

    # Fecha a conexão com o banco de dados
    conexao.com.close()