def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'so se vive uma vez'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Putz, dormi muito! Estou atrasado para o trabalho!'

    else:
        return f'continuo cansado após dormir por {num_horas} horas'


def eh_engracada(pessoa):
    comediantes = ['jim carrey', 'bozo']
    if pessoa in comediantes:
        return True
    return False

