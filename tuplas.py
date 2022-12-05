"""

Tuplas ( tuple )

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças basicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# CUIDADE 1: As tuplas são representadas por parenteses (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla !
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela virgula não pelo uso do parenteses

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# Podemos criar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em python: Essencial')
escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro(ValueErro) se colocarmos um numero diferente de elementos para desempacotar;

# Metodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis

# Soma*, valor maximo*, valor minimo* e tamanho
#  * se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla1 = tupla1 + tupla2 # Tuplas são imutaveis, mas podemos sobre escrever seus valores
print(tupla1)

# verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)
print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))
escola =  tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


# O acesso a elementos de uma tupla é tambem semelhante a de uma lista

print(meses[5])
print('')

# Iterar com While
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# verificamos em qual indice um elemento está na tupla

print(meses.index('julho', 6))

# Obs: Caso o elemento não exista, será gerado ValueError.


# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

# Por que utilizar tuplas ?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# - * Isso porque trabalhar com elementos imutaveis tras segurança para o código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = tupla + outra

print(nova)
print(tupla)

"""



