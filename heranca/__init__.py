class Equipamento:

    def __init__(self, tipo, marca):
        self.__tipo = tipo
        self.__marca = marca

    @property
    def tipo(self):
        return self.__tipo

    @property
    def marca(self):
        return self.__marca

    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo

    @marca.setter
    def marca(self, nova_marca):
        self.__marca

    def exibe_informacao(self):
        print(self.__tipo)
        print(self.__marca)
        print('')


class Computador(Equipamento):

    def __init__(self, tipo, marca, cor, voltagem):
        super().__init__(tipo, marca)
        self.__cor = cor
        self.__voltagem = voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def voltagem(self):
        return self.__voltagem

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor

    @voltagem.setter
    def voltagem(self, nova_voltagem):
        self.__voltagem = nova_voltagem

    def exibe_informacao(self):
        print(self.tipo)
        print(self.marca)
        print(self.__cor)
        print(self.__voltagem)


class TestaEquipamento:

    if __name__ == '__main__':
        equip = Equipamento('Eletrodomestico', 'Eletrolux')
        pc = Computador('Informática', 'Asus', 'Preto', '220')

        equip.exibe_informacao()
        pc.exibe_informacao()


