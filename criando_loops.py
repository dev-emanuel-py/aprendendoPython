"""

Criando sua propria versão de loop

for numero in [1, 2, 3, 4, 5]:
    print(numero)

for letra in 'geek university':
    print(letra)


"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)




