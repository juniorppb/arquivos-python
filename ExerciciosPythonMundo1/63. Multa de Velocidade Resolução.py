radar = float(input('Qual a velocidade atual do carro? '))
if radar > 80:
    print('Você excedeu a velocidade permitida.')
    multa = (radar - 80) * 7.00
    print('Você deve pagar uma multa no valor de R$ {:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
