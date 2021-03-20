from time import sleep
import emoji
print('Contagem regressiva .... ')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVO! :tada:'))
