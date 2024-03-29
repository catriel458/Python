# -*- coding: utf-8 -*-
"""Ejercicios python extra ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gm2ckVtRE6kzB74vx20qgk2qhktgRodq

**NIVEL 1**

1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

print("El programa devuelve el mayor de los numeros ingresados")
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

def maximo(n1,n2):
  if n1>n2:
    print(n1)
  elif n1<n2:
    print(n2)
  else:
    print("Los numeros son iguales")

# Una vez definida la función la invocamos para mostrar el resultado

print("Resultado: ")
maximo(n1,n2)

"""2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos."""

print("El programa devuelve el mayor de los numeros ingresados")
a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))
c = int(input("Ingrese segundo numero: "))

def max_de_tres(n1,n2,n3): #Cuando defino la función son parametros
  if n1>n2 and n1>n3:
    print(n1)
  elif n2>n1 and n2>n3:
    print(n2)
  elif n3>n2 and n3>n1:
    print(n3)
  else:
    print("Los tres numeros ingresados son iguales")

print("Resultado: ")
max_de_tres(a,b,c) # Invoco la función con los argumentos (que son los inputs)

"""**Hacer una funcion imprimir que imprima los elementos de una lista**"""

compras = ["Azucar",10,"Harina",500.2,"Leche",1,"Manteca",False,"Jamon",True,"Huevos"]

def imprimir (compras):
  for mercaderia in compras:
    print (mercaderia)
imprimir (compras)

"""Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio."""

# Recorrer una lista usando el bucle for:

lista = [1,2,3,4,5]

for elemento in lista:
  print(elemento)

def longitud(lista):
  a = 0
  for x in lista:
     a = a + 1
  print("La cantidad de elementos de la lista es: ",a)

longitud([1,2,3,4,"Conejo",6,7,8,10,55,"Perro",897.6])
longitud("hola")

"""4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False."""

# vocales a,e,i,o,u

print("¿Es vocal?")

b = input("Ingrese un caracter: ")

def es_vocal(c):
  if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "U" or c == "O":
    print(True)
  else:
    print(False)

print("Resultado:")
es_vocal(b)

"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""

def sum(lista):
  n = 0
  for x in lista:
    n+=x
  print("La suma de los elementos de la lista es: ",n)

def multip(lista):
  n = 1
  for x in lista:
    n = n*x
  print("el producto de los elementos de la lista es: ",n)

sum([1,2,3,4])
multip([1,2,3,4])

"""Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""



"""Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

"""



"""Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

"""

def superposicion(lista1,lista2):
  for x in lista1:
    for y in lista2:
      if x == y:
        return True
  return False

superposicion([2,3],[4,5])

"""Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""

def generar_n_caracteres(n,c):
  for i in range(1,n,1):
    print(c)

generar_n_caracteres(5,"x")

def generar_n_caracteres(n,c):
  print(n*c)

generar_n_caracteres(5,"x")

"""Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla"""

def procedimiento(lista):
  for x in lista:
    print(x*"*")

procedimiento([4,9,7])

"""**NIVEL 2**

La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

def max_in_list(lista):
  inicio = 0
  for x in lista:
    if x > inicio:
      inicio = x
  return inicio

max_in_list([1,2,9,4])

"""Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""

"""
len()
El método len() devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario.

len() toma un argumento, que puede ser una secuencia (como una cadena, bytes, tupla, lista o rango) o colección (como un diccionario, conjunto o conjunto "set" congelado "set frozen").
"""

def mas_larga(lista):
  inicio = ""
  for x in lista:
    if len(x) > len(inicio):
      inicio = x
  return x

mas_larga(["Hola","Elizabeth","DiositoGood666"])

"""Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista,n):
  nueva_lista = []
  n = int(input("Ingrese cantidad de caracteres: "))
  for x in lista:
    if len(x) > n:
      nueva_lista.append(x)
  return(nueva_lista)

