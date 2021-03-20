from datetime import date
anonasc = int(input('Em que ano você nasceu?'))
idade = date.today().year - anonasc
print ('Sua idade é {} anos.'.format(idade))
if idade < 18:
    print('Você ainda não está em fase de alistamento. Falta {} anos para você se alistar.'.format (18 - idade))
elif idade == 18:
    print('Chegou a hora de se alistar no exercito do Brasil.')
elif idade > 18:
    print ('Você já passou da fase de alistamento. Você deveria ter se apresentando há {} anos. Você agora é um reservista!'.format(idade - 18))