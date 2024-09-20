import sqlite3
import conexao

def criar_banco():
    conn = sqlite3.connect('Gestao_Moda_Express.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,quantidade INTEGER NOT NULL,preco REAL NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (id INTEGER PRIMARY KEY AUTOINCREMENT,produto_id INTEGER NOT NULL,quantidade INTEGER NOT NULL,data TEXT NOT NULL,valor_total REAL NOT NULL,FOREIGN KEY(produto_id) REFERENCES Produtos(id))''')

    conn.commit()
    conn.close()

criar_banco()


def consultarVenda():
        com = sqlite3.connect('Gestao_Moda_Express.db')
        cursor = com.cursor()
        cursor.execute('SELECT * FROM cliente')
        vendas = cursor.fetchall()
        com.close()
        return vendas


def registrarVenda(self):
    print(f"Produto ID: {self.produto_id},Quantidade: {self.quantidade},Valor Total: {self.valor_total}")
    conn = sqlite3.connect('Gestao_Moda_Express.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Vendas (produto_id, quantidade, data, valor_total) VALUES (?, ?, date("now"), ?)', (self.produto_id, self.quantidade, self.valor_total))
        
    # Atualiza o estoque
    cursor.execute('UPDATE Produtos SET quantidade = quantidade - ? WHERE id = ?',(self.quantidade, self.produto_id))

    conn.commit()
    conn.close()

def consultarVenda():
    conn = sqlite3.connect('Gestao_Moda_Express.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vendas')
    vendas = cursor.fetchall()
    conn.close()
    return vendas