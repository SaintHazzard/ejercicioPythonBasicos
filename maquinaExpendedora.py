from os import system
vuelto=0
productos = [['Producto A', '270'], ['Producto B', '340'],    ['Producto C', '390']]; monedas = [10, 50, 100]
def menu(productos):
    print('¿Qué producto desea? ')
    for i in range(1, 4):
        print(f'\t{i}. {productos[i-1][0]}')
    elecproducto = int(input())
    try:
      if elecproducto > 0 and elecproducto <= 3:
        return int(productos[elecproducto-1][1])
      else: raise ValueError()
    except ValueError:
      print('Eleccion no valida')
      return menu(productos)

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
    
def maquina_alimentos(prod_elect):
  pago = False
  total_pago = 0
  while not pago:
    # system("clear")
    print('Inserte las moneda: ')
    print('1. Moneda de 10$')
    print('2. Moneda de 50$')
    print('3. Moneda de 100$')
    elec_moneda = int(input())
    try:
        if 1<elec_moneda <3:
         total_pago += monedas[elec_moneda - 1]
        else: raise ValueError()
    except ValueError:
        print(f'Eleccion no valida')
    status=False
    print('Su pago actual es de: ', total_pago)
    input('Presione Enter para continuar...')
    if total_pago >= prod_elect:
      print('Pago completo')
      pago = True
      vuelto = total_pago - prod_elect
      generar_vuelto(vuelto, monedas)

maquina_alimentos(menu(productos))