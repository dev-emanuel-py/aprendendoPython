"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))  # 129


# Faça um programa que receba dois valores do usuario e mostre o maior

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

print(max(num1, num2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(True, False))

print(max(3.14, 3.15))

print(max('Geek University'))






min() -> Retorna o menor valor em um iteravel ou o menor de dois ou mais elementos


# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))  # 1


# Faça um programa que receba dois valores do usuario e mostre o maior

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

print(min(num1, num2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(True, False))

print(min(3.14, 3.15))

print(min('Geek University'))



# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim

print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander

print(min(nomes, key=lambda nome: len(nome)))  # Tim


"""

musicas = [
    {"Titulo": "Thunderstruck", "Tocou": 3},
    {"Titulo": "Dead Skin Mask", "Tocou": 2},
    {"Titulo": "Back in Black", "Tocou": 4},
    {"Titulo": "Too old to rock'in roll, too young to die", "Tocou": 32}

]


print(max(musicas, key=lambda musica: musica["Tocou"]))
print(min(musicas, key=lambda musica: musica["Tocou"]))

# DESAFIO !  IMPRIMA O TITULO DA MUSICA
print(max(musicas, key=lambda musica: musica["Tocou"])['Titulo'])
print(min(musicas, key=lambda musica: musica["Tocou"])['Titulo'])

# DESAFIO ! COMO ENCONTRAR A MUSICA MAIS TOCADA E MENOS TOCADA SEM USAR
# MAX MIN E LAMBDA

max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['Titulo'])

min = 9999999999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['Titulo'])







