
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

fila_seleccionada = 3 
if 0 <= fila_seleccionada < len(matriz):
    print(f"\nFila {fila_seleccionada + 1}: {matriz[fila_seleccionada]}")
else:
    print(f"\nLa fila {fila_seleccionada + 1} no es válida para esta matriz.")

