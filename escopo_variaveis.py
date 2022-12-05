"""
Escopo de Variáveis

Dois casos de escopo:

1- Variáveis Globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2- Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarado.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declaramos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuímos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42
"""

numero = 42 # Exemplo de Variável Global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existe = 'oi'
print(nao_existe)

numero = 2
# novo = 0
if numero > 10:
    novo = numero + 10 # Exemplo de Variável Local declarada dentro do bloco do if
    print(novo)

print(novo)
