#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Diseñe un arreglo en el que se ingrese la
cantidad de productos y sus respectivos
precios, para la preparación de un plato,
también se debe mostrar al final el costo a
gastar.


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas


productos = []
precios = []

# Hacemos lista de productos

for i in range(0,5,1):
  p = input("Ingrese el producto: ")
  productos.append(p)

for i in range(0,5,1):
  pr = int(input("Ingrese el precio: "))
  precios.append(pr)

# Ahora sumamos los precios:

suma = 0
for valor in precios:
  suma += valor # suma = suma + valor
print("El costo es: ",suma)
