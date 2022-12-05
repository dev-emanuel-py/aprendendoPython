"""
set comprehension

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""

# Exemplo

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: faça uma alteração na estrutura acima para gerar um dicionario ao inves de set

numeros = {x:x ** 2 for x in range(10)}
print(numeros)

# Para finalizar

letras = {letra for letra in 'Geek University'}
print(letras)
