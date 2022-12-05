"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py


def soma(a, b):
    # Soma os numeros a e b

    #>>> soma(2, 3)
    #5

    #>>> soma(4, 6)
    #100

    #
    #return a + b


# saída do doctests

Trying:
    soma(2, 3)
Expecting:
    5
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.





# Outro exemplo aplicando o TDD

def duplicar(valores):
    # duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    return [2 * elemento for elemento in valores]





# Erro inesperado...

Dentro do doctest, o python não reconhece string com aspas duplas. precisa ser aspas simples

def fala_oi():
    #Fala oi

    # fala_oi()
    'oi'
    #
    #return "oi"

"""

# Um ultimo caso estranho


def verdade():
    """Retorna verdade

    >>> verdade()
    True

    """
    return True









