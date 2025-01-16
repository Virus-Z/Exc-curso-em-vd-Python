from datetime import date

def voto(ano):
    idade = date.today().year - int(ano)
    if idade < 16:
        return print(f'Com {date.today().year - int(ano)} anos o voto é: \033[1;34mNEGADO\033[m')
    elif 16 <= idade < 18 or idade > 70:
        return print(f'Com {date.today().year - int(ano)} anos o voto é: \033[1;34mOPCIONAL\033[m')
    else:
        return print(f'Com {date.today().year - int(ano)} anos o voto é: \033[1;34mOBRIGATÓRIO\033[m')

voto(input('Referente a poder votar vamos ver qual seu status!\nEm que ano você nasceu? '))
