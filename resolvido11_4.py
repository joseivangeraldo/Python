'''Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que este arquivo
tem um numero inteiro em cada linha. Todos os numeros lidos devem ser mostrados na tela.
Mostrar tambem a soma dos valores, a quantidade, a media aritimetica, o menor valor e o maior valor,
usar um laço while e na leitura usar o metodo.readline()'''
Lst = []
arqEntr = open('entrada_er11_04.txt', 'r')   # abre o arquivo para leitura
linha = arqEntr.readline()                  # lê a primeira linha
while linha != '':
    Lst.append(int(linha))                  # converte linha para inteiro e coloca na lista
    linha = arqEntr.readline()              # lê a próxima linha
arqEntr.close()                             # fecha o arquivo
print('Valores lidos do arquivo')
print(Lst)
Soma = sum(Lst)    # calcula a soma dos elementos da lista
print(f'Soma dos valores = {Soma}')
Qtde = len(Lst)    # determina a quantidade dos elementos da lista
print(f'Quantidade = {Qtde}')
print(f'Média dos valores = {Soma/Qtde}')
Minimo = min(Lst)  # determina o menor elemento da lista
print(f'Mínimo dos valores = {Minimo}')
Maximo = max(Lst)  # determina o maior elemento da lista
print(f'Máximo dos valores = {Maximo}')
print('Fim do Programa')


