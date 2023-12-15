arrayDaysPrice=[]

def dataPriceDay():
  try:
    n=int(input(f'Ingrese la cantidad de dias de muestra:'))
    if n > 0 and n < 11:
      for i in range(n):
        price=int(input(f'Precio de la monena en el dia {i}: '))
        arrayDaysPrice.append(price)
      return arrayDaysPrice
    else:
      raise ValueError()
  except ValueError:
    print(f'Entrada invalida, no trollee')
    return dataPriceDay()

def maxVariation(array):
  maxVar=0
  for i in range(0,len(arrayDaysPrice)-1):
    diffVar=arrayDaysPrice[i+1]-arrayDaysPrice[i]
    if diffVar > maxVar:
      maxVar=diffVar;dia1,dia2=i,i+1
  print(f'La maxima variacion fue de {maxVar} del dia {dia1} al dia {dia2}')   


maxVariation(dataPriceDay())