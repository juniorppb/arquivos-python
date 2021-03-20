dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = dias * 45.00 + km * 0.14
print('O valor total do aluguel é de: R$ {}.'.format(pago))
