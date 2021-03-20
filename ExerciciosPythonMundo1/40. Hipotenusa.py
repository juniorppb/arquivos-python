num1 = float(input('Qual é o comprimento do cateto oposto?'))
num2 = float(input('QUal é o comprimento do cateto adjascente?'))
hip = (num1 ** 2 + num2 ** 2) ** (1/2)
print('Valor da Hipotenusa é: {:.2f}.'.format(hip))