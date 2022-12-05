"""
Erros mais comuns em python

Atenção ! É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
do nosso codigo

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que o python
não reconhece como parte da linguagem.

# Exemplos SyntaxError

a)
def funcao:
    print('Geek')

b)
None = 1
def = 1

c)
return


2 - NameError -> Ocorre quando uma variavel ou função não foi definida

# Exemplos NameError

a)
print(geek)

b)
geek()

c)

a = 18
if a < 10:
    msg = 'é maior que 10'

print(msg)
 # NameError: name 'msg' is not defined


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplos de TypeError

a)
print(len(5))
# TypeError: object of type 'int' has no len()

b)
print('geek'+[])
# TypeError: can only concatenate str (not "list") to str




4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice invalido

exemplos IndexError

a)
lista = ['Geek']
print(lista[2])
# IndexError: list index out of range

b)
lista = ['Geek']
print(lista[0][10])
# IndexError: list index out of range



5 - ValueError -> Ocorre quando uma função ou operação built-in(integrada) recebe um argumento com tipo correto
mas valor inapropriado

Exemplos ValueError

a)
print(int('Geek'))
# ValueError: invalid literal for int() with base 10: 'Geek'


6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplos KeyError

a)
dic = {}
print(dic['Geek'])
# KeyError: 'Geek'

b)
dic = {'python': 'University'}
print(dic['Geek'])
# KeyError: 'Geek'



7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 12, 13, 2, 39)
print(tupla.sort())
# AttributeError: 'tuple' object has no attribute 'sort'


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
def nova():
print('Geek')
# IndentationError: expected an indented block

b)
for i in range(10):
i + 1

print(i)

# IndentationError: expected an indented block


OBS: Exceptions e Erros são sinonimos na programação.

OBS: Importante ler e prestar a tenção na saída de erro.

"""




