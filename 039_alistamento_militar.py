from datetime import date
s = int(input('''[1] \033[1;36mMasculino
\033[m[2] \033[1;35mFeminino
\033[mQual seu sexo: '''))
if s == 1:
    a = int(input('Qual o ano de seu nascimento: '))
    ali = a + 18
    at = date.today().year
    if a <= at - 111:
        print('\033[1;31mOuve algum erro pois já era para você estar morto!')
    elif ali > at:
        print('Quem nasceu em {}, tem {} anos em {}.'.format(a,at - a,at))
        print('Ainda faltam {} anos para o alistamento.'.format(ali - at))
        print('Seu alistamento será em {}'.format(ali))
    elif ali < at:
        print('Quem nasceu em {}, tem {} anos em {}'.format(a,at - a,at))
        print('Seu alistamneto foi a {} anos atrás em {}'.format(at - ali,ali))
        print('voce ja deve ou deveria ter se alistado!!!')
    elif ali == at:
        print('Quem nasceu em {}, tem {} anos em {}.'.format(a,at - a,at))
        print('Seu alistamento será esse ano!!!')
else:
    r = int(input('''Para mulheres o alistamento não é obrigatorio, você gostaria de se alistar mesmo assim:
[1] \033[1;36mSim
\033[m[2] \033[1;31mNão
\033[mR: '''))
    if r == 1:
        a = int(input('\033[mQual o ano de seu nascimento: '))
        ali = a + 18
        at = date.today().year
        if a <= at - 111:
            print('\033[1;31mOuve algum erro pois já era para você estar morto!')
        elif ali > at:
            print('Quem nasceu em {}, tem {} anos em {}.'.format(a, at - a, at))
            print('Ainda faltam {} anos para o alistamento.'.format(ali - at))
            print('Seu alistamento será em {}'.format(ali))
        elif ali < at:
            print('Quem nasceu em {}, tem {} anos em {}'.format(a, at - a, at))
            print('Seu alistamneto foi a {} anos atrás em {}'.format(at - ali, ali))
            print('voce ja deve ou deveria ter se alistado!!!')
        elif ali == at:
            print('Quem nasceu em {}, tem {} anos em {}.'.format(a, at - a, at))
            print('Seu alistamento será esse ano!!!')
    else:
        print('Okay, sem problemas tenha um ótimo dia!!!')
