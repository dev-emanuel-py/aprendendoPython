"""
Por que tesr=tar nosso codigo ?

Testes Automatizados !

         Aplicação web
------------------------------------
|                                  |
|      frontend e backend          |
------------------------------------
|       testes automatizados       |
------------------------------------

Por que testar nosso codigo ?
    - Redizir bugs(Problemas) no código existe;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (Problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs (Problemas);

TDD - Test Driven Development (Desenvolvimento Guiado Por Testes)

Com TDD é utilizado estagios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o codigo mínimo suficiente para fazer o teste passar (Ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testar novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estagios de desenvolvimento do TDD são quese como um mantra
que os desenvolvedores seguem, conhecidos como:

    - Red - vamos escrever um teste que vai falhar;
    - Green - Escrever um codigo minimo pra o teste passar;
    - Refactor - Ajusta o codigo para que ele cumpra a funcionalidade prevista;

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')


felix = Gato('felix')

felix.miar()
print(felix.nome)


