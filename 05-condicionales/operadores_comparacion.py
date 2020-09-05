# == igual
# != diferente
# < menor
# > mayor
# <= menor o igual que
# >= mayor o igual que

year = int(input('¿En qué año estamos? '))

print('EJEMPLO 1 >= <=')
if year >= 2021:
  print(f'Estamos de 2021 en adelante')
else:
  print(f'Estamos en 2020')

print('EJEMPLO 2 == ')

if year == 2020:
  print(f'Estamos en {year}')
else:
  print('No estamos en 2020')