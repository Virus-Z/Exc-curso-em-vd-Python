from time import sleep

def contador(i, f, p):
    for c in range(i, f, p):
        print(f'{c}',end=' ', flush=True)
        sleep(0.35)

def user():
    while True:
        try:
            i = int(input(f'Inicio: '))
            f = int(input(f'Fim: ')) + 1
            p = int(input(f'Passo: '))
            if p == 0:
                p = 1
            if i == 0:
                i = 1
            if f == 0:
                f = 1
            if i > f:
                p *= -1
                f -= 2
            contador(i, f, p)
            break
        except:
            print(f'Ops, aparentemente você não digitou um  número valido vamos tentar novamente!')
            continue

def continuar():
    while True:
        user()
        quest = input(f'\nGostaria de escolher mais uma vez?[S/N]: ').upper().strip()[0]
        while quest not in 'SN':
            quest = input(f'Desculpe, Mas gostaria de escolher mais uma vez?[S/N]: ').upper().strip()[0]
        if quest == 'N':
            break


print(f'Contagem de 1 até 10 de 1 em 1:')
contador(1, 11, 1)
print(f'\nContagem de 10 até 0 de 2 em 2:')
contador(10, -1, -2)
print(f'\nAgora digite o inicio, fim e o passo: ')
continuar()
print(f'{'=-'*5}{'Fim'}{'=-'*5}')
