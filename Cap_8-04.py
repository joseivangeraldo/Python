Codigo = [103, 117, 121, 135, 161, 189, 288, 284, 216]
Lista = []
print('Alternativa com if clássico')
for codigo in Codigo:
    if 120 <= codigo and codigo <= 200:
        Lista.append(codigo)
print(f'  códigos filtrados --> {Lista}')

Lista = []
print('\n\nAlternativa com if nica linha')
for codigo in Codigo:
    Lista.append(codigo) if 120 <= codigo and codigo <=200 else 0
print(f'  códigos filtrados --> {Lista}')