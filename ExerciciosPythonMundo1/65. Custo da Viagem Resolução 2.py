distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} KM.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem é de R$ {}.'.format(preço))
