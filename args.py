"""
Entendendo o *args

- O *args é um parametro, como qualquer outro. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo

*xis

Mas por conversão, utilizamos *args para defini-lo


Mas o que é o *args ?

O parametro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutaveis.



# Exemplo

def soma_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_numeros(2, 4, 7))
print(soma_numeros(4, 3))  # TypeError
print(soma_numeros(2, 3, 4, 5))  # TypeError



def soma_numeros(*args):
    print(args)


soma_numeros()
soma_numeros(1)
soma_numeros(1, 2)
soma_numeros(1, 2, 3)
soma_numeros(1, 2, 3, 4)

# Saída
# ()
# (1,)
# (1, 2)
# (1, 2, 3)
# (1, 2, 3, 4)



# Entendendo o args

def soma_numeros(nome, *args):
    return sum(args)


print(soma_numeros('Emanuel'))
print(soma_numeros('Emanuel', 1))
print(soma_numeros('Emanuel', 1, 2))
print(soma_numeros('Emanuel', 1, 2, 3))
print(soma_numeros(1, 2, 3, 4))



# Outro exemplo do *args

def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza, quem é voce ?'


print(verifica_info())
print(verifica_info(1, True, 'university', 'geek'))
print(verifica_info('university', 1, 3.14))


"""


def soma_todos_numeros(*args):
    print(args)
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(1, 2, 3, 4))

numeros_lista = [1, 2, 3, 4, 5, 6, 7]
numeros_tupla = (1, 2, 3, 4, 5, 6, 7)
numeros_set = {1, 2, 3, 4, 5, 6, 7}

# desempacotador

print(soma_todos_numeros(*numeros_lista))
print(soma_todos_numeros(*numeros_tupla))
print(soma_todos_numeros(*numeros_set))

# Obs: O asterisco serve para que informemos ao python que estamos passando como
# argumento uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar
# esses dados

