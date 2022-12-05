"""
# def cumprimentos(nome: str) -> str:
#    return f'Olá, {nome}'
#
#
# print(cumprimentos('emanuel'))


def cabecacho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecacho('geek university'))

print(cabecacho('geek university', False))

print(cabecacho('geek university', alinhamento='geek'))


# correto

texto: str

# Incorreto

texto:str
texto : str

# correto

) -> str
)->str
) ->str

# correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True






import math


def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circuferencia.__annotations__)

nome: str = 'geek university'
peso: float = 67.9
ativo: bool

ativo = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)

"""


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)

print(p.__dict__)

# print(p.__annotations__) não tem annotations

print(p.andar.__annotations__)
print(p.__init__.__annotations__)
