import random
arrayNum=[]

for i in range(0,9):
  arrayNum.append(random.randint(0,100))
print(f'Lista base {arrayNum}')
arrayNum.sort(reverse=True)


array2=[random.randint(0,100) for _ in range(9)]
print(f'Lista en orden ascendente {sorted(array2)}')
print(f'Lista en orden descendente {sorted(array2,reverse=True)}')
