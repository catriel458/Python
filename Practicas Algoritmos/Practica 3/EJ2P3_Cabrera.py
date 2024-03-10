#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Crear lista de 10 valores asignados manualmente y calcular el promedio

#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas


lista = []

# Creamos la lista

for i in range(10):
  elemento = int(input("Ingrese valor: "))
  lista.append(elemento)

# Calculamos el promedio para eso la recorremos

s = 0

for elemento in lista: #Hay otras formas de recorrerla, me gusta esta porque es parecida al for of de JS
  s = s + elemento

p = s/len(lista)

print("El promedio de los elementos de la lista es: ",p)
