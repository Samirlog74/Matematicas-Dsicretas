print("-----------------------------------------")
print("Maximo Comun Divisor entre dos números ")
print("-----------------------------------------")
print("-----Algoritmo de Euclides Extendido-----")

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))


cocientes = []
contador = 0
c1 = 0
x1 = 0
x2 = 1
x = [1,0]
y = [0,1]


#----------------------------------------------------------------------------
r = a%b
b1 = b
q = a //b

cocientes.append(q)



while r != 0:
    r1 = b % r
    q = b//r
    cocientes.append(q)
    b = r
    r = r1
print(f"El mcd({a},{b1}) es :  {b}")

#---------------------------------------------------------------------------
#print(coeficientes)
  
n1 = len(cocientes) -1

while contador < n1:
    num1 = (y[x1]) - ((cocientes[c1])*(y[x2]))
    num = (x[x1]) - ((cocientes[c1])*(x[x2]))
    x.append(num)
    y.append(num1)
    x1 += 1
    c1 += 1
    x2 +=1
    contador +=1



print(f"La manera extendida es {a}*{x[-1]} + {b1}*{y[-1]}")
