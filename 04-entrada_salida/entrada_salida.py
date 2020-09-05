# Entrada

nombre = input('¿Cuál es tu nombre? ')
edad = input('¿Cuál es tu edad? ')

# Salida

print(f'Me has dicho que tu nombre es {nombre} y tienes {edad} años')
print(f'En 10 años tendrás {int(edad) + 10}') # Si no se convierte a entero no se pueden summar variables en un string