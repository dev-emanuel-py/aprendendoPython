"""
Any e All



all() - > Retorna true se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os elementos são verdadeiros ?  # False
print(all([1, 2, 3, 4]))  # Todos os elementos são verdadeiros ?  # True
print(all([]))  # Todos os elementos são verdadeiros ?  # True
print(all((1, 2, 3, 4)))  # Todos os elementos são verdadeiros ?  # True
print(all({1, 2, 3, 4}))  # Todos os elementos são verdadeiros ?  # True
print(all('Geek'))  # Todos os elementos são verdadeiros ?  # True


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0]=='C' for nome in nomes]))

# Iteravel vazio convertido em boolean é false, mas o all entende como true
print(all([letra for letra in 'fg' if letra in 'aeiou']))


print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))






any() -> Retorna true se qualquer elemento do iterável for verdadeiro. Se o iteravel estiver vazio , retorna False


print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, [], {}, ()]))  # False

print(any([0, False, [], {}, (), 1]))  # true


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

"""

