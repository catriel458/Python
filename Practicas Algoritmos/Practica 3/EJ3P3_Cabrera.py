#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Crear dos listas de 10 elementos y sumarlos en una tercera lista resultante:

Pedir valores numéricos en dos arrays
distintos de 10 y almacenar el resultado de
los valores de cada posición en un tercero
de la misma dimensión (posición 0 del
arreglo 1 + posición 0 del arreglo 2) y
mostrar el contenido de los 3 arreglos de
esta forma. valor pos 0 arreglo 1 + valor
pos 0 arreglo 2 = valor pos 0 arreglo 3 valor
pos 1 arreglo 1 + valor pos 1 arreglo 2 =
valor pos 1 arreglo 3 y así sucesivamente).


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas



# Creamos la primera lista:

lista1 = []

for i in range(10):
  elemento = int(input("Ingrese valor: "))
  lista1.append(elemento)

# Creamos segunda lista:

lista2 = []

for i in range(10):
  elemento = int(input("Ingrese valor: "))
  lista2.append(elemento)

# Creamos lista resultante

lista3 = []

for i in range(10):
  lista3.append(lista1[i]+lista2[i]) # Con el metodo append agregamos elementos a la lista vacia.

print("La lista resultado es: ", lista3)
