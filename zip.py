"""
Zip

zip() -> Cria um iteravel (zip object) que agrega elemento de cada um dos dois iteraveis passados como entrada em pares.


lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 12]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, ou dicionario

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# Obs: O zip() utiliza como parametro o menos tamanho em iteravel. Isso significa que se estiver
# Trabalhando com iteraveis de tamanhos diferentes, irá para quando os elementos do menor
# Iteravel acabar

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteraveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Podemos utilizar tambem uma lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))

"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map para fazer isso

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
