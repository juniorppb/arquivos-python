print('Vou pintar as paredes da minha casa, mas não sei quanto usar de tinta. Então vamos calcular.')
alt = float(input('Qual é a altura da parede? '))
lar = float(input('Qual é a largura da parede? '))
mao = float(input('Quantas demãos serão dada? '))
m2 = alt * lar
ma1 = m2 * mao
t2 = ma1 / 2
print('Sua parede tem um total de {:.2f} m², sendo assim você terá {:.2f} m² dando {:.1f} demãos, você precisará de {:.2f} litros de tinta.'.format(m2, ma1, mao, t2))
