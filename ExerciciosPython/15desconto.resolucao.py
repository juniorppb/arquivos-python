preco = float(input('Qual é o preço do produto? R$ '))
desconto = float(input('Qual é o valor de desconto? '))
desc = preco * desconto / 100
novo = preco - (preco * desconto / 100)
print('O produto no valor de R$ {}, com desconto de {:.2f} (que equivale a {:.0f}%) custará R$ {:.2f}.'.format(preco, desc, desconto, novo))

