"""
MRO - Method Resolution Order

Method Resolotion Order (Resolução de ordem de metodos), é a ordem de
execução dos metodos(quem será executado primeiro).

Em python,a gente pode conferir a ordem de execução dos metodos (MRO) de 3 formas:
    -Via propriedade de classe __mro__
    -Via método mro()
    -via help

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terreste(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} esta andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Terreste, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Pinguim(Aquatico, Terreste)
Eu sou Tux do mar

Pinguim(Terrestre, Aquatico)
Eu sou Tux da terra
"""

