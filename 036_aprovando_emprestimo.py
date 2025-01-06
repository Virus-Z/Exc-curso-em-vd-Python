c = float(input('Valor da casa: '))
s = float(input('Salario do comprador: '))
a = int(input('Quantos anos pretende financiar: '))
p = c/(a*12)
t = s*30/100
if p <= t:
    print('Para comprar uma casa de R${:.2f} em {} anos, você pagará uma parcela de R${:.2f}'.format(c,a,p))
    print('Como sua margem é R${:.2f} seu emprestimo foi aprovado!!'.format(t))
else:
    print('Para comprar uma casa de R${:.2f} em {} anos, você pagará uma parcela de R${:.2f}'.format(c,a,p))
    print('Como sua margem é de R${:.2f} seu emprestimo foi infelizmente negado!!'.format(t))