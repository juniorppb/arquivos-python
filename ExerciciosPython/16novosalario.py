print('Quanto receberei de salário, com aumento que recebi?')
sal = float(input('Meu salário atual é: '))
sal2 = float(input('Recebi um aumento de %: '))
n1 = sal2 / 100
n2 = n1 * sal
n3 = sal + n2
print('Eu recebi {:.2f} de aumento, portanto, meu novo salário será de: {:.2f}.'.format(n2, n3))
