from funcionalidades import *

tv = Televisor('SONY', 'SONY-123')

controle = ControleRemoto(tv)
controle.sintonizaCanal('SBT')
controle.sintonizaCanal('ESPN')
controle.trocaCanal('Globo')
controle.trocaCanal('ESPN')

controle.aumentaVolume()

print(tv.volume)
print(tv.canal_atual)