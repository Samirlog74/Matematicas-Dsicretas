print("-----------------------------------------")
print("Un número en base según el usuario ")
print("-----------------------------------------")


a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese la base deseada > 1: "))
residuos = []



r = a%b
c = a//b
b1 = b

residuos.append(r)




while c != 0:
    
    r = c % b
    residuos.append(r)
    c = c//b

print("-----------------------------------------")
print("El número ",a," en base ", b1," es:","".join([str(_) for _ in residuos[::-1]]))
print("-----------------------------------------")