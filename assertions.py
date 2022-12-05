"""
Assertions (Afirmações/Checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada.

#OBS: A palavra 'assert' pode ser utilizada em qualquer função ou codigo nosso...não precisa
ser exclusivamente nos testes.


# ALERTA: Cuidado ao utilizar 'assert'


Se um programa python for executado com o parametro -O, nenhum assertion
sera validado. Ou seja, todas as suas validações já eram.

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os numeros precisam ser positivos'
    return a + b


# print(soma_numeros_positivos(2, 4))  # 6
# print(soma_numeros_positivos(2, 4))  # AssertionError


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'


def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins!'
    destroi_todo_o_sistema()
    return 'Adeus'
