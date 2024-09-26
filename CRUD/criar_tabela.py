import sqlite3
import conexao

def tabelaCliente():
    """Cria a tabela cliente se não existir."""
    conexao.conectar()  # Conecta ao banco de dados
    criarTabelaCliente = '''CREATE TABLE IF NOT EXISTS cliente(nome TEXT, sobrenome TEXT, cpf INTEGER, telefone INTEGER, rua TEXT, numero INTEGER, cidade TEXT, estado TEXT)'''
    conexao.cursor.execute(criarTabelaCliente)

def tabelaProduto():
    """Cria a tabela produto se não existir."""
    conexao.conectar()
    criarTabelaProduto = '''CREATE TABLE IF NOT EXISTS produto(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, quantidade INTEGER, tamanho TEXT, valor INTEGER, material TEXT, cor TEXT)'''
    conexao.cursor.execute(criarTabelaProduto)

def tabelaVendedor():
    """Cria a tabela vendedor se não existir."""
    conexao.conectar()
    criarTabelaVendedor = '''CREATE TABLE IF NOT EXISTS vendedor(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT, cpf INTEGER)'''
    conexao.cursor.execute(criarTabelaVendedor)

def tabelaVendas():
    """Cria a tabela vendas se não existir."""
    conexao.conectar()
    criarTabelaVendas = '''CREATE TABLE IF NOT EXISTS Vendas(id INTEGER PRIMARY KEY AUTOINCREMENT, produto_id INTEGER NOT NULL, quantidade INTEGER NOT NULL, data TEXT NOT NULL, valor_total REAL NOT NULL, FOREIGN KEY(produto_id) REFERENCES produto(id)'''
    conexao.cursor.execute(criarTabelaVendas)
