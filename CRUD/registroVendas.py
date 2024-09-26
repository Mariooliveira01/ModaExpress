import sqlite3
import conexao

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("Gestao_Moda_Express.db")
cursor = conexao.cursor()

# Criar a tabela de estoque, se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
''')
conexao.commit()

def adicionar_item(nome, quantidade):
    cursor.execute("SELECT quantidade FROM estoque WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    
    if resultado:
        nova_quantidade = resultado[0] + quantidade
        cursor.execute("UPDATE estoque SET quantidade = ? WHERE nome = ?", (nova_quantidade, nome))
        print(f"Atualizado: {quantidade} unidades adicionadas ao item '{nome}'. Total: {nova_quantidade}.")
    else:
        cursor.execute("INSERT INTO estoque (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        print(f"Adicionado: {quantidade} unidades do item '{nome}'.")
    
    conexao.commit()

def consultar_item(nome):
    cursor.execute("SELECT quantidade FROM estoque WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"O item '{nome}' tem {resultado[0]} unidades no estoque.")
    else:
        print(f"O item '{nome}' não foi encontrado no estoque.")

def listar_estoque():
    cursor.execute("SELECT nome, quantidade FROM estoque")
    itens = cursor.fetchall()
    
    if itens:
        print("Estoque atual:")
        for item in itens:
            print(f"- {item[0]}: {item[1]} unidades")
    else:
        print("O estoque está vazio.")

def remover_item(nome, quantidade):
    cursor.execute("SELECT quantidade FROM estoque WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    
    if resultado:
        nova_quantidade = resultado[0] - quantidade
        if nova_quantidade > 0:
            cursor.execute("UPDATE estoque SET quantidade = ? WHERE nome = ?", (nova_quantidade, nome))
            print(f"{quantidade} unidades removidas do item '{nome}'. Total restante: {nova_quantidade}.")
        elif nova_quantidade == 0:
            cursor.execute("DELETE FROM estoque WHERE nome = ?", (nome,))
            print(f"O item '{nome}' foi removido completamente do estoque.")
        else:
            print(f"Quantidade insuficiente de '{nome}' no estoque para remover.")
    else:
        print(f"O item '{nome}' não foi encontrado no estoque.")

    conexao.commit()