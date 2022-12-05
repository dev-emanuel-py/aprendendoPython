"""
Teste de memoria com generators

# Sequencia de fibonacci
1,1,2,3,5,8,13...
"""
from sys import getsizeof


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

def fib_gen(max):
    c, d, cont = 0, 1, 0
    while len(nums2) < max:
        a, b = b, a + b
        yield b
        cont += 1

lista1 = fib_list(10)
print(lista1)
print(getsizeof(lista1))


lista2 = fib_gen(10)
print(lista2)
print(getsizeof(lista2))

# Quando colocamos com 100000 valores na lista gastou 449 MB de memoria
# enquanto quando colocamos 100000 valores no geradores gastou apenas 2,8 MB

