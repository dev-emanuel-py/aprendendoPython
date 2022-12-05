"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... Por que elas se chamam gererators

nomes = ['Carlos', 'Camila', 'Carla', Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))
print('')

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))



# Qual a utilidade de getsizeof() ? -> Retorna a quantidade de bytes em memoria do elemento passado como parametro

from sys import getsizeof

# Mostra quantos bytes a string 'geek' esta ocupando. Quanto maior a string mais espaco ocupa

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92736763763))

print(getsizeof(True))




from sys import getsizeof

# Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com dictionary comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria : ')
print(f'List comprehension: {list_comp} bytes')
print(f'Set comprehension: {set_comp} bytes')
print(f'Dictionary comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)




