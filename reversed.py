"""
Reversed

OBS: Não confunda com a função reserve() que estudamos em listas.
reserve() ela inverte a lista.
e so funciona em listas.

Já a função reversed() funciona com qualquer interavel.

Sua função é inverter o iteravel.

A função reversed() retorna um iteravel chamado List Reverse Interator

"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla, ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Set
print(set(reversed(lista)))  # OBS: O set não define ordem dos elementos.

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Ja vimos como fazer isso mais facil com o slice de strings
print('Geek University'[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que tambem ja vimos como fazer isso utilizando o proprio range()

for n in range(10, 0, -1):
    print(n)



