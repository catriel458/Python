#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Buscar un elemento dentro de un arreglo,
que nosotros ingresamos por teclado. Dicho
arreglo se carga previamente de forma
interactiva. Indicar las posiciones donde se
encuentra. Si hay más de uno, indicar
igualmente la posición.


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S"))  # Formato de 24 horas




lista_uno = []

for i in range(0,5,1):
  elemento = int(input("Ingrese el precio: "))
  lista_uno.append(elemento)

concidencia = int(input("Ingrese valor a buscar: "))

def buscar_elemento(lista,valor_busqueda):
  encuentra = 0
  contador = 0
  for valor in lista:
    contador += 1
    if valor == valor_busqueda:
      encuentra = 1
      print("Hay coincidencia con: ",valor, "en la posición: ",contador-1)

  if encuentra == 0: # Variable bandera o flag
     print("No hay coincidencia")

buscar_elemento(lista_uno,concidencia) 
