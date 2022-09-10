# Definimos la tupla
vocales = ('a', 'e', 'i', 'o', 'u')
print(vocales[2])

#Duplicamos la tupla
vocales = vocales * 2
print(vocales)

# Obtenemos el indice de la tupla
print(vocales.index('a'))

# vocales[0] = 'A' # Las tuplas no se pueden modificar, esta linea genera un error

# Conveertimos la tupla en una lista para que podamos modificarla
lista_vocales = list(vocales)
lista_vocales[0] = 'A'
print(lista_vocales)

vocales_tupla2_la_venganza_el_regreso_remasterizada = tuple(lista_vocales)

print(vocales_tupla2_la_venganza_el_regreso_remasterizada)