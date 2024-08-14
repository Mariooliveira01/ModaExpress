import conexao
conexao.conectar()

def tabelaCliente():
    criarTabelaCliente = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, cpf integer, telefone integer, rua string, numero integer, cidade string, estado string)"
    conexao.cursor.execute(criarTabelaCliente)

def tabelaProduto():
    criarTabelaProduto = "CREATE TABLE IF NOT EXISTS produto(id integer primary key autoincrement, nome string, quantidade integer, tamanho string, valor integer, material string, cor string)"
    conexao.cursor.execute(criarTabelaProduto)

def tabelaVendedor():
    criarTabelaVendedor = "CREATE TABLE IF NOT EXISTS vendedor(id integer primary key autoincrement, nome string, sobrenome string, cpf integer)"
    conexao.cursor.execute(criarTabelaVendedor)