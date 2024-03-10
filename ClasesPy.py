# Operadores en Python

# numero1=15
# numero2=20
# print(numero1==numero2)

# print(numero1!=numero2)

# print(numero1>numero2)
# print(numero1<numero2)

# edad = 20
# viene_acompañado = False
# print(edad > 18 and viene_acompañado)

# edad = 20
# viene_acompañado = False
# print(edad > 18 or viene_acompañado)

# edad = 15
# viene_acompañado = True
# print(edad > 18 or viene_acompañado)

# edad = 15
# viene_acompañado = False
# print(edad > 18 or viene_acompañado)

# edad = 15
# viene_acompañado = False
# print(not edad > 18 or viene_acompañado)

# edad = 15
# viene_acompañado = False
# print(not (edad > 18 or viene_acompañado))

# edad = 20
# viene_acompañado = False
# print(not (edad > 18 or viene_acompañado))

# lista = [25,56,45,87,True,"Lopez"]
# print(24 in lista)
# print("Lopez" in lista)
# print("Perez" not in lista)

# lista.append("Jose Perez")
# print(lista)

# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# print(type(edad))

# anio_actual = 2023
# anio_nacimiento = input("ingrese año de nacimiento: ")
# edad = anio_actual - int(anio_nacimiento)
# # edad= anio_actual - float(anio_nacimiento)
# print("La edad es: ",edad)

# numero = 10
# if numero < 10:
#     print ("El numero es menor a 10")
#     print ("es el verdadero del fin")
# # print ("hola a todos ")
# else :
#     print ("El numero es mayor a 10")


# numero = 10
# if numero < 10:
#     print ("El numero es menor a 10")
#     print ("es el verdadero del fin")
# elif numero == 10:
#     print ("El numero es igual a 10")

# else :
#     print ("El numero es mayor a 10")

# numero = 10
# if numero < 10:
#     print ("El numero es menor a 10")
#     print ("es el verdadero del fin")
# else:
#     if numero == 10:
#         print ("El numero es igual a 10")
#     else:
#         print ("El numero es mayor a 10")

# contador = 1
# while contador <= 20:
#     print(contador)
#     contador+= 1

# lista = [5, 8.9, 'arturo',False, 'celia']
# for i in range (5) :
#     print(lista[i])

# for elemento in lista :
# print (elemento)
# print ("CANTIDAD DE LEMENTOS CONTENIDOS EN LA LISTA", len(lista))

# for i in range (3 , 5) :
#      print(lista[i])

# nombre = "carlos"
# print ("cantidad de caracteres: ", len (nombre))

# Buscador

# lista = [5, 8.9, 'arturo',False, 'celia']
# for i in range (5):
#     # print (lista[i] )
#     if lista [i] == "arturo" :
#         print ("Elemento encontrado")

# nombres = ["a","b","c","d",28,True]
# # print(len(nombres))
# # print(nombres)

# for i in range(len(nombres)):
#     print(nombres[i])

# for i in range(5):
#     if i == 3:
#         pass
#     else:
#         print(i)

# articulos = [("articulo 1",250.50,1000),("articulo 2",175.89,50)]

# for i in range(len(articulos)):
#     if articulos[i][2] > 500:
#         print(articulos[i])
#     else:
#         pass

# lista = [1,3,True,"Hola",1.75]

# for elemento in lista:
#     if elemento == "Hola":
#         break
#     print(elemento)

# lista = [1.789,3,False,"Hola",1.75]

# for elemento in lista:
#     if not elemento:
#         continue
#     else:
#         print(elemento)


# def sumar(n1,n2):
#     suma = n1+n2
#     print("el resultado de la suma es: ",suma)

# sumar(4,5)


# def sumar(n1, n2):
#     suma = n1 + n2
#     return suma

# print(sumar(5,10))

# print("el resultado de la suma es: ",sumar(7,8))

# resultado = sumar(7,8)
# print("El resultado de la suma es: ",resultado)


mis_datos = {"nombre": "Lucia", "apellido": "Ramirez",
             "edad": 24, "trabaja": True, "Productos": ["Coca", 24, False]}

# print("nombre: ",mis_datos["nombre"]," Apellido: ",mis_datos["apellido"])

# mis_datos["edad"]=32
# print(mis_datos)

# claves = ("nombre","apellido","edad","trabaja")
# valores = ("Juan","Rodriguez",28,True)

# mis_datos3 = dict(zip(claves,valores))
# print(mis_datos3)

# print(mis_datos.items())

# print(mis_datos.keys())

# print(mis_datos.values())

# mis_datos.pop("trabaja")

# print(mis_datos)

# mis_datos["beca"] = True
# print(mis_datos)

# print("La longitud de mi diccionario es ",len(mis_datos))

# alumnos = {1: "Jose Perez", 2: "Celia Ramos"}

# print(alumnos.keys())

# def sumar(*args):
#     s=0
#     for valor in args:
#         s += valor
#     print("El resultado de la suma es: ",s)

# sumar(3,5,6,7)

# def minfun(**kwargs):
#     for clave,valor in kwargs.items():
#         print(clave," = ",valor)

# minfun(ciudad = "salta",provincia = "Bs As")

# def sumar(**kwargs):
#     s = 0
#     for valor in kwargs.values():
#         s+=valor
#     print("la suma de los numeros es: ",s)
 
# sumar(a=5,b=9,c=21)

# conjunto = {1,3,8,9,1,1,4,5,6,3}
# print(conjunto)

# conjunto_vacio = set()
# f = frozenset([3,5,6,7,9,7,6,8])
# print(f)

# mi_conjunto = {1,6,9,5,4}

# for elemento in mi_conjunto:
#     print(elemento)

# nombre = "Catriel"
# apellido = "Cabrera"

# print(f"El nuevo compañero se llama {nombre} y su apellido es {apellido}")

# personas = [["Ana",32],["Juan",15],["Francisca",25]]

# for persona in personas:
#     print(f"¿la persona {persona[0]} es mayor de edad? {True if persona[1]>=18 else False}")

# import json

# with open("test.json") as file:
#     datos = json.load(file)

# # print(type(datos))

# for key,value in datos.items():
#     print(key," - ",value)

