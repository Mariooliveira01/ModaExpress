# Sistema de Gerenciamento de Estoque de Produtos
class Produto:
    def _init_(self, tipo, tamanho, quantidade):
        self.tipo = tipo
        self.tamanho = tamanho
        self.quantidade = quantidade

    def _str_(self):
        return f"{self.tipo} - Tamanho: {self.tamanho} - Quantidade: {self.quantidade}"


class Estoque:
    def _init_(self):
        self.produtos = []

    def cadastrar_produto(self, tipo, tamanho, quantidade):
        if self._verificar_produto_existe(tipo, tamanho):
            print(f"O produto {tipo} tamanho {tamanho} já está cadastrado.")
        else:
            novo_produto = Produto(tipo, tamanho, quantidade)
            self.produtos.append(novo_produto)
            print(f"Produto {tipo} tamanho {tamanho} cadastrado com sucesso.")

    def _verificar_produto_existe(self, tipo, tamanho):
        for produto in self.produtos:
            if produto.tipo == tipo and produto.tamanho == tamanho:
                return True
        return False

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.produtos:
                print(produto)

    def atualizar_quantidade(self, tipo, tamanho, nova_quantidade):
        for produto in self.produtos:
            if produto.tipo == tipo and produto.tamanho == tamanho:
                produto.quantidade = nova_quantidade
                print(f"Quantidade atualizada para {tipo} tamanho {tamanho} para {nova_quantidade}.")
                return
        print(f"Produto {tipo} tamanho {tamanho} não encontrado.")


def menu():
    estoque = Estoque()

    while True:
        print("\nSistema de Gerenciamento de Estoque")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Atualizar quantidade")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
             tipo = input("Digite o tipo do produto (camisa, calça, vestido, short): ").lower()
             tamanho = input("Digite o tamanho do produto (P, M, G, GG): ").upper()
             quantidade = int(input("Digite a quantidade: "))
             estoque.cadastrar_produto(tipo, tamanho, quantidade)

        elif escolha == "2":
            estoque.listar_produtos()

        elif escolha == "3":
            tipo = input("Digite o tipo do produto (camisa, calça, vestido, short): ").lower()
            tamanho = input("Digite o tamanho do produto (P, M, G, GG): ").upper()
            nova_quantidade = int(input("Digite a nova quantidade: "))
            estoque.atualizar_quantidade(tipo, tamanho, nova_quantidade)

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if "_name_" == "_main_":
    menu()