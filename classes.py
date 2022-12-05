"""
POO - Classes

Em POO,classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente

Imagine que voce queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja ,pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, Possivelmente
    iríamos querer saber se a lâmpada é de 110 ou 220 volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto
    pode realizar no seu sistema. No caso da lampada, por exemplo, um comportamento comum que muito
    provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em python para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em python quando temos um bloco de codigo que ainda não está
implementado.

OBS: Quando nomeamos nossas classes em python utilizamos por convenção o nome com inicial em
maiusculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiusculo, todas juntas, essa forma é chamada de CarmelCase.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretorios e etc.

Obs: quando estamos planejando um software e definimos qual classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade.


"""

idade = 32
preco = 2340.45
nome = 'Felicity Jones'

print(type(idade))
print(type(preco))
print(type(nome))


# Mas não temos um tipo para lampada, porem podemos criar uma classe representado esse objeto
# E isso vira um tipo de dado


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


valor = int('42')  # Cast

print(help(int))


