# Declaramos una variable 
calificación = input("Introduce tu calificación de la AZ-900: ")

calificación = int(calificación)

#preguntamos si laa calificación es menor a 700 
if calificación < 700 :
    print ("ves por no estudiar") # Si es menor a 700 muestra esto 
elif calificación > 1000 :
    print("no loco, tampoco te quieras pasar de verga, solo se puede sacar mil en la certificación")
else  : # Si no se cumple el If anterior, se pasa a esta linea 
    print("felicidades te mamaste, ve por tu certificado de Azure") ##se ejecuta si ninguno de los IF se cumple

# verificador de mayoría de edad
edad = input("introduce tu edad: ")
edad = int(edad)
if edad >= 18 and edad <= 100 :
    print("a huevo, ya eres explotable legalmente")
elif edad > 100 :
    print("no mames ya eres munra")
elif edad < 0 :
    print("no maa eres un homunculo")
else : # recuerda que en else no se debe poner la variable pues ya la determina por defecto 
    print("Nel saquese, huele a carcel")

#EN PYTHON NO HAY SWITCH CASE