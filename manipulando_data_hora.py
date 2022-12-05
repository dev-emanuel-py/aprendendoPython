"""
Manipulando data e hora

Python tem um módulo built-in(integrado) para se trabalhar com data e hora
chamado datetime



# print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2022-04-20 11:06:02.229236  BR 20/04/2022

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 6 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)






# recebendo dados do usuario e convertendo para data


print(evento)

print(type(evento))

print(type('16/03/2024'))


aniversario = input('Informe sua data de nascimento(dd/mm/yyyy): ')

print(aniversario)

aniversario = aniversario.split('/')

aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

print(aniversario)

print(type(aniversario))

"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos da data e hora

print(evento.year)  # ano
print(evento.month)  # mes
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # Microsegundos


