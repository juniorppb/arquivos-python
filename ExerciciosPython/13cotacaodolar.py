dol = float(input('Vamos converter real para dólar, e saber quanto podemos comprar. Quanto de dinheiro (em real) você tem? R$ '))
n1 = dol / 5.28
print('Você tem US$ {:.2f}.'.format(n1))

real = float(input('E quanto terei em reais, se trocar todos os meus dólares? US$  '))
n2 = real * 5.28
print('Você tem R$ {:.2f}.'.format(n2))