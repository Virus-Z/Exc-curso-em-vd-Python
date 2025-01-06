d = int(input('Quantos dias alugado: '))
k = float(input('Quantos Km: '))
p = ((d*60)+(k*0.15))
print('O total a pagar é de: R${:.2f}'.format(p))