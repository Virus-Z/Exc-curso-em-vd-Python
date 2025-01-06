n = input('Digite seu nome completo: ').strip().split()
print('''Muito prazer em te conhecer!
Seu primeiro nome é: {}
Seu último nome é: {}'''.format((n[0]), n[len(n) - 1]))