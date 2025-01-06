print('\033[1;31m-='*8,end='')
print('\033[1;36m LOJAS VIRU_Z ',end='')
print('\033[1;31m-='*8)
p = float(input('\033[mValor total da compra: '))
print('''\033[1;35mFormas de pagamentos
\033[m[1] á vista no dinheiro/Pix
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
f = int(input('Qual a forma de pagamento: '))
if f == 1:
    print('''\033[1;35mÓTIMO!\n\033[mPagando a vísta em compras acima de R$650,00 você ganha um desconto de 5%!
Já em compras acima de R$1000,00 você ganha um desconto de 8%''')
    if p <= 1000 and p >= 650:
        print('Seu desconto é de 5% com isso sua compra de R${:.2f}, vai para R${:.2f}'.format(p,p-(p*5/100)))
    elif p > 1001:
        print('Seu desconto é de 8% com isso sua compra de R${:.2f}, vai para R${:.2f}'.format(p,p-(p*8/100)))
    else:
        print('Infelizmente você não atingiu o minímo para obter algum desconto!\nDeseja comprar mais para ganhar um desconto?')
        r = int(input('\033[1;32m[1] SIM\n\033[1;31m[2] NÃO\n\033[mR:'))
        if r == 1:
            print('Legal!\nBoas compras!')
        else:
            print('OK, dirijá-se ao caixa.')
elif f == 2:
    print('\033[1;33mBACANA!!\n\033[mPor gentileza dirija-se ao caixa!')
elif f == 3:
    print('''Em compras parceladas em 2x cobramos um acrecimo de 2% em cima do valor
assim sua compra de R${:.2f}, saira por R${:.2f}'''.format(p,p+(p*2/100)))
elif f == 4:
    r = int(input('Quantas vezes gostaria de parcelar?\nR:'))
    if r < 6:
        print('Sua compra de R${:.2f}, parcelada em {}X tera um adicional de 4% fazendo\nAssim as parcelas sairam por R${:.2f}'.format(p,r,(p+(p*4/100))/r))
    else:
        print('Sua compra de R${:.2f}, parcelada em {}X tera um adicional de 7% fazendo\nAssim as parcelas sairam por R${:.2f}'.format(p,r,(p+(p*7/100))/r))