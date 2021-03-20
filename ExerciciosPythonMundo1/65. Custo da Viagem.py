v = float(input('Qual a distância que você viajou? '))
valor1 = v * 0.50
valor2 = v * 0.45
if v <= 200:
    print('Você percorreu {} KM. E o valor da sua passagem é de R$ {}.'.format(v, valor1))
else:
    print('Você percorreu {} KM. E o valor da sua passagem é de R$ {}.'.format(v, valor2))
