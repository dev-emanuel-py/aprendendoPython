"""
Trabalhando com modulos built-in (Modulos integrados, que ja vem instalados no python)
________________________
|Python|Modulos builtin|
------------------------




# Utilizando alias (apelidos) para modulos ou funções

import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um modulo utilizando o ( * )

from random import *
# import random (são diferentes)

print(random())



# Importando todo o modulo

import random

print(random.random())




# Utilizando alias (apelidos) para modulos ou funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())
"""

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (
    random,
    randint,
    choice,
    shuffle
)

print(random())

print(randint(2, 7))

lista = ['geek', 'university', 'python']
shuffle(lista)
print(lista)

print(choice('university'))
