peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC é de: {:.2f}. '.format(imc), end='')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print ('Você está no PESO IDEAL.')
elif imc < 30:
    print('Você está com SOBREPESO.')
elif imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')

