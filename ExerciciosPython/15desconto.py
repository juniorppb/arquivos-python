print('Qual é o valor do desconto se eu comprar esse produto?')
vp = float(input('Qual é o valor do produto? R$  '))
vd = float(input('Qual é o valor de desconto em % ?'))
desc = vd / 100
desc1 = vp * desc
print('O valor do desconto será de: {:.2f} reais.'.format(desc1))
