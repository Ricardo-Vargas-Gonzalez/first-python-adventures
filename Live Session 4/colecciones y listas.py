lista = [5, # entero
          5.5, # flotante
          "cinco", # string - cadena de caracteres
          3 + 4j, # tipo de dato complejo
          ]

for i in lista :
    print(f"{i:7} - tipo: {type(i)}")

print("Tamaño de la lista: ", len(lista), "elementos")

# Crear una lista con los elementos de otra lista mediante su indice
''' # Comentario multilinea}
La lista tiene cuatro elementos. Los indices son: 0, 1, 2, 3
[:2] nos traería los valores de los indices 0 y 1, es decir: 5 y 5.5
[3:] nos traería los valores de los indices 3 y 4, es decir: 3 + 4j
'''

lista2 = lista[:2] # esta función señala a python que corra desde o hasta la linea señalada, esto es un slicing
print(lista * 2) # Se duplica la lista en si misma

# Definimos una funcion
milista = [3, 5, 6, 8, 9, 7, 10, 4, 4, 5, 1, 2]

print("lista original: ", milista, "\n\n")

milista.append(0)
print("Con el append", milista)

milista.insert(3, 100)
print("Con el insert", milista)

milista.extend(range(-1, -4, -1))
print("Con el extend", milista)

del milista[9:]
print("Después del del:", milista)

milista.remmove(5)
milista.remmove(4)
milista.remmove(100)
print("Después del remove()", milista)

print(milista.pop(2))
print(milista.pop())
print("Después del pop()", milista)

#milista.clear()
#print("Después del clear()", milista)