s = float(input('Qual é o salário do funcionário? '))
s1 = (s * 15) / 100
s2 = (s * 10) / 100
if s <= 1250:
    print('Quem ganhava R${:.2f}, passa a ganahar R${:.2f} agora.'.format(s, (s + s1)))
else:
    print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f} agora.'.format(s, (s + s2)))

s = float(input('Qual é o salario do funcionario? '))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print('Quem ganhava R${:.2F}, passa a ganhar R${:.2f} agora'.format(s,n))