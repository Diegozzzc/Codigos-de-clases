def fibonacci(n):
  

  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
numero = int(input("¿Cuántos números de la secuencia Fibonacci deseas ver?: "))

print("Los primeros", numero, "números de la secuencia Fibonacci son:")
for i in range(numero):
  print(fibonacci(i))
