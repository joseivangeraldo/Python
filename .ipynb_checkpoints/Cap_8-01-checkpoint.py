n = -1
while n != 0:
    n = int(input('Digite um inteiro'))
    match n:
        case 1:
            print( 'Você digitou Um' )
        case 2:
            print( 'Você digitou Dois' )
        case 3:
            print( 'Você digitou Tres' )
        case _:
            print( 'Você digitou outra coisa' )
print('\n\nFim do Programa')



            