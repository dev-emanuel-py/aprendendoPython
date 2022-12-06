"""
Tipo String

Em python, um dado é considerado do tipo String sempre que:

-Estiver entre uma Aspas Simples -> 'Uma String', '234', 'a', 'True', '42.3'
-Estiver entre uma Aspas Duplas -> "Uma String", "234", "a", "True", "42.3"
-Estiver entre uma Aspas Simples Triplas -> '''Uma String''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \" Jolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) #Transforma em uma lista de Strings

print(nome[0:4]) # Slice de String

print(nome[5:15]) # Slice de String

# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])
"""
# -Estiver entre uma Aspas Simples -> """Uma String""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,   11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'
"""
[::-1] -> comece do primeiro elemento, vá ate o ultimo elemento e inverta
"""
print(nome[::-1]) # Inversão da String Pythônico

print(nome.replace('e', 'i'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)
print(texto[::-1])

nome = 'ana' # Palíndromo
print(nome)
print(nome[::-1])
