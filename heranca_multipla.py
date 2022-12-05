"""
POO - Heranças múltiplas

Herança múltipla nada mais é do que a possibilidade da uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

Obs: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta
    - Por Multiderivação Indireta




# Exemplo 1 - Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass




# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


# Obs: não importa se a derivação é direta ou indireta. A classe que realizar a herança herdara
todos os atributos e metodos das super classes.

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


class Pinguim(Aquatico, Terreste):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terreste('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Eu sou tux da terra /  Eu su tux do mar
# MRO - Method Resolution Order

# Objeto é instância de...

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terreste)}')
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instancia de object? {isinstance(tux, object)}')
