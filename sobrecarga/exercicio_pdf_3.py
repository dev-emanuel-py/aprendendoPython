class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        print('Construtor Padrão !')

    def exibe(self):
        print(self.__codigo)
        print(self.__nome)
        print(self.__idade)

    def exibe(self, parametro):
        if parametro == 1:
            print(self.__codigo)
            print(self.__nome)
            print(self.__idade)
        else:
            print(self.__codigo)
            print(self.__nome)


class TestaPessoa:

    emanuel = Pessoa('073.725.244-82', 'Emanuel Flavio Dos Santos Silva', 22)
    emanuel.exibe()

