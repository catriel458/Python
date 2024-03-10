#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Pediremos los IDs (números) de alumnos
de dos clases, álgebra y análisis que se
guardaran en dos arreglos. Queremos
mostrar todos los alumnos comunes en las
dos asignaturas. Estos alumnos se
guardaran en un tercer arreglo y que sea el
que se muestre, las coincidencias. También
debe mostrarse al final el número de
alumnos que se repiten.


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas



algebra = []
analisis = []
coincidencias = []

for i in range(0,5,1):
  dni = int(input("Ingrese DNI: "))
  algebra.append(dni)

for i in range(0,5,1):
  dni = int(input("Ingrese DNI: "))
  analisis.append(dni)

  
  

def buscarCoincidencias(lista1,lista2):
  encuentra = 0
  for x in lista1:
    for y in lista2:
      if x == y:
        encuentra = 1
        coincidencias.append(x)
  if encuentra == 0:
    print("No hay condicencias")
  else:
    print("La lista coincidencias es: ",coincidencias)
  
buscarCoincidencias(algebra,analisis)
