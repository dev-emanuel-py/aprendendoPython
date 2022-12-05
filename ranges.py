"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive(início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive(início especificado pelo usuário, e passo de 1 em 1)

#Exemplo Forma 2
for num in range(4, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(inicio epsecificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 3
for num in range(0, 51, 5):
    print(num)

# forma 4(Inversa)

range(valor_final, valor_de_parada, passo)

OBS: valor_de_parada não inclusive(valor_final epsecificado pelo usuario, e passo especificado pelo usuario)

# Exemplo forma 4
for num in range(10, -11, -1):
    print(num)

"""


