def escreva(txt):
    print('\033[1;31m-' * (len(txt) + 2))
    print(f'{'\033[m '}{txt}')
    print('\033[1;31m-' * (len(txt) + 2))


print(f'{'-'*15}{'\033[1;33mPalavras'} {'\033[m-'*15}')
while True:
    user = input('\033[mDigite uma palavra, frase ou texto: ')
    escreva(user)
    exit = input('\033[mQuer continuar[S/N]: ').upper().strip()[0]
    while exit not in 'SN':
        exit = input('Quer continuar[S/N]: ').upper().strip()[0]
    if exit == 'N':
        break
