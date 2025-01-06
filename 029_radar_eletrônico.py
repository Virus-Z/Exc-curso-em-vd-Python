"""print('-=-'*18)
print('Limite MAX permitido 60KM/H.')
v = int(input('Qual a velocidade do automovel: '))
if v in range(0,60):
    v1 = v
    m1 = (v1 - 60) * 10
    if v1 <=60:
        print('''Tudo certo!
Sua velocidade está dentro do limite, pode prosseguir viagem!''')
        print('-=-' * 18)
    else:
        print('''Stop!
Você será multado em R${:.2f}, por estar acima do limite!'''.format(m1))
        print('-=-' * 18)
else:
    v2 = v
    m1 = (v2 - 60) * 10
    m2 = (v2 - 80)*15
    if v2 <=80:
        print('''Stop!
Você será multado em R${:.2f}, por estar acima do limite!'''.format(m1))
        print('-=-' * 18)
    else:
        print('''Stop!
Você será multado em R${:.2f}, por estar acima do limite!'''.format(m2))
        print('-=-' * 18)"""

print('-=-'*18)
print('Limite MAX permitido 60KM/H.')
print('-=-'*18)
v = int(input('Qual a velocidade do automovel: '))
if v in range(61,300):
    m1 = (v - 60) * 10
    m2 = (v - 60) * 15
    if v in range(61,80):
        print('''STOP, você está a {}KM/H, isso é {}Km/h acima do permitido!
Você recebera uma multa de R${:.2f}, por estar acima da velocidade!'''.format(v,(v-60),m1))
    else:
        print('''STOP, você está a {}KM/H, isso é {}Km/h acima do permitido!
Você recebera uma multa de R${:.2f}, por estar acima da velocidade!'''.format(v,(v-60),m2))

else:
    print('''Tudo certo!
Você esta dentro do permitido, boa viagem!''')
