"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional

print('Geek University')
print()

# EXEMPLO DE FUNÇÃO ONDE A PASSAGEM DE PARÂMETRO SEJA OBRIGATÓRIA


def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  # TypeError -  Parametro é obrigatorio




def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuário

# Obs:
# Se o usuario passar somente um parâmetro este será atribuido ao parametro numero, e será calculado o quadrado
# desse numero.
# Se o usuario passar 2 argumento, o primeiro será atribuido ao parametro numero e o segundo ao parametro
# potencia. Então será calculada esta potencia.
print(exponencial())  # Isso vai ser executado por que definimos o valor nos parametros


# OBS: Em funções python os parametros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO !

def teste(potencia, num=2):
    return num ** potencia


print(teste(6))



# outros exemplos


def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError




# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'bem vindo instrutor {nome} !'
    elif nome == 'Geek':
        return 'Eu pensei que você era um instrutor'
    return f'Olá {nome} !'


print(mostra_informacao('Emanuel'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Emanuel', True))
print(mostra_informacao(nome='Julia'))



# Por que utilizar parametros com valor default ?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de codigo;



# quais tipos de dados podemos utilizar como valores para parametros?

- Qualquer tipo de dado:
    - Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funções e etc;


# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))





# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek'  # Variavel global


def diz_oi():
    instrutor = 'Python'  # Variavel local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS:  Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia.




def diz_oi():
    prof = 'Geek'  # Variavel Local
    return f'Ola {prof}'


print(diz_oi())
print(prof)  # NameError




# Atenção com variaveis globais (SE PUDER EVITE !)

total = 0

def incrementa():
    total = total + 1  # UnboundLocalError (A variavel local esta sendo usada para processamento, sem ser inicializada)
    return total

print(incrementa())





# Atenção com variaveis globais (SE PUDER EVITE !)

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variavel global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

"""


# Podemos ter funções que são declaradas dentro de funções, e tambem tem uma forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

print(dentro())  # NameError



