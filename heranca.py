"""
Herança - POO (Inheritance)

A ideia de herança é a de reaproveitar codigo. Tambem extender nossas classes.

Obs: com a herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cleinte
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Perguntar: Existe alguma entidade genérica o suficinete para encapsular os atributos
e metodos comuns a outras entidades ?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.678.90', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.765.432.10', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


Obs: Quando uma classe herda de outra classe ela herda todos os atributos e metodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:

    [Pessoa]
    - Super classe
    - Classe mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de uma classe, ela é chamada:

    [Cliente, Funcionario]
    - Sub Classe
    - Classe Filha
    - Classe Especifica




class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa #

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    #Funcionario herda de Pessoa#

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.678.90', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.765.432.10', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)



# Sobrescrita de métodos (Overriding)

Sobrescrita de métodos, ocorre quando reescrevemos/ reiplementamos um método presente na super classe
em classes filhas

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Fincionario:{self.__matricula} Nome:{self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.678.90', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.765.432.10', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


