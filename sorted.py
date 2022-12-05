"""
Sorted

OBS: Não confunnda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar.


# OBS: O sorted, sempre retorna uma lista com os elementos do iteravel ordenados

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = {6, 1, 8, 2}

# Adicionando parametros ao sorted()
print(set(sorted(numeros)))
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor



# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))



"""

# Ultimo exemplo

musicas = [
    {"Titulo": "Thunderstruck", "Tocou": 3},
    {"Titulo": "Dead Skin Mask", "Tocou": 2},
    {"Titulo": "Back in Black", "Tocou": 4},
    {"Titulo": "Too old to rock'in roll, too young to die", "Tocou": 32}

]
# Ordenando da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['Tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))


