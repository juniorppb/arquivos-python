from time import sleep
sal = float(input('Qual o valor do seu salário? R$ '))
emp = float(input('Qual o valor do emprestimo? R$ '))
quant = float(input('Em quantos anos prefere fazer o emprestimo?'))
porc = sal*0.30
parc1 = quant * 12
parc2 = emp / parc1
sleep(3)
if parc2 >= porc:
    print ('Infelizmente seu limite é muito baixo, não podemos liberar o emprestimo para você.')
elif parc2 <= porc:
    print('Seu limite foi aprovado, estamos processando...')
    print('R$ {:.2f} esse é o valor da sua parcela.'.format(parc2))
    print('Você financiou o valor de R$ {:.2f}, e parcelou em {:.0f} meses.'.format(emp, parc1))
