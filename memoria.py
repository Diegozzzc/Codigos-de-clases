
def obtener_calificacion():
  calificacion = int(input( "Introduzca la calificación: "))
 
  return calificacion
calificaciones = []

for i in range(5):
  calificacion = obtener_calificacion()
  calificaciones.append(calificacion)

print("Calificaciones:", calificaciones)

