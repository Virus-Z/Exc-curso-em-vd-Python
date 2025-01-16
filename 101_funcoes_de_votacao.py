from datetime import date

def voto(ano):
    idade = date.today().year - int(ano)
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'

ano = input('Referente a poder votar vamos ver qual seu status!\nEm que ano você nasceu? ')
print(f'Com {date.today().year - int(ano)} anos: {voto(ano)}')