"""
Documentando funções com docstring

Obs: podemos ter acesso a documentação de uma função em python
utilizando a propriedade especial __doc__

podemos ainda fazer acesso a documentação com a função help()

"""

# Exemplos

def diz_oi():
    """
    Uma função simples que retorna a string 'Oi!'
    """
    return 'Oi !'


print(diz_oi())

print(help(diz_oi))

print(diz_oi.__doc__)


def exponecial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou o 'numero' a potencia informada.
    :param numero: Número que desejamos gerar o exponecial
    :param potencia: Potência que queremos gerar o exponecial. Por padrão é 2.
    :return: Retorna o exponecial de um 'numero' por 'potencia'.
    """
    return numero ** potencia


print(exponecial(10, 3))

print(help(exponecial))

print(exponecial.__doc__)
