import tkinter as tk
from tkinter import *
import sqlite3 as sq3
from tkinter import messagebox


def conectar():
    global con
    global cur
    con = sq3.connect('mi_db.db')  # creando la conexion
    cur = con.cursor()  # creando el vehiculo para transmitir info
    messagebox.showinfo("STATUS", "Conexión exitosa")


def salir():
    respuesta = messagebox.askquestion("CONFIRME", "¿Desea salir?")
    if respuesta == 'yes':
        # global con
        # con.close()
        raiz.destroy()


# Creamos para mostrar licencia:

def mostrar_licencia():
    msg = '''
    Este software fue desarollado por Catriel Cabrera todos los derechos reservados
    '''
    messagebox.showinfo("STATUS", msg)


def mostrar_acerca_de():
    messagebox.showinfo("ACERCA DE...",
                        "Creado por Catriel Cabrera para CodoACodo En Julio 2023")


def limpiar():
    legajo.set("")
    apellido.set("")
    nombre.set("")
    email.set("")
    calificacion.set("")
    escuela.set("")
    localidad.set("")
    provincia.set("")


def buscar_escuelas(crear_registro):
    con = sq3.connect("mi_db.db")
    cur = con.cursor()

    # Analizando la rama verdadera (crear)
    if crear_registro:
        cur.execute(
            'SELECT id,localidad,provincia FROM escuelas WHERE nombre = ?', (escuela.get(), ))
    # Rama del faslo (actualizar)
    else:
        cur.execute('SELECT nombre FROM escuelas')
    # obtiene una lista con tuplas que tienen los resultados de la QUERY
    resultado = cur.fetchall()
    retorno = []
    for elemento in resultado:
        if crear_registro:
            localidad.set(elemento[1])
            provincia.set(elemento[2])
        # toma el primer elemento de la tupla q es la escuela
        retorno.append(elemento[0])
    con.close()
    return retorno


def setear_prov_local(evento):
    con = sq3.connect("mi_db.db")
    cur = con.cursor()
    cur.execute(
        'SELECT localidad,provincia FROM escuelas WHERE nombre = ?', (escuela.get(), ))
    resultado = cur.fetchall()
    localidad.set(resultado[0][0])
    provincia.set(resultado[0][1])


def crear():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = (id_escuela, legajo.get(), apellido.get(),
             nombre.get(), calificacion.get(), email.get())
    cur.execute(
        'INSERT INTO alumnos(id_escuela,legajo,apellido,nombre,nota,email) VALUES (?,?,?,?,?,?)', datos)
    con.commit()
    messagebox.showinfo("Status", "Registro agregado")
    limpiar()


def buscar():
    query_buscar = ''' SELECT alumnos.legajo , alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, 
    escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela
     = escuelas.id WHERE alumnos.legajo =  '''

    cur.execute(query_buscar+legajo.get())  # concateno string query con legajo
    resultado = cur.fetchall()
    if resultado == []:
        messagebox.showerror("ERROR", "N° Legajo inexistente")
        legajo.set("")
    else:
        nombre.set(resultado[0][1])
        apellido.set(resultado[0][2])
        calificacion.set(resultado[0][3])
        email.set(resultado[0][4])
        escuela.set(resultado[0][5])
        localidad.set(resultado[0][6])
        provincia.set(resultado[0][7])
        #legajo_input.config(state='disabled')


def actualizar():
    id_escuela = int(buscar_escuelas(True)[0])
    datos = id_escuela, apellido.get(), nombre.get(), calificacion.get(), email.get()
    cur.execute("UPDATE alumnos SET id_escuela = ?, apellido = ?, nombre = ?, nota = ?, email = ? WHERE legajo = " 
    + legajo.get(), datos)
    con.commit()
    messagebox.showinfo("STATUS", "Registro actualizado")
    limpiar()


def eliminar():
    resp = messagebox.askquestion("BORRAR","¿Desea borrar el registro?")
    if resp == 'yes':
        cur.execute("DELETE FROM alumnos WHERE legajo=" + legajo.get())
        con.commit()
        messagebox.showinfo("STATUS","Registro eliminado")
        limpiar()

    


# Creando el contenedor padre llamado raíz
raiz = tk.Tk()

# Creamos un titulo en el contenedor raíz

raiz.title("GUI - comisión 23219")


barra_menu = tk.Menu(raiz)  # Instanciamos un objeto del tipo barra menu
raiz.config(menu=barra_menu)  # Le indico a la raiz que coloque una barra menu

# Creamos 4 botones contenidos dentro de la barra_menu
# Instanciamos 4 objetos del tipo Menu

bbdd_menu = tk.Menu(barra_menu, tearoff=False)
graficas_menu = tk.Menu(barra_menu, tearoff=False)
limpiar_menu = tk.Menu(barra_menu, tearoff=False)
ayuda_menu = tk.Menu(barra_menu, tearoff=False)