filtrar_palabras(["Hola","Perro","Muchedumbre"],4)

"""**Ejercicio 4**
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

**tittle():** transformado la primera letra de cada palabra en mayúscula
**upper():** Con este método conseguiremos convertir todos y absolutamente todos los caracteres de un string en mayúsculas, da igual lo largo que sea.
**lower():** Y como gemelo opuesto pero no malvado, tenemos el método **lower()** que hace exactamente lo contrario, lo convierte todo en minúsculas.
"""

# def cant_mayus(str):

# No me sale

"""****
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

curso = int(input("ingrese el año del curso: "))
nombre1=input("ingrese su nombre: ")
cumpleaños1=int(input("ingres su año de nacimiento: "))
nombre2=input("ingrese su nombre: ")
cumpleaños2=int(input("ingres su año de nacimiento: "))
nombre3=input("ingrese su nombre: ")
cumpleaños3=int(input("ingres su año de nacimiento: "))
print(nombre1," ","cumplirá ",curso-cumpleaños1," años")
print(nombre2," ","cumplirá ",curso-cumpleaños2," años")
print(nombre3," ","cumplirá ",curso-cumpleaños3," años")

"""https://ellibrodepython.com/tuplas-python Tuplas


"""

lista = [1,2,3,4]
lista[0] = 69

print(lista) # son mutables

tupla = () # Las tuplas son inmutables (no se pueden agregar ni modificar datos). Las tuplas suelen ser mas rapidas.
print(tupla)

print(type(lista))
print(type(tupla))

"""Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
"""

edades = (14,19,25,47,78,98,87,98,52,99)
cantidad = 0
for elemento in edades:
  if elemento > 20:
    cantidad+=1 # variable acumuladora
print("La cantidad de personas con edades superiores a 20 años son: ",cantidad)

"""**Definir** una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

lista = []

for i in range(5):
  agregar = input("Escriba su nombre: ")
  lista.append(agregar)

cantidad = 0

for elemento in lista:
  if elemento[0] == "a" or elemento[0] == "A" or elemento[0] == "á" or elemento[0] == "Á":
      cantidad+=1
print("La cantidad de palabras que comienzan con a es: ",cantidad)

"""Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

palabra_ingresada = input("Ingrese palabra: ")

def contar_vocales(palabra):
  #Definimos las acumuladoras
  a = 0
  e = 0
  i_ingresada = 0
  o = 0
  u = 0
  for i in range(len(palabra)):
    if palabra[i] == "a" or palabra[i] == "A":
      a+=1
    elif palabra[i] == "e" or palabra[i] == "E":
      e+=1
    elif palabra[i] == "i" or palabra[i] == "I":
      i_ingresada+=1
    elif palabra[i] == "o" or palabra[i] == "O":
      o+=1
    elif palabra[i] == "u" or palabra[i] == "U":
      u+=1
  print("la cantidad a es: ",a)
  print("la cantidad e es: ",e)
  print("la cantidad i es: ",i_ingresada)
  print("la cantidad o es: ",o)
  print("la cantidad u es: ",u)
  print("La cantidad de vocales que tiene la palabra ",palabra_ingresada," es: ",a+e+i_ingresada+o+u)


contar_vocales(palabra_ingresada)

"""

Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400. Operador modulo: https://www.freecodecamp.org/espanol/news/el-operador-del-modulo-python-que-significa-el-simbolo-de-porcentaje-en-python-resuelto/
"""

def es_bisiesto(año): # % modulo da el resto del cociente
  if año % 4 == 0 and (not(año % 100 == 0)):
    print("El año ",año," Es bisiesto porque es multiplo de 4")
  elif año % 400 == 0:
    print("El año ",año," Es bisiesto porque es multiplo de 400")
  else:
    print("El año ",año,"No es bisiesto")


año_ingresado = int(input("Ingrese el año: "))
es_bisiesto(año_ingresado)