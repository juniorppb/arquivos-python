from datetime import date
nome = str(input('Digite seu nome: '))
anonasc = int(input('{}, por favor. Digite seu ano de nascimento: '.format(nome)))
idade = date.today().year - anonasc
print ('{}, com sua idade de {} anos.'.format(nome,idade))
if idade < 9:
    print('Sua categoria é MIRIM.')
elif idade >= 9 and idade < 14:
    print('Sua categoria é INFANTIL.')
elif idade >= 14 and idade< 19:
    print('Sua categoria é JÚNIOR.')
elif idade >= 19 and idade < 20:
    print ('Sua categoria é SÊNIOR.')
elif idade >= 20:
    print ('Sua categoria é MASTER.')

