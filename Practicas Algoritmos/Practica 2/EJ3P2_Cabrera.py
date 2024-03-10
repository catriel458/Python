#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Realice un algoritmo para determinar el sueldo semanal de un trabajador con
base en las horas trabajadas y el pago por hora, considerando que después de las
40 horas cada hora se considera como excedente y se paga el doble.


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas


pago_hora = int(input("Ingrese el pago por hora: "))
horas = int(input("Ingrese las horas semanales trabajadas: "))

# Horas es un numero positivo:

while horas < 0:
    print("Escribir valor positivo")
    horas = int(input("Ingrese las horas semanales trabajadas: "))

if horas < 40:
    sueldo = pago_hora*horas
    print("Su sueldo es: ", sueldo)

else:
    sueldo = pago_hora*horas*2
    print("Su sueldo es: ", sueldo)
