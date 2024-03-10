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

u = int(input("Ingrese número de unidades a comprar: "))

#Se puede comprar solo más que una unidad:

while u <=0:
  print("Incorrecto, ingrese nuevamente")
  u = int(input("Ingrese número de unidades a comprar: "))

if u <= 9:
  p = u*10
elif u >= 10 and u <=99:
  p = u*8
elif u >=100 and u <=499:
  p = u*7
elif u >= 500:
  p = u*6

c = 0.0825 * p

print("Usted compró ",u," CDs debe abonar: ",p,"$")
print("El empleado tuvo una ganancia de ",c,"$")

