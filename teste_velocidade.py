"""
Teste de velocidade com expressoes geradoras

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num


g1 = nums()

print(g1)

print(next(g1))
print(next(g1))
print(next(g1))


g2 = (num for num in range(1, 10))

print(g2)
print(next(g2))
print(next(g2))


"""

# Realizando o teste de velocidade
import time

# Generations Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 Milhoes
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 Milhoes
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


