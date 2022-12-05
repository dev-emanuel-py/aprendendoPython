"""
Preservando metadatas com Wraps

Metadados - > São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.




# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois numeros
    return a + b


# print(soma(56, 42))

print(soma.__name__)  # Soma
print(soma.__doc__)  # Soma dois numeros.

"""

from functools import wraps

# Resolução do Problema


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


# print(soma(56, 42))

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma dois numeros.

print(help(soma))

