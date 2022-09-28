print("------------------------------------------")
print("RSA CALCULATOR 4000")
print("------------------------------------------")

print("Pasos a seguir. \nPaso 1. Elegir p y q")

p = 17
q = 29

print("------------------------------------------")
print("Calcular n y Φn:")

n = p*q
n2 = (p-1)*(q-1)

print("n = " , n ,"\nΦn = ", n2)
print("------------------------------------------")
print("Paso 2. Escogemos un número e, 1 < e < " , n2, "\ntal que mcd(e,",n2,") = 1.")

e = 101

print("------------------------------------------")
print("Paso 3. Calculamos el inverso multiplicativo de e.")
cocientes = []
x = [1,0]
y = [0,1]
c1 = 0
x1 = 0
x2 = 1

r = n2%e
e2 = e
q = n2 //e

cocientes.append(q)
while r != 0:
    r1 = e % r
    q = e//r
    cocientes.append(q)
    e = r
    r = r1
n1 = len(cocientes) -1

while n1 != 0:
    num1 = (y[x1]) - ((cocientes[c1])*(y[x2]))
    num = (x[x1]) - ((cocientes[c1])*(x[x2]))
    x.append(num)
    y.append(num1)
    x1 += 1
    c1 += 1
    x2 +=1
    n1 -= 1

d = y.pop()
print(f"d = {y[-1]}")

print("------------------------------------------")

dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'ñ':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27}

valores=list(dic.values())
claves=list(dic.keys())

frase=input("Ingrese la frase que desea encriptar: ")
frase=frase.lower()

print(frase)
listica= list(frase)

for i in range (len(listica)):
    if listica[i] in dic:
        listica[i]=dic[listica[i]]

for i in range (len(listica)):
  if isinstance(listica[i],int):
    listica[i]=(listica[i]**e2)%n


print(*listica, sep=" ")

print("Desea desencriptar la frase(si o no): ")
op=input()

if op=="si":
  for i in range(len(listica)):
    if isinstance(listica[i],int):
      listica[i]=(listica[i]**d)%n
  
  for i in range(len(listica)):
    if listica[i] in valores:
      listica[i]=claves[listica[i]-1]
  
  print(listica)
  
else:
  print("Fin del programa  :)")


