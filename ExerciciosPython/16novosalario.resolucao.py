sal = float(input('Meu salário atual é: '))
aum = float(input('Recebi um aumento de (em %): '))
n1 = sal + (sal * aum / 100)
n2 = sal * aum / 100
print('Com {:.1f}%. Eu recebi um aumento de {:.2f}, portanto, meu novo salário será de: {:.2f}.'.format(aum, n2, n1))
