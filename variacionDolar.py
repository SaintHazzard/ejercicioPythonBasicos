arrayDaysPrice=[]

def dataPriceDay():
  n=int(input(f'Ingrese la cantidad de dias de muestra: '))
  for i in range(n):
    price=int(input(f'Precio de la monena en el dia {i}: '))
    arrayDaysPrice.append(price)
  return arrayDaysPrice  


arrayDaysPrice=dataPriceDay()

def maxVariation(array):
  maxVar=0
  for i in range(0,len(arrayDaysPrice)-1):
    diffVar=arrayDaysPrice[i+1]-arrayDaysPrice[i]
    if diffVar > maxVar:
      maxVar=diffVar
      
  print(f'La maxima variacion fue de {maxVar}')   




maxVariation(arrayDaysPrice)