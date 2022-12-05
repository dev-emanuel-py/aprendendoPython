class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def mostra_nome(self):
        return self.__nome

    def mostra_idade(self):
        return self.__idade

    def mostra_altura(self):
        return self.__altura

    def modifica_nome(self, novo_nome):
        self.__nome = novo_nome

    def modifica_idade(self, nova_idade):
        self.__idade = nova_idade

    def modifica_altura(self, nova_altura):
        self.__altura = nova_altura

    def mostra_infor(self):
        print(self.__nome)
        print(self.__idade)
        print(self.__altura)


pessoa1 = Pessoa('Emanuel', 21, 1.70)

print(pessoa1.mostra_nome())
print(pessoa1.__dict__)
pessoa1.modifica_altura(1.73)
print(pessoa1.__dict__)


