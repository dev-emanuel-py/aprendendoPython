"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro generico

try:
    geek()
except:
    print('Deu algum erro')

# Tente executar a função geek(), caso encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma generica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
tratar de forma especifica.


# Exemplo 3 - tratando um erro especifico

try:
    geek()
except NameError:
    print('voce esta utilizando uma função inexistente')



# Exemplo 4 - tratando um erro especifico

try:
    len(5)
except TypeError:
    print('voce esta utilizando uma função inexistente')



# Exemplo 5 - tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Podemos efetuar diversos taratamentos de erros de uma vez.

try:
    geek()
    #print('geek'[5])
    #len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('deu um erro diferente')


"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "geek"}

print(pega_valor(dic, 8))



