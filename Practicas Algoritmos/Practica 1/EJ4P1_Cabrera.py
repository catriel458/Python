################################
# PRACTICA I #
################################

"""


#ENUNCIADO:  
Una empresa se encarga de la venta y distribución de CD vírgenes. Los clientes pueden
adquirir los artículos (supongamos un único producto de una única marca) por
cantidad. Los precios son:
$10. Si se compran unidades separadas hasta 9.
$8. Si se compran entre 10 unidades hasta 99.
$7. Entre 100 y 499 unidades.
$6. Para más de 500 unidades.
La ganancia para el vendedor es de 8,25 % de la venta. Realizar
un algoritmo en Pseint que dado un número de CDs a vender calcule el precio total
para el cliente y la ganancia para el vendedor.  
#Autor: Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S")) #Formato de 24 horas 

id = int(input("Elegir empleado: 1 cajero, 2 servidor, 3 mezclas , 4 mantenimiento: "))

while id < 1 or id > 4:
  print("Valor incorrecto, reintente")
  id = int(input("Elegir empleado: 1 cajero, 2 servidor, 3 mezclas , 4 mantenimiento: "))

d = int(input("Elegir dias trabajados: "))

while d < 1 or d > 6:
  print("Valor incorrecto, reintente")
  d = int(input("Elegir dias trabajados"))

if id == 1:
  s = 56*d
  print("El empleado ganará ",s,"$")

elif id == 2:
  s = 64*d
  print("El empleado ganará ",s,"$")

elif id == 3:
  s = 80*d
  print("El empleado ganará ",s,"$")

elif id == 4:
  s = 40*d
  print("El empleado ganará ",s,"$")