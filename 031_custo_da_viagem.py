d = float(input('Qual a distancia da viagem? '))
p = d * 0.55
m = d * 0.50
g = d * 0.45
if d in range(0,201):
    if d in range(0,101):
        print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d,p))
    else:
        print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d,m))
else:
    print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d, g))

D = float(input('Qual a distancia da viagem? '))
p = d * 0.55
m = d * 0.50
g = d * 0.45
if d <= 200:
    if d <= 100:
        print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d, p))
    else:
        print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d, m))
else:
    print('''Você está prestes a fazer uma viagem de {}KM.
E o preço da sua passagem será de R${:.2f}!'''.format(d, g))