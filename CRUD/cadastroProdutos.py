import sqlite3
import conexao
class Produto:

    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def salvarProduto(self):
        conexao.conectar()
        conn = sqlite3.connect('Gestao_Moda_Express.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produto (nome, quantidade, preco) VALUES (?, ?, ?)',(self.nome, self.quantidade, self.preco))
        conexao.conn.commit()
        conexao.conn.close()

    @staticmethod
    def atualizarProduto(id, quantidade=None, preco=None):
        conexao.conectar()
        conn = sqlite3.connect('Gestao_Moda_Express.db')
        cursor = conn.cursor()
        if quantidade is not None:
            cursor.execute('UPDATE produto SET quantidade = ? WHERE id = ?',(quantidade, id))
        if preco is not None:
            cursor.execute('UPDATE produto SET preco = ? WHERE id = ?',(preco, id))
        conexao.conn.commit()
        conexao.conn.close()

    @staticmethod
    def consultarProduto():
        conexao.conectar()
        conn = sqlite3.connect('Gestao_Moda_Express.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Produto')
        produtos = cursor.fetchall()
        conexao.conn.close()
        return produtos