class Televisao:

    def __init__(self, canal, volume):
        self.__canal = canal
        self.__volume = volume

    def qual_canal(self):
        return self.__canal

    def qual_volume(self):
        return self.__volume

    def escolha_canal(self, novo_canal):
        self.__canal = novo_canal

    def muda_canal(self, botao_canal):
        if botao_canal:
            self.__canal += 1
        else:
            self.__canal -= 1

    def muda_volume(self, botao_volume):
        if botao_volume:
            self.__volume += 1
        else:
            self.__volume -= 1


class ControleRemoto:

    def __init__(self):
        self.__botao_canal = False
        self.__botao_volume = False

    @staticmethod
    def ir_para_canal(tv, canal):
        tv.escolha_canal(canal)

    def aumentar_canal(self, tv):
        self.__botao_canal = True
        tv.muda_canal(self.__botao_canal)

    def diminuir_canal(self, tv):
        self.__botao_volume = False
        tv.muda_volume(self.__botao_canal)

    def aumentar_volume(self, tv):
        self.__botao_volume = True
        tv.muda_volume(self.__botao_volume)

    def diminuir_volume(self, tv):
        self.__botao_volume = False
        tv.muda_volume(self.__botao_volume)


tv1 = Televisao(1, 1)
controle = ControleRemoto()

controle.aumentar_volume(tv1)

print(tv1.qual_volume())

controle.ir_para_canal(tv1, 23)

print(tv1.qual_canal())










