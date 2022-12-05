"""
Geradores

- Geradores (generators) são Iterators (Iteradores);

OBS: O CONTRARIO NÃO É VERDADEIRO. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generators Functions (Funções Geradoras)

----------------------------------------------------------------------------------
/ Funções                                / Generators Functions                  /
/ Utilizam return                        / utilizam yield                        /
/ retorna uma vez                        / podem utilizar yield multiplas vezes  /
/quando executada, retorna uma valor     / quando executada, retorna um generator/
----------------------------------------------------------------------------------


gen = conta_ate(5)
print(conta_ate(10))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""


# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
# Uma Generator Function não é um Generator. Ela gera um Generator. ok?


gen = conta_ate(10)

for num in gen:
    print(num)

gen =  conta_ate(5)
print(list(gen))




