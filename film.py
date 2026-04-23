
def óraperc(p):
    óra = p // 60
    perc = p % 60
    return str(óra) + " óra " + str(perc) + " perc"

cim1 = input("Add meg egy film címét: ")
perc1 = int(input("Hány perces a film: "))
print("A(z)", cim1, "című film", óraperc(perc1), "hosszú.")
cim2 = input("Add meg egy film címét: ")
perc2 = int(input("Hány perces a film: "))
print("A(z)", cim2, "című film", óraperc(perc2), "hosszú.")
cim3 = input("Add meg egy film címét: ")
perc3 = int(input("Hány perces a film: "))
print("A(z)", cim3, "című film", óraperc(perc3), "hosszú.")