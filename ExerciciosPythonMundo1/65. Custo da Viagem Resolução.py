from time import sleep
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} KM.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Estamos calculando sua passagem. Só um momento.')
sleep(3)
print('E o preço da sua passagem será de R$ {}.'.format(preço))

