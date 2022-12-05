"""
Funções com Parâmetro

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> Processamento - > saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;





# Refatorando uma função


def quadrado(numero):
    return numero ** 4


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(9)
print(ret)

# print(quadrado())  # TypeError





# Refatorando a função


def cantar_parabens(aniversariante):
    print('parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva o/a {aniversariante} !')


cantar_parabens('Emanuel')
cantar_parabens()  #TypeError





# Funções podem ter n parametros de entradas. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessarios. Eles são separados por virgula.

# Exemplo

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))


# Obs: Se a gente informar um numero errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
# print(soma(4))  # TypeError - Passando argumentos a menos








# Nomeando Parâmetros

def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# Diferença entre parametros e argumentos
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa !

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos noemados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# Utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))


"""


# Erro comum na utilização dom return

# Certo
def soma_impares_certo(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares_certo(lista))


# Errado
def soma_impares_errado(numeros):  # O erro esta na indentação
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares_errado(lista))


