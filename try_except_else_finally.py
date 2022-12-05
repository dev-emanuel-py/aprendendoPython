"""
try, except, else, finally

Dica de quando e onde tratar codigo:

TODA ENTRADA DEVE SER TRATADA !

Obs: A função do usuario é destruir seu sistema.



# Else -> é executado somente se não ocorrer o erro.
try:
    num = int(input('informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'voce digitou {num}')



# Finally

try:
    num = int(input('Imforme um numero:'))
except ValueError:
    print('Voce nao digitou um valor valido. ')
else:
    print(f'voce digitou o numero {num}')
print('Voce esta executando o finally')


# O bloco finally é sempre executado. Independente se houve exceção ou não.
# O finally, geralmente é utilizado para fechar ou desalocar recursos.




# Exemplo mais complexo Errado

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor Incorreto')




# Exemplo mais complexo Correto - Generico
# OBS: Voce é responsavel pelas entradas das suas funções. Então trate-as !


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu Um problema'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

"""


# Exemplo mais complexo Correto - Semi-Generico
# OBS: Voce é responsavel pelas entradas das suas funções. Então trate-as !


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu Um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

