#Ejercicio 1,2,3,4 del laboratorio 1 - Matematicas Discretas.

valores = [True, False]

print("p \tq \tp y q \tp o q \tp => q \tp <=> q")

for p in valores:
    for q in valores:
        print(p,q, p and q, p or q, not p or q, (not p or q)and(not q or p),  sep = "\t")