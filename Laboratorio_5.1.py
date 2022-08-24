
print("-----------------------------------------")
print("Números random")
print("-----------------------------------------")

m = int(input("Del 1 hasta qué número desea generar los números: "))
cantidad = int(input("Ingrese la cantidad de números que desea generar: "))



num_random =[]

x_0 = 5
a = 3
c = 2


while cantidad != 0:
    num = ((a*x_0) + c) % m
    num_random.append(num)
    x_0 = num
    cantidad -= 1




print("\n-----------------------------------------")
print(num_random)
print("-----------------------------------------")