# AINDA FALTA TERMINAR


class Elevador:

    def __init__(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__andar_atual = 0
        self.__total_pessoas = 0

    def entrar(self, quantidade_pessoas):
        self.__total_pessoas += quantidade_pessoas
        if self.__total_pessoas < self.__capacidade:
            pass
        else:
            self.__total_pessoas -= quantidade_pessoas
            print('O elevador esta cheio')

    def sair(self, quantidade_pessoas):
        if self.__total_pessoas >= 0:
            print('O elevador esta vazio')
        else:
            self.__total_pessoas -= quantidade_pessoas

    def sobe(self):
        if self.__andar_atual < self.__capacidade:
            self.__andar_atual += 1
        else:
            print('elevador no ultimo andar')

    def desce(self):
        if self.__andar_atual == 0:
            print('Elevador no terreo')
        else:
            self.__andar_atual -= 1


elevador1 = Elevador(5, 5)
print(elevador1.__dict__)
elevador1.sobe()
print(elevador1.__dict__)
elevador1.entrar(2)
print(elevador1.__dict__)
elevador1.entrar(4)
print(elevador1.__dict__)
elevador1.sobe()
print(elevador1.__dict__)
elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
print(elevador1.__dict__)
elevador1.sobe()
print(elevador1.__dict__)
elevador1.desce()
elevador1.desce()
elevador1.desce()
elevador1.desce()
elevador1.desce()
elevador1.desce()
print(elevador1.__dict__)
elevador1.sair(3)
print(elevador1.__dict__)
