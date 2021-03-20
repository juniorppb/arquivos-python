print('=*='*25)
print('Analisador de Triângulos')
print('=*='*25)
seg1 = float(input('Primeiro Segmento:'))
seg2 = float(input('Segundo Segmento:'))
seg3 = float(input('Terceiro Segmento:'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')

