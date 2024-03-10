################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  
Hacer un algoritmo en Pseint donde se ingrese una hora y nos calcule la hora dentro
de un segundo. 
#Autor: Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S")) #Formato de 24 horas 


h = int(input("Ingrese la hora: "))

while h <1 or h > 24:
  print("Hora incorrecta")
  h = int(input("Ingrese la hora: "))

m = int(input("Ingrese los minutos: "))
while m < 1 or m > 60:
  print("Minutos incorrectos")
  m = int(input("Ingrese los minutos: "))

s = int(input("Ingrese los segundos: "))

while s < 1 or s > 60:
  print("Segundos incorrectos")
  s = int(input("Ingrese los segundos: "))

print("La hora ingresada es",h,":",m,":",s)


#Si los minutos son 59 y los segundos 59 cambia de hora:

if s == 59 and m == 59:
  s=0
  m=0
  h=h+1

#Si los segundos son 59 y se le suma 1 aumentan los minutos en 1

elif s == 59:
   s = 0
   m = m+1

# Caso contrario se suma un segundo:

else:

  s= s+1

print("La hora actual es",h,":",m,":",s)

