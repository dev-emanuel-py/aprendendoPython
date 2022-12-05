"""
Map

Com map, fazemos mapeamento de valores para função.



import math

def area(r):

   # Calcula a area de um circulo

   # :param r: recebe o raio
   # :return: retorna a area de um circulo

    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# forma comum

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# forma com o Map

# Map é uma função que recebe dois parametros: o primeiro a função, o segundo um interável. retorna um Map Object

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS:  apos utilizar a função map() depois da primeira utilização do resultado, ele zera.



# Para fizar - Map

# Temos dados iteraveis:

# Dados a1, a2,..., an

# Temos uma função:

# Função f(x)

# Utilizamos uma função map (f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O map object: f(a1), f(a2), f(...), f(an)
"""

# MAIS UM EXEMPLO

cidades = [('berlin', 29), ('cairo', 36), ('buenos aires', 19), ('los angeles', 26), ('tokio', 27), ('nova york', 28),
('londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda


print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
