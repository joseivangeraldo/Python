from random import randint
def CarregaLista():
    L = []
    for i in range(10):
        L.append(randint(1, 1000))
    return L

print('Inicio do Programa.')

print('Primeira lista gerada')
valores = CarregaLista()
print(f'Lista gerada >> {valores}')

print('Segunda lista gerada')
valores2 = CarregaLista()
print(f'Lista gerada >> {valores2}')

print('Fim do Programa')
