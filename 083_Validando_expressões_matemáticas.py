user = input('Digite uma expressão matematica com parenteses; ex. (5+(1-5)): ')
x = user.count("(")
z = user.count(")")
if z == x:
    print(f'Sua expressão está correta.')
else:
    print(f'Sua expressão está incorreta.')
