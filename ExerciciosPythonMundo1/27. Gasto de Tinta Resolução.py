print('Vou pintar as paredes da minha casa, mas não sei quanto usar de tinta. Então vamos calcular.')
alt = float(input('Qual é a altura da parede? '))
lar = float(input('Qual é a largura da parede? '))
m2 = alt * lar
print('Sua parede tem a dimensão de {} x {}, totalizando {} m².'.format(alt, lar, m2))
demao = float(input('Quantas demãos? '))
ma1 = m2 * demao
print('Ao total você tem {}m² para pintar. Considerando que a cada litro de tinta você pode pintar 2m²'.format(ma1))
l = ma1 / 2
print('Você precisará de {:.2f}l de tinta.'.format(l))
