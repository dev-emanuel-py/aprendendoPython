"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores Unários:
    - Not
Operadores Binários:
    - And, Or, Is

Regras de Funcionamento:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com outro.

# Se não estiver ativo
if not ativo:
    print('Ative sua conta, cheque seu e-mail')
else:
    print('bem vindo usuario !')

print(not True)
print(not False)
"""

ativo = False
logado = False

if ativo:
    print('Bem vindo Usuário !')
else:
    print('Ative sua conta! ')
# Ativo é Falso ?
print(ativo is False)
