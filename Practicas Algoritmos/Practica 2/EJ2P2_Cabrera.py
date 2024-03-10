#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Realice un algoritmo para determinar si una persona puede votar con base en su edad en
las próximas elecciones


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas

edad = int(input("Ingrese edad: "))

if edad >= 18:
    print("Usted puede votar")
else:
    print("No puede votar")
