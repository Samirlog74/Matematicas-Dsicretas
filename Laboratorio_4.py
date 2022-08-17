print("-----------------------------------------")
print("Maximo Comun Divisor entre dos números ")
print("-----------------------------------------")
print("-----Algoritmo de Euclides Extendido-----")

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))


coeficientes = []
contador = 0
c1 = 0
c2 = 0
x1 = 0
x2 = 1
y1 = 0
y2 = 1
x = [1,0]
y = [0,1]


#----------------------------------------------------------------------------
r = a%b
b1 = b
q = a //b

coeficientes.append(q)



while r != 0:
    r1 = b % r
    q = b//r
    coeficientes.append(q)
    b = r
    r = r1
print(f"El mcd({a},{b1}) es :  {b}")

#---------------------------------------------------------------------------
#print(coeficientes)
  
n1 = len(coeficientes) -1

while contador < n1:
    num = (x[x1]) - ((coeficientes[c1])*(x[x2]))
    x.append(num)
    x1 += 1
    c1 += 1
    x2 +=1
    contador +=1


contador = 0
while contador < n1:
    num1 = (y[y1]) - ((coeficientes[c2])*(y[y2]))
    y.append(num1)
    y1 += 1
    c2 += 1
    y2 +=1
    contador += 1


print(f"La manera extendida es {a}*{x[-1]} + {b1}*{y[-1]}")
