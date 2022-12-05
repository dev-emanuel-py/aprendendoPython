"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.9939329
data_final = dd/mm/yyyy 13:34:23.0878747

delta = data_final - data_inicial


import datetime

#temos da data de hoje
data_hoje = datetime.datetime.now()

# Data de um evento futuro
aniversario = datetime.datetime(2023, 2, 14, 0)

# calcula o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(tempo_para_evento.days)
print(f'faltam {tempo_para_evento.days} para o evento')
"""
import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
