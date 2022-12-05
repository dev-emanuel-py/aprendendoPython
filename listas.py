"""
Listas ( List )

Listas em Python funcionam como em vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    -Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
 - Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
 - Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []

Listas são mutaveis: ou seja elas podem mudar constantemente.

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista.
num = int(input('Qual numero voce deseja achar: '))
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'não encontrei o numero {num}')

caractere = input('Qual letra voce procura: ')
if caractere in lista5:
    print(f'Encontrei a letra {caractere}')
else:
    print(f'Não encontrei a letra {caractere}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# A adicionar elementos em lista

# Para adicionar elementos ou valores em lista, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)
lista1.sort()
print(lista1)

# lista1.append(12, 34, 56) # Erro
#OBS: com append, nós so conseguimos adicionar 1 elemento por vez

lista1.append([8, 3, 1]) # Coloca como elemento único (sublista)
print(lista1)

if [8, 3,  1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([126, 46, 67])  # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)


# podemos facimento juntar duas listas
lista6 = lista1 + lista2  # criamos uma nova lista que é composta pela lista 1 e 2
lista1.extend(lista2)   # adicionamos os elementos da lista 2 na lista 1
print(lista6)
print(lista1)

# Podemos facimente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2

# Tambem podemos com o slice de string inverter uma lista
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista2)
print(lista6)

# Tamanho de uma lista (podemos contar quantos elementos existem dentro da lista)

print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
# O pop não somente remove o ultimo elemento mas tambem o retorna

print(lista5)
elemento = lista5.pop()
print(lista5)
print(elemento)

# Podemos remover um elemento pelo indice
# Os elementos a direta desde indice serão deslocados para a esquerda.
# Se não houver o elemento no indice informado, teremos o erro IndexError.
elemento = lista5.pop(2)
print(lista5)
print(elemento)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# exemplo 1

curso = 'Programação em Pythn essecial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por Padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python,Essecial'
print(curso)
curso = curso.split(',')
print(curso)

lista6 = ['Programacao', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: pega a lista6, coloca cifrão entre cada elemento e tranforma em uma string
curso = '$'.join(lista6)
print(curso)

# podemos colocar qualquer tipo de dado dentro de uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1,2,3], 456778535]
print(lista6)
print(type(lista6))

# iterando sobre listas

# Exemplo 1 - Utilizando o for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista dou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#          1          2        3         4
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um circulo, onde
# o final de um elemento está ligado ao inicio da lista.

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # erro, pois noa existe indice -5


for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# listas aceitam valore repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros metodos não tão importantes, mas tambem uteis
# Encontrar um indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista está o valor 6 ?
print(numeros.index(6))

# Em qual indice da lista está o valor 9 ?
print(numeros.index(9))

# print(numeros.index(19) # Gera ValueErro
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueErro
# OBS: Retorna o Índice do primeiro elemento encontrado
print(numeros.index(5))

# podemos fazer buscar dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do indice 1
print(numeros.index(5, 2))  # buscando a partir do indice 2
print(numeros.index(5, 3))  # buscando a partir do indice 3

# print(numeros.index(5, 4))  # buscando a partir do indice 4 # ValueError
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueErro

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o indice do valor 8, entre os indices 3 e 6

# revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de listas com o paramentro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1::]) #Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2])  # começa em 0, pega até o indice 2 - 1
print(lista[:4])  # começa em 0, pega até o indice 4 - 1
print(lista[1:3])  # começa do indice 3, pega até o indice 3 - 1

# Trabalhando com slice de lista com o parametro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final de 2 em 2

print(lista[::2])


# invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # Maximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desenpacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferentes de elementos na lista ou variaveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow copy e Deep Copy)

# forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # cópia
print(nova)
nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da listas para uma nova lista, mas elas
# Ficaram totalmente independentes, ou seja, modificamos uma lista, não afeta a outra. isso em python
# é chamado de Deep Copy (Cópia Profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)
nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
# Apos realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# isso em python é chamado de shallow copy

"""



lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista1.sort()
print(lista1)
