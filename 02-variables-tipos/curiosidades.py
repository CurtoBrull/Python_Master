mi_texto = " 'Máster' "
# mi-texto2 = 'Mundo' --- El guion no es válido
mi_texto2 = 'en \"Python\"' # Para incluir comillas en el string se puede utilizar \ para escapar el siguiente caracter.
mi_texto3 = '"Queda claro?"'

mi_texto_unido = mi_texto + ' ' + mi_texto2 + ' ' + mi_texto3
print(mi_texto_unido)

print('------------------')

# \n salto de línea

mi_texto_unido = mi_texto + '\n' + mi_texto2 + '\n' + mi_texto3
print(mi_texto_unido)

# \t tabulación

print('------------------')
mi_texto_unido = mi_texto + '\t' + mi_texto2 + '\t' + mi_texto3
print(mi_texto_unido)

# \r borra lo anterior
print('------------------')
mi_texto_unido = mi_texto + '\r' + mi_texto2 + ' ' + mi_texto3
print(mi_texto_unido)