"""
Listas Alinhadas (Nested List)

- Algumas linguagens de programação possuem uma estrutura de dados chamada de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em python nós temos as Listas

numeros = [1, 2, 3, 4, 5]


print(listas)
print(type(listas))

#  Como fazemos para acessar os dados ?

print(listas[0][1])  # 2
print(listas[2][1])  # 8


# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3



# Iterando com loops em uma lista alinhada

for lista in listas:
    for numero in lista:
        print(numero)



# List comprehension

[[print(valor) for valor in lista] for lista in listas]
"""


# Outros exemplos

# Gerando um tabuleiro/matriz 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
