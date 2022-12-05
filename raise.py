"""
Levantando os proprios erros com raise

raise -> Lança exceçôes

OBS: O raise não é uma função. é uma palavra reservada, assim como o def ou qualquer outra em python.

Para simplifincar, pense no raise como sendo útil para que possamos criar nossas proprias exceçoes e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

raise ValueError('Valor Incorreto')


# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('True', 7)



# Exemplo real refatorado


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Geek', 'preto')


Obs: o raise, assim como o return, finaliza a função. Ou seja, nada apos o raise é executado
"""

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print('depois do raise')
    print(f'O texto {texto} sera impresso na cor {cor}')


colore('Geek', 'preto')




