"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nos desenvolvedores)



import json

ret = json.dumps(['produto', {'playstation 4': ('2Tb', 'novo', '220v', 2340)}])

print(type(ret))
print(ret)


import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('felix', 'vira-lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)



Integrando o JSON com o Pickle

pip install jsonpickle

"""


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('felix', 'vira-lata')




