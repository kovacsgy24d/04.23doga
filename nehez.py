from allat import Allatfaj

a1 = Allatfaj(input("Első állat neve: "), float(input("Tömege: ")))
a2 = Allatfaj(input("Második állat neve: "), float(input("Tömege: ")))
a3 = Allatfaj(input("Harmadik állat neve: "), float(input("Tömege: ")))
legnehezebb = a1
if a2.tomeg > legnehezebb.tomeg:
    legnehezebb = a2
if a3.tomeg > legnehezebb.tomeg:
    legnehezebb = a3
f = open("legnehezebb.txt", "w", encoding="utf-8")
f.write("A(z) " + legnehezebb.nev + " a legnehezebb.")
f.close()