#Expansion de cantor de cierto número



print("-------------------------------------------")
a = int(input("Ingrese un número entero: "))
print("-------------------------------------------")

residuos = []
b = 2
contador = 0
n = 1
num = 0
resultado = " "
mas = "+"

r = a%b
c = a//b

residuos.append(r)
while c != 0:
    b += 1
    r = c % b
    residuos.append(r)
    c = c//b
    
     
print ("La expansion de cantor del número" , a, " es:")
print("-------------------------------------------")

while contador < len(residuos):
    numero = residuos[num]
    resultado = mas  + " (" +str(numero) + ")"  + str(n) + "! "  + resultado
    contador +=1
    n+= 1
    num += 1
    
    if contador == len(residuos) - 1:
        mas = "="

print(resultado)
print("-------------------------------------------")
    
    


