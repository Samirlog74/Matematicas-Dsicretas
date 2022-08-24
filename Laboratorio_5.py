
print("-----------------------------------------")
print("Algoritmo de Exponenciación rapida")
print("-----------------------------------------")


print("Calcular cierta matriz A con cierto exponente")
a = int(input("Ingrese el exponente de la matriz a calcular: "))

residuos = []
b = 2
n = 0
resultado = " "
contador = 0


r = a%b
c = a//b
b1 = b

residuos.append(r)

while c != 0:
    r = c % b
    residuos.append(r)
    c = c//b


while contador < len(residuos):
    if residuos[n] == 1:
        exponentes = b**n
        resultado = "A**"+ str(exponentes)+ "  " + resultado
    
    n+= 1
    contador +=1

print("\n-----------------------------------------")
print("La matriz A**" , a , " = " + resultado)
print("-----------------------------------------")

