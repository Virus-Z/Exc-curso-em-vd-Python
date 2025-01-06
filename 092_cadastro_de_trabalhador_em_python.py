from datetime import date
geral = {}
geral['nome'] = input(f'nome: ')
ano = int(input(f'Digite o ano de nascimento: '))
geral['idade'] = date.today().year - ano
geral['ctps'] = int(input(f'Digite o número de sua CTPS(caso não possua digite 0): '))
if geral['ctps'] == 0:
    geral['ctps'] = 'Não possui carteira de trabalho'
else:    
    geral['contratação'] = int(input('Digite o ano da contratação: '))
    aposentadoria = (geral['contratação'] + 35) - ano
    geral['aposentadoria'] = aposentadoria
    geral['salario'] = float(input('Digite o valor do salario: '))
for k, v in geral.items():
    print(f'{k}: {v}')
