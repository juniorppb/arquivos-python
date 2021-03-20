carro = float(input('Por quantos dias você pretende alugar o carro? '))
km = float(input('Em média, irá percorrer quantos KM? '))
aluguel = carro * 45.00
aluguel2 = km * 0.14
tar = aluguel + aluguel2
print('Para o período alugado, o valor do carro fica em R${:.2f} e a kilometragem em R${:.2f}.\nTotalizando em R$ {:.2f}.'.format(aluguel, aluguel2, tar))
