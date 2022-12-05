"""
Módulo Random e o que são modulos?

- Em python, modulos nada mais são do que outros arquivos Python.

- Modulo random -> possui varias funções para geração de numeros pseudo-aleatorio.




# OBS: Existem duas formas de se utilizar um modulo ou função deste

# Forma 1 - Importando todo o módulo (não recomendado).

import random

# random() -> Gera um numero real pseudo-aleatorio entre 0 e 1.

# Ao realizar o import de todo o modulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do modulo ficarão disponiveis (Ficarão em memoria). Caso voce saiba quais funções voce precisa utilizar
# deste módulo, então esta não seria a forma idela de utilização. Nós veremis uma forma melhor na Forma 2.

print(random.random())

# Veja que pra utilizar a função random do pacote random, nos colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso mas a função random é
# apenas uma função dentro do módulo random.



# Forma 2 - Importando uma função especifica do módulo - Forma recomendada

from random import random

# No import acima estamos falando: Do módulo random, import a função random

for i in range(10):
    print(random())





# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluido.




# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.

# gerador de apostas para a mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Comeca em 1 e vai até 60





# choice -> Mostra um valor aleatorio entre um iteravel.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice('Geek University'))
"""

from random import shuffle
# shuffle() -> tem a função de embaralhar dados

cartas = ['k', 'q', 'j', 'a', 2, 3, 4, 5, 6, 7]

print(cartas)
shuffle(cartas)
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())

