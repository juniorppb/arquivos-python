radar = float(input('Qual foi a velocidade que você passou pelo radar? '))
multa = (radar - 80) * 7.00
if radar > 80:
    print('Você excedeu a velocidade permitida.')
    print('Sua multa será de R$ {:.2f}.'.format(multa))
else:
    print('Você estava dentro da velocidade permitida.')
