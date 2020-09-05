# Nombre de la variable = valor

texto = 'Master en Python'
texto2 = 'Estudiado por Javier Curto'
numero = 41
decimal = 41.3

print(texto +' '+ texto2)
# %s string %d integer %f floating %.xf floating con x decimales 
# %x %X Integers en hex (lower uppercase)
print('Hola, tengo %s años, para ser exactos %.1f' % (numero, decimal))

nombre = 'Javier'
apellidos = 'Curto Brull'
web = 'http://curtobrull.github.io/'

# Concatenar con + y con f-string f"{}"
print('---------------------------------------------')
print(nombre + " " + apellidos + " - " + web)
print('---------------------------------------------')
print(f"{nombre} {apellidos} - {web}")
print('---------------------------------------------')
print(f'5 x 5 =  {5*5}')

# Interpolar
print('---------------------------------------------')

nombre2 = f'Izhan {apellidos}'
print(nombre2)

# .format
print('---------------------------------------------')

print('Hola me llamo {} {} y mi web es: {}'.format(nombre, apellidos, web))

print('---------------------------------------------')
# No es concatenación pero se parece

print(nombre, apellidos, web)