#################################
# PRACTICA I #
################################

"""

#ENUNCIADO:  

Hacer un algoritmo que simule el sombrero seleccionador, el cual es un sombrero
mágico que hablaba en el colegio Hogwarts de Magia y Hechicería. El sombre decide a
cuál de las cuatro casas de estudiantes va a ir quien se lo pruebe, dichas casas son:
a. Gryffindor
b. Ravenclaw
c. Hufflepuff
d. Slytherin
Mencionado algoritmo deberá hacer preguntas y en base a las respuestas elige a que
casa irá el estudiante
P1 ¿ Te gusta el Amanecer o el Anochecer? (opciones 1: Amanecer 2: Anochecer)
Si se elige la opción 1 Gryffindor y RavenClaw obtienen un punto, si se elige la
opción 2 Hufflepuff y Slytherin obtienen 1 punto, otra opción debe marcarse
opción inválida.
P2 ¿Cuándo muera quiero que la gente me recuerde cómo? (opciones 1: El/La bueno/a
2: El/La grande 3: El/La audaz 4: El/La sabio/a)
Si se elige la opción 1 Hufflepuff suma 2 puntos, opción 2 Slytherin suma 2
puntos, opción 4 RavenClaw suma 2 puntos y opción 5 Griffindor suma 2 puntos, otra
opción debe marcarse como inválida
P3 ¿Qué instrumento agrada más a tu oído? (opciónes 1:Violin 2: Trompeta 3:Piano
4:Tambor)
Si se elige la opción 1 Slytherin suma 4 puntos, opción 2 Hufflepuff suma 4
puntos, opcion 3 RavenClaw suma 4 puntos y opción 4 Gryffindor suma cuatro puntos,
otra opción debe marcarse como inválida
Una vez evaluado esto, debe imprimirse que casa es la elegida en base a la de mayor
puntos obtenidos


#Autor:Catriel Cabrera
#su codigo

"""
import time
print("Cabrera")
print(time.strftime("%d/%m/%y - %H:%M:%S")) #Formato de 24 horas 

g = 0
r = 0
h = 0
s = 0

opcion1 = int(input("Te gusta el amanecer (1) o el anochecer (2)?: "))

if opcion1 == 1:
    g+=1
    r+=1
elif opcion1 == 2:
    h+=1
    s+=1
else:
    print("Opción invalida")

opcion2 = int(input("¿Como queres que te recuerden cuando mueras?: 1-Bueno,2-Grande,3-Audaz,4-Sabio: "))

if opcion2 == 1:
    h+=2
elif opcion2 == 2:
    s+=2
elif opcion2 == 3:
    r+=2
elif opcion2 == 4:
    g+=2
else:
    print("Opción invalida")

opcion3 = int(input("¿Que instrumento te gusta más?: 1-violin,2-Trompeta,3-Piano,4-Tambor: "))

if opcion3 == 1:
    s+=4
elif opcion3 == 2:
    h+=4
elif opcion3 == 3:
    r+=4
elif opcion3 == 4:
    g+=4
else:
    print("Opción invalida")

# Casa ganadora

if g > r and g > s and g > h:
    print("Gryffindor ganó con ",g," puntos")
elif h > r and h > s and h > g:
    print("Hufflepuff ganó con ",h," puntos")
elif s > r and s > h and s > g:
    print("Slytherin ganó con ",s," puntos")
elif r > s and r > g and r > h:
    print("RavenClaw ganó con ",r," puntos")
else:
    print("Hubo un empate")