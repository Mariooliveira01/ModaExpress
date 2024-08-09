import conexao
conexao.conectar()
<<<<<<< HEAD
def ():
=======
def tabelaCliente():
    criarTabelaCliente = "CREATE TABLE IF NOT EXISTS cliente(nome string, sobrenome string, cpf integer, telefone integer, rua string, numero integer, cidade string, estado string)"
    conexao.cursor.execute(criarTabelaCliente)
>>>>>>> 56552eacc24a4346294458698dddd70fea0fc26b
