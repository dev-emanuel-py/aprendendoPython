"""
Reduce

Obs: A partir do python 3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a partir do modulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso.
99% das vezes um loop for é mais legivel.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E voce tem uma função que recebe dois parametros:

def funcao(x,y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o interavel.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado.
    passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda
    o resultado.

    isso é repetido até o final.
    passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. no final,
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)


"""

# Como funciona na pratica ?

# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parametros

res = reduce(lambda x, y: x * y, dados)

print(res)

# Utilizando loop normal

res = 1
for n in dados:
    res = res * n

print(res)






