print("-----------------------------------------")
print("Números random")
print("-----------------------------------------")

m = int(input("Del 1 hasta qué número desea generar los números: "))
cantidad = int(input("Ingrese la cantidad de números que desea generar: "))



num_random =[]

x_0 = 1
a = 2


# Primera condicion

if m %2 == 0:
    c = m - 1

else:
    c = 2
    

#Segunda condicion

if m % 2 == 0:
    a = a**2






#Tercera condicion

if m % 4 == 0:
    a = 5
 
    








while cantidad != 0:
    num = ((a*x_0) + c) % m
    num_random.append(num)
    x_0 = num
    cantidad -= 1




print("\n-----------------------------------------")
print(num_random)
print("-----------------------------------------")