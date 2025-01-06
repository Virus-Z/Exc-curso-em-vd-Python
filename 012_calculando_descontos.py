p = float(input('Qual o valor do produto? R$'))
d = (p*5/100)
print('O produto que custava R${:.2f}, na promoção com o desconto de 15% ira custar R${:.2f}.'.format(p,(p-d)))