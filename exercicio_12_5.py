from random import randint
def CarregaLista(qtde):
''' Carrega uma lista com qtde de elementos aleatorios entre 1 e 1000'''
    L = []
    for i in range(qtde):
        L.append(randint(1, 1000))
    return L

q = int(input('Digite a quantidade desejada: '))
valores =CarregaLista(q)
print(f'Lista gerada >> {valores} ')
print(f'A lista gerada tem {q} elementos')
print('Fim do Programa')
