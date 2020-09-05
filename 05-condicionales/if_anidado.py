edad = int(input('Introduce tu edad: '))
nombre = 'Javier'
ciudad = 'Almería'
continente = 'Europa'
mayoria_edad = 18

if edad >= mayoria_edad:
  print(f'{nombre} es mayor de edad')
    
  if continente != 'Europa':
    print(f'{nombre} no es Europeo')
  else:
    print(f'{nombre} es Europeo de la ciudad de {ciudad}')
else:
  print(f'{nombre} es menor de edad')

print('----EJEMPLO 2-----')

dia = int(input('Introduce el Nº de día de la semana '))
'''
if dia == 1:
  print('Es Lunes')
else:
  if dia == 2:
    print('Es Martes')
  else:
    if dia == 3:
      print('Es Miécoles')
    else:
      if dia == 4:
        print('Es Jueves')
      else:
        if dia == 5:
          print('Es Viernes')
        else:
          if dia == 6:
            print('Es Sábado')
          else:
            if dia == 7:
              print('Es Domingo')
            else:
              print('Numero de día incorrecto')
'''

if dia == 1:
  print('Es lunes')
elif dia == 2:
  print('Es martes')
elif dia == 3:
  print('Es miércoles')
elif dia == 4:
  print('Es jueves')
elif dia == 5:
  print('Es viernes')
elif dia == 6:
  print('Es sabado')
elif dia == 7:
  print('Es domingo')
else:
  print('Nº de día incorrecto')
