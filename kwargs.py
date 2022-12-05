"""
**kwargs

Poderiamos chamar este parametro de **xix, mas por convençã́o chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionario.



# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parâmetros *args e **kwargs não são obrigatorios.

cores_favoritas()

cores_favoritas(geek='navy')




# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um comprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek !"
    return 'Não tenho certeza de quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))





# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatorios;
- *args;
- Parâmetros default (Não obrigatórios)
- **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)



# Entenda por que é importante manter a ordem dos parâmetros na declaração
# Função com a ordem correta de parametros
# def mostra_info(a, b, *args, instrutor='geek', **kwargs):
#    return[a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parametros
def mostra_info(a, b, instrutor='geek', *args, **kwargs):
    return[a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'geek'
kwargs = {'sobrenome' : 'university', 'cargo':'Instrutor'}



print(mostra_info(1, 2, 3, sobrenome='university', cargo='Instrutor'))





# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


soma_multiplos_numeros(1, 2, 3)

lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

tupla = (1, 2, 3)
soma_multiplos_numeros(*tupla)

set = [1, 2, 3]
soma_multiplos_numeros(*set)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# Obs: os nomes da chave em um dicionario devem ser o mesmo dos parâmetros da função

# dicionario = dict(f=1, g=2, h=3)  # TypeError

# soma_multiplos_numeros(**dicionario)  # TypeError

soma_multiplos_numeros(**dicionario, lang='Python')

