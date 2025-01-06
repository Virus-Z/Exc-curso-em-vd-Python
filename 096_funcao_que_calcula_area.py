def area(l, c):
    a = (l * c)
    print(f'Com a largura de {l} e o comprimento de {c}, teremos uma área de: {a}m²')
    print('-' * 40)


print('-' * 40)
print(f'{'Calculadora de Área':^40}')
print('-' * 40)
while True:
    l = float(input('Digite a largura do terreno: '))
    c = float(input('Agora digite o comprimento do terreno: '))
    area(l, c)
    user = input('Gostaria de calcular mais um terreno?[S/N]: ').upper().strip()[0]
    while user not in 'SN':
        user = input('Gostaria de calcular mais um terreno?[S/N]: ').upper().strip()[0]
    if user == 'N':
        break
print(f'{'-' * 13}{' Volte  Sempre '}{'-' * 13}')
