while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('_'*30)
    for c in range(1,11):
        print(f'{tab} x {c} = {tab*c}')
    print('_'*30)
print('PROGRAMA TABUADA ENCERRADO! Volte sempre...')
