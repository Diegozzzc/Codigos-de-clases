from array import array

frutas = array('u')
frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")
print(frutas)

frutas.pop(0)
frutas.pop(1)
frutas.append("Sandía")
print(frutas)
