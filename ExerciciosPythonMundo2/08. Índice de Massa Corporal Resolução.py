peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC é de: {:.2f}. '.format(imc), end='')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print ('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA.')

