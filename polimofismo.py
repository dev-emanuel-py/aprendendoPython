"""
POO - Polimofismo

Poli -> Muitas
Mofis -> Formas

Quando a gente reimplementa um metodo presente na classe pai em classes filhas
estamos realizando uma sobresescritas de metodos (Overriding).

O overrinding é a melhor representação do polimofismo.

"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo...')


dog = Cachorro('rex')
cat = Gato('Felix')
mouse = Rato('Stuart')

dog.falar()
dog.comer()

cat.falar()
cat.comer()

mouse.comer()
mouse.falar()

