'''Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que este arquivo
tem um numero inteiro em cada linha. Todos os numeros lidos devem ser mostrados na tela.
Mostrar tambem a soma dos valores, a quantidade, a media aritimetica, o menor valor e o maior valor,
usar um laço while e na leitura usar o metodo.readline()'''

Lst = []

arqEntr = open('entrada_er11_04.txt', 'r')
linha = arqEntr.readline()

while linha != '':
    Lst.append(linha)
    linha = arqEntr.readline()
arqEntr.close()

print(Lst)

print('\nFim do Programa.')

