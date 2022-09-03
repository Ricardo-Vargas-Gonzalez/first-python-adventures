# el primer programa es 
# HOLA MUNDO
print("esto no es brujeria es tecnología ")
print("suma de dos enteros")
print('''Introduce dos numeros enteros y despues los sumare y \
te mostrare el resultado''')

primer_numero = input('Introduce el primer numero entero: ')

if primer_numero.isnumeric() :
   try:
    primer_numero = int(primer_numero)
   except ValueError:
    print("Debes introducir un numero entero")
    exit()

else :
    print("Debes introducir un numero entero")
    # Aquí te regresa al inicio del programa
    exit()

segundo_numero = input('Introduce el segundo numero entero: ')

if segundo_numero.isnumeric() :
   try:
    segundo_numero = int(segundo_numero)
   except ValueError:
    print("Debes introducir un numero entero")
    exit()

else :
    print("Debes introducir un numero entero")
    # Aquí te regresa al inicio del programa
    exit()

suma = primer_numero + segundo_numero

print('El resultado es: ' + str(suma))
print('El resultado es:', suma)
print(f'El resultado es: {suma}')
print("El resultado es: %d" % suma)