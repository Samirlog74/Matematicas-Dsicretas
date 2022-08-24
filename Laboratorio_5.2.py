
print("--------------------------------------------------------------------------")
print("Encontrar el residuo de un número elevado a un exponente dividido por otro")
print("--------------------------------------------------------------------------")


num = int(input("Ingrese el número: "))
a = int(input("Ingrese el exponente del número: "))
div = int(input("Ingrese por quien desea dividirlo: "))

residuos = []
nums_expo = []
nums_residuos = []
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
        nums_expo.append(exponentes)
        resultado = str(num) +"**"+ str(exponentes)+ "  " + resultado
    
    n+= 1
    contador +=1

print("\n-----------------------------------------")
print( num, "**",a ,"mod ",div , " = (",resultado,") mod ",div)
print("-----------------------------------------")


contador = 0
n = 0
while contador < len(residuos):
    num1 = (a**nums_expo[n]) % div
    nums_residuos.append(num1)




    n+=1
    contador += 1