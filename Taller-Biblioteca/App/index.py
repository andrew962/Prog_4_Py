import sqlite3,os

db = sqlite3.connect('DB/data_biblioteca')
cursor = db.cursor()

def creation():
    return cursor.execute('''CREATE TABLE LIBRO(ID INTEGER PRIMARY KEY, AUTOR TEXT,TITULO TEXT, PUBLICACION TEXT)''')

def insert():
    autor = input('Nombre del Autor: ')
    libro = input('Nombre del Libro: ')
    public = input('Fecha de Publicación DD/MM/AA: ')
    cursor.execute('''INSERT INTO LIBRO(AUTOR,TITULO,PUBLICACION) VALUES(?,?,?)''',(autor,libro,public))
    db.commit()

def borrar():
    try:
        borr = input('Borrar Autor por si ID: ')
        cursor.execute("""DELETE FROM LIBRO WHERE ID = ? """,(borr))
        db.commit()
    except Exception as e:
        print(e)

def listar():
    os.system("clear")
    cursor.execute('''SELECT ID,AUTOR,TITULO FROM LIBRO''')
    resul = cursor.fetchall()
    print('     Autor       Titulo.')
    for fila in resul:
        print('{0}. {1}          {2}'.format(fila[0],fila[1],fila[2]))

def consultar():
    try:
        con = input('Traer todos los resultados con la Primera letra')
        cursor.execute('''SELECT * FROM LIBRO WHERE AUTOR like ?''',(con))
        resul = cursor.fetchall()
        for fila in resul:
            print('{0}'.format(fila[0]))
    except Exception as e:
        print(e)


def menu():
    os.system("clear")
    num = True
    while num != False:
        num = input('Menu de OPCIONES \n1. Agregar\n2. Borrar\n3. Listar'
                    '\n4. Consultar\nCualquier letra para Salir\n-->')
        if num == '1':
            insert()

        elif num == '2':
            borrar()

        elif num == '3':
            listar()

        elif num == '4':
            consultar()

        else:
            num = False
