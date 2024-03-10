################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  
Hacer un algoritmo en Pseint que lea un número y según ese número, 
indique el día que corresponde.
#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S")) #Formato de 24 horas 


n = int(input("Ingrese numero de día: "))

if n == 1:
  print("Lunes")
elif n == 2:
  print("Martes")
elif n == 3:
  print("Miercoles")
elif n == 4:
  print("Jueves")
elif n == 5:
  print("Viernes")
elif n == 6:
  print("Sábado")
elif n == 7:
  print("Domingo")

else:
  print("El número de dia ingresado: ",n," ,es incorrecto")
  
