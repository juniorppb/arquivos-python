print('Estamos verificando a folha de pagamento de todos os funcionários da empresa, e precisamos saber qual é o seu salário.')
print('='*120)
n = float(input('Qual é o seu salário? '))
if n <= 1250.00:
    print('Seu novo salário será de R$ {:.2f}.'.format(n+(n*0.15)))
else:
    print('Seu novo salário será de R$ {:.2f}.'.format(n+(n*0.10)))

#s = n + (n * 0.10)
#print('Seu novo salário será de R$ {:.2f}.'.format(s))
