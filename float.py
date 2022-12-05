"""

Tipo Float, Real, Decimal

Casas Decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.

"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# é possivel fazer dupla atribuição
valor2, valor1 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# PODEMOS CONVERTER UM FLOAT PARA UM INT
"""
OBS: ao converter valores float para inteiros, perdemos precisão

"""
res = int(valor)
print(res)
print(type(res))

# podemos trabalhar com numeros complexos
variavel = 5j
print(type(variavel))
