"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho(ou seja, o numero de itens) de um iteravel.


# So pra revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5}))
print(len(range(0, 10)))

# Por debaixo dos panos quando utilizamos a função len() o python faz o seguinte:
# Dunder len
print('Geek University'.__len__())





# Abs

abs() -> Retorna um valor absoluto de um numero inteiro ou real. De forma basica, seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))




# Sum

sum() -> Recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos
incluindo o valor inicial.

# Obs: O valor inicial default = 0


# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.14, 5.789]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))



# Round

round() -> Retorna um numero arredondado para n digito de precisão após a casa decimal. se a precisão não for
informada retorna o inteiro mais proximo da entrada.

"""

# Exemplos Round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.2199999, 2))
print(round(1.2121212121))








