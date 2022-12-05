"""
dictionary comprehension

Pense no seguinte:

se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

se quisermos criar um set:

conjunto = {1, 2, 3, 4}

se quisermos criar um dicionario:

dicionario = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

# Sintaxe

dictionary comprehension
{chave: valor para for valor in iteravel}

list comprehension
[valor for valor in iteravel]


numeros = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)




# Exemplos

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""

# Exemplo com logica condicional

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)



