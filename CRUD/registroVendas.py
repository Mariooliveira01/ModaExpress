import sqlite3
import criar_tabela  # Certifique-se de que esta importação está correta

def setup():
    """Configura o banco de dados, criando a tabela de vendas."""
    criar_tabela.tabelaVendas()

def consultar_venda_cliente():import sqlite3
import criar_tabela  # Certifique-se de que esta importação está correta

def setup():
    """Configura o banco de dados, criando a tabela de vendas."""
    criar_tabela.tabelaVendas()

def consultar_venda_cliente():
    """Consulta todas as vendas registradas na tabela cliente."""
    setup()  # Garante que a tabela de vendas existe
    with sqlite3.connect('Gestao_Moda_Express.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cliente')
        vendas = cursor.fetchall()
    return vendas

def registrar_venda(produto_id, quantidade, valor_total):
    """Registra uma nova venda no banco de dados e atualiza o estoque do produto."""
    setup()  # Garante que a tabela de vendas existe
    print(f"Produto ID: {produto_id}, Quantidade: {quantidade}, Valor Total: {valor_total}")
    
    with sqlite3.connect('Gestao_Moda_Express.db') as conn:
        cursor = conn.cursor()
        
        # Insere a venda na tabela Vendas
        cursor.execute('INSERT INTO vendas (produto_id, quantidade, data, valor_total) VALUES (?, ?, date("now"), ?)', (produto_id, quantidade, valor_total))
        
        # Atualiza o estoque na tabela Produto
        cursor.execute('UPDATE produto SET quantidade = quantidade - ? WHERE id = ?', (quantidade, produto_id))

def consultar_venda():
    """Consulta todas as vendas registradas na tabela vendas."""
    setup()  # Garante que a tabela de vendas existe
    with sqlite3.connect('Gestao_Moda_Express.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vendas')
        vendas = cursor.fetchall()
    return vendas


def registrar_venda(produto_id, quantidade, valor_total):
    """Registra uma nova venda no banco de dados e atualiza o estoque do produto."""
    setup()  # Garante que a tabela de vendas existe
    print(f"Produto ID: {produto_id}, Quantidade: {quantidade}, Valor Total: {valor_total}")
    
    with sqlite3.connect('Gestao_Moda_Express.db') as conn:
        cursor = conn.cursor()
        
        # Insere a venda na tabela Vendas
        cursor.execute('INSERT INTO vendas (produto_id, quantidade, data, valor_total) VALUES (?, ?, date("now"), ?)', (produto_id, quantidade, valor_total))
        
        # Atualiza o estoque na tabela Produto
        cursor.execute('UPDATE produto SET quantidade = quantidade - ? WHERE id = ?', (quantidade, produto_id))

def consultar_venda():
    """Consulta todas as vendas registradas na tabela vendas."""
    setup()  # Garante que a tabela de vendas existe
    with sqlite3.connect('Gestao_Moda_Express.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vendas')
        vendas = cursor.fetchall()
    return vendas

