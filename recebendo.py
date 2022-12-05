"""
Recebendo dados dos usuarios

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas Simples Triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie
- Aspas Simples Triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """ Angelina Jolie """

# Entrada de dados

#print("Qual seu nome ?")
#nome = input()

nome = input('Qual seu nome ? ')

# Exemplo de print antigo da versão 2.x
#print('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno da versão 3.x
#print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade ?")
# idade = input()

idade = int(input('Qual sua idade ?'))

# Saida de dados
# Exemplo de print antigo da versão 2.x
# print('O (A) %s tem %s anos' %(nome, idade))

# Exemplo de print moderno da versão 3.x
#print('O(A) {0} tem {1} anos '.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O(A) {nome} tem {idade} anos')

print(f'O(A) {nome} nasceu em {2021 - int(idade)}') # Cast => int(idade)