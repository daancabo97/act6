# Escribir un programa que almacene en una lista los siguientes precios,
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for p in precios:
    if p < min:
        min = p
    elif p > max:
        max = p 
print("El precio minimo es : " + str(min)) 
print("El precio maximo es : " + str(max))