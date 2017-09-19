import sqlite3
import hashlib

#para guardar todo en memoria y no guardarlo en disco usamos :memory:
#db = sqlite3.connect(':memory:') #DB en Memoria



def cifrar_pass(passw):
    cifrado = hashlib.sha512(passw.encode('utf-8')).hexdigest()
    return cifrado

db = sqlite3.connect('data/prueba') #DB en Disco
db.create_function('cifrar', 1, cifrar_pass)
cursor = db.cursor()
cursor.execute('''CREATE TABLE clave(ID INT PRIMARY KEY,EMAIL TEXT UNIQUE, PASS TEXT)''')

user = input('Usuario: ')
passw = input('contraseña: ')

cursor.execute('''INSERT INTO clave(EMAIL, PASS) VALUES(?,cifrar(?))''', (user, passw))
db.commit()

#-------------------------------------------------------------------------------------------------------------------#

#cursor.execute('''SELECT ID,NOMBRE FROM usuario''')
# resultado = cursor.fetchall()
# for fila in resultado:
#     print("{0} : {1}" .format(fila[0],fila[1]))
#
# ID = input("ID de usuario a cambiar: ")
# for fila in resultado:
#     if int(ID) == int(fila[0]):
#         nuevo_nombre = input('Nombre nuevo: ')
#         cursor.execute('''UPDATE usuario SET nombre = ? WHERE id = ?''',(nuevo_nombre,ID))
#         db.commit()
#

#-------------------------------------------------------------------------------------------------------------------#

# def creation():
#      return cursor.execute('''CREATE TABLE usuario(ID INTEGET PRIMARY KEY, NOMBRE TEXT,
#                         TELEFONO TEXT, EMAIL TEXT UNIQUE, PASS TEXT)''')
#
# def insert():
#     nom = input('Nombre: ')
#     tel = input('Telefono: ')
#     email = input('Email: ')
#     passw = input('Password: ')
#     cursor.execute('''INSERT INTO usuario(NOMBRE, TELEFONO, EMAIL, PASS) VALUES(?,?,?,?)''', (nom, tel, email, passw))
#     #cursor.execute('''INSERT INTO usuario(NOMBRE, TELEFONO, EMAIL, PASS) VALUES(:nom, :tel, :email, :passw)''', {'NOMBRE':nom, 'TELEFONO':tel,'EMAIL':email, 'PASS':passw})
#     db.commit()
#     db.close()  # Para cerrar la coneccion
#
# if __name__ == '__main__':
#     try:
#         creation()
#         insert()
#     except Exception as e:
#         print(e)
#         insert()
#     finally:
#         print('Tabla ya creada')


