#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Crear lista de 5 valores asignados manualmente

#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas


# Creamos la lista vacía:

lista = []

# Pedimos al usuario que ingrese 5 elementos:

for i in range(5):
   elemento = input("Ingresar un elemento: ")
   lista.append(elemento)

# Imprimimos la lista

print("La lista asignada es: ",lista)