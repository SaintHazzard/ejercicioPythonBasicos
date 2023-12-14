from os import system
vuelto=0
def menu(productos):
    print('¿Qué producto desea? ')
    for i in range(1, 4):
        print(f'\t{i}. {productos[i-1][0]}')
    
    try:
      elecproducto = int(input())
      if elecproducto > 0 and elecproducto <= 3:
        return int(productos[elecproducto-1][1])
    except:
      print('Eleccion no valida')
      menu(productos)

def generar_vuelto(vuelto, monedas):
    vueltos = [0, 0, 0]
    vueltos[2] = vuelto // 100
    vuelto = vuelto % 100
    vueltos[1] = vuelto // 50
    vuelto = vuelto % 50
    vueltos[0] = vuelto // 10
    print('Su vuelto es: ')
    for i in range(2, -1, -1):
        for j in range(vueltos[i]):
            print(monedas[i])
    
def maquina_alimentos():
  
  productos = [['Producto A', '270'], ['Producto B', '340'],    ['Producto C', '390']]; monedas = [10, 50, 100]
  prod_elect = menu(productos)
    
  pago = False
  total_pago = 0
  
  while not pago:
    # system("clear")
    print('Inserte las moneda: ')
    print('1. Moneda de 10$')
    print('2. Moneda de 50$')
    print('3. Moneda de 100$')
    elec_moneda = int(input())
    total_pago += monedas[elec_moneda - 1]
    print('Su pago actual es de: ', total_pago)
    input('Presione Enter para continuar...')
        
    if total_pago >= prod_elect:
      print('Pago completo')
      pago = True
      vuelto = total_pago - prod_elect
      generar_vuelto(vuelto, monedas)

maquina_alimentos()