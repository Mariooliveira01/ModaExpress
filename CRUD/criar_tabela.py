import sqlite3
import conexao

def tabelaCliente():
    """Cria a tabela cliente se não existir."""
    conn = conexao.conectar()  # Conecta ao banco de dados
    cursor = conn.cursor()
    criarTabelaCliente = '''CREATE TABLE IF NOT EXISTS cliente(nome TEXT, sobrenome TEXT, cpf INTEGER, telefone INTEGER, rua TEXT, numero INTEGER, cidade TEXT, estado TEXT)'''
    cursor.execute(criarTabelaCliente)
    conn.commit()
    #conn.close()  # Fecha a conexão

def tabelaProduto():
    """Cria a tabela produto se não existir."""
    conn = conexao.conectar()
    cursor = conn.cursor()
    criarTabelaProduto = '''CREATE TABLE IF NOT EXISTS produto(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, quantidade INTEGER, tamanho TEXT, valor INTEGER, material TEXT, cor TEXT)'''
    cursor.execute(criarTabelaProduto)
    conn.commit()
    #conn.close()

def tabelaVendedor():
    """Cria a tabela vendedor se não existir."""
    conn = conexao.conectar()
    cursor = conn.cursor()
    criarTabelaVendedor = '''CREATE TABLE IF NOT EXISTS vendedor(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT, cpf INTEGER)'''
    cursor.execute(criarTabelaVendedor)
    conn.commit()
    #conn.close()

def tabelaVendas():
    """Cria a tabela vendas se não existir."""
    conn = conexao.conectar()
    cursor = conn.cursor()
    criarTabelaVendas = '''CREATE TABLE IF NOT EXISTS Vendas(id INTEGER PRIMARY KEY AUTOINCREMENT, produto_id INTEGER NOT NULL, quantidade INTEGER NOT NULL, data TEXT NOT NULL, valor_total REAL NOT NULL, FOREIGN KEY(produto_id) REFERENCES produto(id)'''
    cursor.execute(criarTabelaVendas)
    conn.commit()
    conn.close()
