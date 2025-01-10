from random import randint

def sortear_numeros():
    lista = []
    for i in range(5):
        lista.append(randint(1, 100))
    return lista

def somar_pares(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    return soma

lista = sortear_numeros()
print(f'Ola bem vindo ao sorteio de numeros')
print(f'Os numeros sorteados foram: {lista}')
print('Os número em ordem crecente são:', sorted(lista))
print(f'A soma dos numeros pares é: {somar_pares(lista)}')
