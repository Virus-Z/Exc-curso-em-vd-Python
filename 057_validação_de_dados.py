s = input('Digite seu sexo [F/M]: ').strip().upper()[0]
while s not in 'MF':
    print('Sexo invalido, tente novamente.')
    s = input('Digite seu sexo [F/M]: ').strip().upper()[0]
print('validação feita com sucesso!')