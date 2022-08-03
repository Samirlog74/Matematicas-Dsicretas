#Ejercicio 5 del laboratorio 1 - Matematicas Discretas.

Lista1 = []
valores = [True, False]
print("--------------------------------------------")
print("(p => q) y r      =\t(¬p y r) o (q y r)")

for p in valores:
    for q in valores:
        for r in valores:
            Lista2 = []
            P = (not p or q) and r
            Q = (not p and r) or (q and r)
            A = (not P or Q)and(not Q or P)
            Lista1.append(A)
            Lista2.append(A)

            print(P,"", Lista2 ,"",Q,sep = "\t")

print("--------------------------------------------")

if all(Lista1) == True:
    print("Es una tautología.")

else:
    print("No es una tautología.")

print("--------------------------------------------")
