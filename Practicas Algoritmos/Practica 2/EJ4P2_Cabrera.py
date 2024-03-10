#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

El 14 de febrero una persona desea comprarle un regalo al ser querido que más
aprecia en ese momento, su dilema radica en qué regalo puede hacerle, las
alternativas que tiene son las siguientes

Tarjeta $10.00 o menos
Chocolates $11.00 a $100.00
Flores $101.00 a $250.00
Anillo Más de $251.00


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas



d = int(input("Ingrese presupuesto: "))

# Solo valores positivos

while d <= 0:
  print("Numero incorrecto, reintente")
  d = int(input("Ingrese presupuesto: "))

if d <= 10:
  print("Tarjeta")
elif d >= 11 and d <= 100:
  print("Chocolates")
elif d >= 101 and d <= 250:
  print("Flores")
else:
  print("Anillos")