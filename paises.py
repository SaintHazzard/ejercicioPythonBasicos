paises=['Colombia','Panama','USA','China','Espania','Sudafrica']
continentes=['Sur america','Centro america','Norte America','Asia','Europa','Africa']

dictPaises={}

for i in range(0,len(paises)):
  dictPaises[paises[i].lower()]=continentes[i]


pais=input('Ingrese nombre de pais ')
print(dictPaises[pais.casefold()])