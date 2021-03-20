from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu?'))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} anos.'.format(ano))
else:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} anos.'.format(ano))