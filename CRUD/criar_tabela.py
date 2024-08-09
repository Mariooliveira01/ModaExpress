import conexao
conexao.conectar()
def tabelaCliente():
    criarTabelaCliente = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, cpf integer, telefone integer, rua string, numero integer, cidade string, estado string)"
    conexao.cursor.execute(criarTabelaCliente)