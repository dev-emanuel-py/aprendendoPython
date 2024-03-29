"""
Funções com Retorno

numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret}')

ret_pr = print(numeros)

print(f'Retrono do print: {ret_pr}')


Obs: em python quando uma função não retorna nenhum valor, o retorno é None


# Exemplo função

def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()

print(f'Retorno de ret: {ret}')

# Saida
# 49
# Retorno de ret: None

Obs: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

Obs: não precisamos necessariamente criar uma variavel para receber o retorno de
uma função. Podemos passar a execução da função para outras funções.



# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

# Criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno de ret: {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')
# Saida
# 49
# 50



# Refatorando a função

def diz_oi():
    return 'oi '


print(diz_oi())

alguem = 'Pedro'

print(diz_oi() + alguem + '!')

# Função sem retorno
def diz_oii():
    print('Oi')


diz_oii()


Obs: Sobre a palavra reservada return

1 - Ela finaliza a função ou seja ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;]
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 1 - Ela finaliza a função ou seja ela sai da execução da função;


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'oi'
    print('estou sendo executado apos o retono')


print(diz_oi())



# Exemplo 2 - Podemos ter, em uma função, diferentes returns;


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())



# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;


def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()


# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))



# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1

    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


"""

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())






