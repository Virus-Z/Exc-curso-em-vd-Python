s = float(input('Qual é o salário do funcionário? R$'))
a = (s*15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% do aumento, passará a receber R${:.2f}'.format(s,(a+s)))