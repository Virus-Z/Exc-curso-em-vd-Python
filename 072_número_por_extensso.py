n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Douze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte' )

while True:
    r = int(input('Digite um número de 1 a 20: '))
    while r  not in range(0, 21):
        r = int(input('Vamos tentar de novo. Digite um número de 1 a 20: '))
    print(f'Você digitou o Numero: {n[r]}')
    y = input('Você gostaria de continuar? [S/N] ').upper().strip()[0]
    if y != 'SN':
        while y not in 'SN':
            y = input('Opss vamos tentar novamente, você gostaria de continuar? [S/N] ').strip().upper()[0]
    if y == 'N':
        break
print('Fim')
