"""
Loop for

Loop -> Estruturas de repetição
For -> Uma dessas estruturas

C ou Java:

for(int i = 0; i < 10; i++){
//execução do loop
}

Python :
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de iteraveis:
    -String
        nome = 'Geek University'
    -Lista
        lista = [1, 3, 5, 7, 9]
    -Range
        numeros = range(1, 10)

# Exemplo de for 1 (iterando sobre uma String)
for letra in nome:
    print(letra)

print('')

# Exemplo de for 2 (iterando sobre uma Lista)
for numero in lista:
    print(numero)

print('')

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


Enumerate:
((0,'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

for indice, letra in enumerate(nome):
    print(letra)
    print(indice )

for _, letra in enumerate(nome):
    print(letra)

Obs: quando não precisamos de um valor podemos descarta-lo usando um underline'_'

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar ? '))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end = '')
"""
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D'* num)

0<i<x
0<j<y
0<k<z