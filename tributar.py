Age = 0
Income = 0
flag = False

def NoNegAge(flag):
    while(flag==False):
        Age = int(input("Ingrese su edad.\n"))
        if Age < 0:
            print("¿Edad negativa?")
        else:
          flag=True
          return Age

def CalcTaxes(Age, Income):
    Income = int(input("Ingrese sus ingresos.\n"))
    if (Age > 16):
        if (Income > 999):
            print("Usted debe tributar por sus ingresos.\n")
    else:
      print("Usted no debe tributar.\n")
      raise ValueError()

while(flag==False):
    try:
      CalcTaxes(NoNegAge(Age), Income)
      flag = True
    except:
        print("Introduzca un número ome.")