
print('----EJEMPLO 3-----')

edad = int(input('Introduce tu edad: '))
edad_minima = 18
edad_maxima = 66

# OPERADORES LOGICOS

# and
if edad >= edad_minima and edad <= edad_maxima:
  print('Estás en edad de trabajar')
else:
  print('No tienes edad para trabajar')