import sqlite3 as sq3  # importaria la libreria sqlite

con = sq3.connect('mi_db.db') # creando la conexion
cur = con.cursor() # creando el vehiculo para transmitir info

query1 = '''SELECT alumnos.legajo, alumnos.apellido, alumnos.nombre, alumnos.nota, alumnos.email, 
escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos 
INNER JOIN escuelas ON alumnos.id_escuela = escuelas.id LIMIT 5'''

query2 = ''' SELECT * FROM escuelas'''

for registro in cur.execute(query1) :
    print(registro)

for registro in cur.execute(query2) :
    print(registro)




#con.commit()
con.close()