
materias = ["Matemáticas", "Física", "Química", "Biología", "Historia"]
calificaciones = []

for i in range(10):
  alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
  calificaciones_alumno = []
  for materia in materias:
    calificacion = float(input(f"Ingrese la calificación de {materia} para {alumno}: "))
    calificaciones_alumno.append(calificacion)
  calificaciones.append(calificaciones_alumno)

for i in range(10):
  alumno = calificaciones[i][0]
  print(f"Calificaciones de {alumno}:")
  for j in range(5):
    print(f"  {materias[j]}: {calificaciones[i][j]}")
