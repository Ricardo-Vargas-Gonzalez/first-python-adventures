numero= 1 # Scope Global

for i in 1, 2, 3: # Scope Local
    print(i)

for i in range(4): # Scope Local
    print(i)

for i in ["Python", "Java", "Javascript", "swift", "HTML", "kotlin", "Dark", "C", "C#"] :
    if i == "HTML":
        print("sal de ahí HTML esa no es tu familia")
    else:
        print(i)

# Imprimir los número primos del uno al 100
# Número primo es el que solo se puede dividir por 1 y por si mismo

for i in range(2, 100) :
    primo = True
    for j in range(2, i) :
        if i == j :
            break 
        elif i % j == 0 :
            primo = False
        else :
            continue

    if primo :
        print(i, end=' ')