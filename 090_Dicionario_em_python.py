# aluno = {}
# n = input('Digite o nome do aluno: ')
# m = float(input('Digite a média do aulono: '))
# situação = ''
# if m < 7 and m > 5:
#     situação = 'Recuperação'
# elif m < 5:
#     situação = 'Reprovado'
# else:
#     situação = 'Aprovado'
# aluno['nome'] = n
# aluno['media'] = m
# aluno['status'] = situação
# for k, v in aluno.items():
#     print(f'{k}: {v}')

geral = {}
geral['nome'] = input('Digite o nome do aluno: ')
geral['media'] = float(input('Digite a media do aluno: '))
if geral['media'] >= 7:
    geral['status'] = 'Aprovado'
elif geral['media'] < 7 and geral['media'] >= 5:
    geral[ 'status'] = 'Recuperação'
else:
    geral['status'] = 'Reprovado'
print('-'*30)
for k, v in geral.items():
    print(f'{k}: {v}')
print('-'*30)
