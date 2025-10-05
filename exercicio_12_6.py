from random import randint
''' Carrega uma lista com qtde de elementos aleatorios entre ae
 e b'''
def CarregaLista(qtde, a, b):
    L = []
    for i in range(qtde):
        L.append(randint(a, b))
    return L

q = int(input('Digite a quantidade desejada: '))
Lmin = int(input('Digite o Limite minimo: '))
Lmax = int(input('Digite o Limite maximo: '))

valores =CarregaLista(q, Lmin, Lmax)
print(f'Lista gerada >> {valores} ')
print(f'A lista gerada tem {q} elementos')
print('Fim do Programa')
