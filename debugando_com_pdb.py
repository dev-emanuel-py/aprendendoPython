"""
Degugando com PDB

PDB -> Python Debugger

Vida de inseto -> Life's Bug

Bug -> Inseto


# Obs: a utilização do print para debugar codigo é uma pratica ruim.

def dividir(a, b):
    print(f'a = {a}, b = {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu Um problema: {err}'


print(dividir(4, 7))





# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando
# O PDB - Python Debugger

# Exemplo com o pycharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu Um problema: {err}'


print(dividir(4, 0))




# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)






# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no inicio do arquivo
# Nos colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.




# Exemplo com PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# * A partir do python 3.7, não pe mais necessario importar a biblioteca pdb, pois o comando de debug foi
# Imcorporado como função built-in(integrada) chamada breakpoint()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no inicio do arquivo
# Nos colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.


"""


# OBS: Cuidado com conflitos entre nomes de variaveis e os comando do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes das variaveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variaveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos em variavel sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4

print(soma(2, 4, 6, 8))

