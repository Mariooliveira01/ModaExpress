import sqlite3
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def salvarProduto(self):
        conn = sqlite3.connect('moda_express.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Produtos (nome, quantidade, preco) VALUES (?, ?, ?)', 
                       (self.nome, self.quantidade, self.preco))
        conn.commit()
        conn.close()

    @staticmethod
    def atualizarProduto(id, quantidade=None, preco=None):
        conn = sqlite3.connect('moda_express.db')
        cursor = conn.cursor()
        if quantidade is not None:
            cursor.execute('UPDATE Produtos SET quantidade = ? WHERE id = ?', 
                           (quantidade, id))
        if preco is not None:
            cursor.execute('UPDATE Produtos SET preco = ? WHERE id = ?', 
                           (preco, id))
        conn.commit()
        conn.close()

    @staticmethod
    def excluirProduto(id):
        conn = sqlite3.connect('moda_express.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Produtos WHERE id = ?', (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def consultarProduto():
        conn = sqlite3.connect('moda_express.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produtos')
        produtos = cursor.fetchall()
        conn.close()
        return produtos