from area import Retangulo

import math 
while True:
    piso_a = ﬂoat(input('Digite um lado do piso: '))
    piso_b = ﬂoat(input('Digite o outro lado do piso: '))

    piso = Retangulo(piso_a, piso_b)
    az_a = ﬂoat(input('Digite o lado do azulejo: '))
    az_b = ﬂoat(input('Digite o outro lado do azulejo: '))

    azulejo = Retangulo(az_a, az_b)
    area_piso = piso.area()
    area_az = azulejo.area()

    qntd_az = area_piso/area_az
    if area_piso % area_az == 0:
        print(f'A quantidade exata de azulejos para preencher o piso é de {qntd_az}')
    else:
        print(f'A quantidade mínima de azulejos para preencher o piso é de {math.ceil(qntd_az)}')
    
    print()
    print()
    print('Adicionei mais testes aqui :')
    print(azulejo.retorna_lado())
