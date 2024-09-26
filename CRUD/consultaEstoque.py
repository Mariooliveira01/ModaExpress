import sqlite3
from conexao import conectar  # Função para conectar ao banco de dados
import criar_tabela
conn = conectar()
cursor = conn.cursor()
criar_tabela.tabelaVendas()

def adicionar_item(id_produto, nome, quantidade, tamanho, valor, material, cor):
    """Adiciona ou atualiza um item no estoque."""
    cursor.execute("SELECT quantidade FROM estoque WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()

    if resultado:
        nova_quantidade = resultado[0] + quantidade
        cursor.execute(
            "UPDATE estoque SET quantidade = ?, tamanho = ?, valor = ?, material = ?, cor = ? WHERE id = ?",
            (nova_quantidade, tamanho, valor, material, cor, id_produto)
        )
    else:
        cursor.execute(
            "INSERT INTO estoque (id, nome, quantidade, tamanho, valor, material, cor) VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (id_produto, nome, quantidade, tamanho, valor, material, cor)
        )
    conn.commit()

def consultar_item(id_produto):
    """Consulta os detalhes de um item no estoque pelo ID."""
    cursor.execute("SELECT nome, quantidade, tamanho, valor, material, cor FROM estoque WHERE id = ?", (id_produto,))
    item = cursor.fetchone()

    if item:
        print(f"Item: {item}")
    else:
        print(f"Item com ID '{id_produto}' não encontrado.")

def listar_estoque():
    """Lista todos os itens no estoque."""
    cursor.execute("SELECT * FROM estoque")
    itens = cursor.fetchall()

    for item in itens:
        print(item)

def remover_item(id_produto, quantidade):
    """Remove uma quantidade de um item do estoque."""
    cursor.execute("SELECT quantidade FROM estoque WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()

    if resultado:
        nova_quantidade = resultado[0] - quantidade
        if nova_quantidade > 0:
            cursor.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
        else:
            cursor.execute("DELETE FROM estoque WHERE id = ?", (id_produto,))
        conn.commit()

def fechar_conexao():
    """Fecha a conexão com o banco de dados."""
    conn.close()
