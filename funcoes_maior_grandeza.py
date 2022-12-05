"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?

Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variaveis do tipo de funções

OBS: Na seção de funçoes, nós utilizamos isso.

Em python, as funções são cidadões de primeiras classes, First Class Citizen



# Exemplo-definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


def calc(num1, num2, funcao):
    return funcao(num1, num2)


print(calc(4, 3, somar))

print(calc(4, 3, diminuir))

print(calc(4, 3, multi))

print(calc(4, 3, div))




# Nested Functions - Funções Alinhadas


# Em python, podemos ter funções dentro de funções, que são conhecidas por Nested Functions
# ou tambem Inner Functions(Funções internas).

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa


# Testando
print(cumprimento('emanuel'))
print(cumprimento('Felicity'))




# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('ahahahahahhaha', 'kkkkkkkkkkk', 'ksksksksksksksks'))
    return rir


rindo = faz_me_rir()
print(rindo())

"""

# Inner Functions(Funções Internas / Nestad Functions) Podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'ksksksksksksk', 'kkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())