# Creo las opciones que va a tener el menu

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Gráficas", menu=graficas_menu)
barra_menu.add_cascade(label="Limpiar", menu=limpiar_menu)
barra_menu.add_cascade(label="Acerca de ", menu=ayuda_menu)

# Agregando opciones al boton BBDD

bbdd_menu.add_command(label="Conectar a BBDD", command=conectar)
bbdd_menu.add_command(label="Listado de alumnos")
bbdd_menu.add_command(label="Salir", command=salir)

# Agregando opciones al boton graficas

graficas_menu.add_command(label="Alumnos por escuela")
graficas_menu.add_command(label="Calificaciones")

# Agregando opciones al boton limpiar

limpiar_menu.add_command(label="Limpiar campos", command=limpiar)

# Agregando opciones al boton ayuda

ayuda_menu.add_command(label="Licencia", command=mostrar_licencia)
ayuda_menu.add_command(label="Acerca de...", command=mostrar_acerca_de)

# ------------ FRAME CAMPOS -----------------------

frame_campos = tk.Frame(raiz)  # me devuelve un object del tipo frame
frame_campos.pack()  # Es para activar

'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

# Apunte: posicionamiento de elemento en tkinter:https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/

# label para legajo
legajo_label = Label(frame_campos, text='Nº Legajo')
legajo_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

# label para apellido
apellido_label = Label(frame_campos, text='Apellido')
apellido_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

# label para nombre
nombre_label = Label(frame_campos, text='Nombre')
nombre_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

# label para Email
legajo_email = Label(frame_campos, text='Email')
legajo_email.grid(row=3, column=0, sticky='e', padx=10, pady=10)

# label para promedio
legajo_promedio = Label(frame_campos, text='Promedio')
legajo_promedio.grid(row=4, column=0, sticky='e', padx=10, pady=10)

# label para escuela
legajo_escuela = Label(frame_campos, text='Escuela')
legajo_escuela.grid(row=5, column=0, sticky='e', padx=10, pady=10)

# label para localidad
legajo_localidad = Label(frame_campos, text='Localidad')
legajo_localidad.grid(row=6, column=0, sticky='e', padx=10, pady=10)

# label para provincia
legajo_provincia = Label(frame_campos, text='Provincia')
legajo_provincia.grid(row=7, column=0, sticky='e', padx=10, pady=10)

# Agregando Entry:

legajo = StringVar()
apellido = StringVar()
nombre = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()


# Agregando los Entry()

legajo_input = Entry(frame_campos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

apellido_input = Entry(frame_campos, textvariable=apellido)
apellido_input.grid(row=1, column=1, padx=10, pady=10)

nombre_input = Entry(frame_campos, textvariable=nombre)
nombre_input.grid(row=2, column=1, padx=10, pady=10)

email_input = Entry(frame_campos, textvariable=email)
email_input.grid(row=3, column=1, padx=10, pady=10)

calificacion_input = Entry(frame_campos, textvariable=calificacion)
calificacion_input.grid(row=4, column=1, padx=10, pady=10)


# escuela_input = Entry(frame_campos, textvariable=escuela)
# escuela_input.grid(row=5, column=1, padx=10, pady=10)

# Lista de escuelas vacias posteriormente las obtendremos haciendo
# escuelas = [(),()]
# un Query a la base de datos

# obtengo el nombre de todas las escuelas de mi tabla escuelas
escuelas = buscar_escuelas(False)
escuela.set('Seleccione una escuela')

escuela_option = OptionMenu(frame_campos, escuela,
                            *escuelas, command=setear_prov_local)
escuela_option.grid(row=5, column=1, padx=10, pady=1, sticky='w', ipadx=50)

localidad_input = Entry(frame_campos, textvariable=localidad)
localidad_input.grid(row=6, column=1, padx=10, pady=10)

provincia_input = Entry(frame_campos, textvariable=provincia)
provincia_input.grid(row=7, column=1, padx=10, pady=10)

# Creamos los botones (no son label ni entry tienen otra estructura)

# Frame CRUD:

frame_botones = Frame(raiz)
frame_botones.pack()

boton_crear = Button(frame_botones, text="Crear", command=crear)
boton_crear.grid(row=0, column=0, padx=10, pady=10)

boton_leer = Button(frame_botones, text="Leer", command=buscar)
boton_leer.grid(row=0, column=1, padx=10, pady=10)

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar)
boton_actualizar.grid(row=0, column=2, padx=10, pady=10)

boton_borrar = Button(frame_botones, text="Borrar", command=eliminar)
boton_borrar.grid(row=0, column=3, padx=10, pady=10)

# Frame del pie

frame_pie = Frame(raiz)
frame_pie.pack()

pie_label = Label(
    frame_pie, text="(2023) por Catriel Cabrera para CaC 4.0 - Big Data")
pie_label.grid(row=0, column=0, padx=10, pady=10)

raiz.mainloop()  # me permite mantener la ventana abierta
