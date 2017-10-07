from sqlalchemy import *
from sqlalchemy.orm import create_session, mapper

db = create_engine('sqlite:///Clase4.db')
db.echo = True #esto evita que la salida de los datos sea por consola

metadata = MetaData(db)

usuarios = Table('usuarios', metadata, autoload = True)
correos = Table('correos', metadata, autoload = True)

sesion = create_session()

class User(object):
    def __init__(self, nombre=None, edad=None, passw=None):
        self.nombre = nombre
        self.edad = edad
        self.passw = passw

    def __repr__(self):
        return self.nombre

class Correo(object):
    def __init__(self,dirreccion=None):
        self.dirrecion = dirreccion
    def __repr__(self):
        return self.dirrecion

correomapper = mapper(correos, Correo)
usuariomapper = mapper(User, usuarios, properties = {
    'correo' : relation(correomapper),
})

usuarios = sesion.query(User).all()
correos = sesion.query(Correo).Count()

for usuario in usuarios:
    print(usuario)
print('Tenemos ' + )


#-----------------------------------------------------------------------------------------#

# usuarios = Table('usuarios', metadata,
#                  Column('usuario_id', Integer, primary_key=True),
#                  Column('nombre', String(30)),
#                  Column('edad', Integer),)
# usuarios.create()
#
# correos = Table('correos', metadata,
#                 Column('correo_id', Integer, primary_key=True),
#                 Column('dirreccion', String),
#                 Column('usuario_id', Integer, ForeignKey('usuarios.usuario_id')),)
# correos.create()
#
# i = usuarios.insert()
# i.execute(
#     {'nombre': 'Petra', 'edad': 50},
#     {'nombre': 'Juana', 'edad': 45},
#     {'nombre': 'Xenobia', 'edad': 17},
#     {'nombre': 'Tinoca', 'edad': 25},
# )
#
# i = correos.insert()
# i.execute(
#     {'direccion': 'petra@.com', 'usuario_id': 1},
#     {'direccion': 'juana@nidea.com', 'usuario_id': 2},
#     {'direccion': 'juana@ejemplo.com', 'usuario_id': 2},
#     {'direccion': 'xndb@.com', 'usuario_id': 3},
# )
#
# def ejecutar(stnc):
#     rs = stnc.execute()
#     for fila in rs:
#         print(fila)
#
# s = select([usuarios, correos], correos.c.usuario_id == usuarios.c.usuario_id)
# ejecutar(s)

# s = select([usuarios.c.nombre, correos.c.dirrecion], correos.c.usuario_id == usuarios.c.usuario_id)
# ejecutar(s)
#
# s = join(usuarios, correos).select() # este trae la data que es igual en el ID
# ejecutar(s)
#
# s = outerjoin(usuarios, correos).select()
# ejecutar(s)

#-----------------------------------------------------------------------------------------#

# usuarios = Table('usuarios', metadata, autoload = True)
#
# def ejecutar(stnc):
#     rs = stnc.execute()
#     for fila in rs:
#         print(fila)
#
# s = usuarios.select(usuarios.c.nombre == 'Juan')
# ejecutar(s)
# s = usuarios.select(usuarios.c.edad < 30)
# ejecutar(s)
# s = usuarios.select(and_(usuarios.c.edad < 35, usuarios.c.nombre != 'Tiene'))
# ejecutar(s)
# s = usuarios.select(or_(usuarios.c.edad < 35, usuarios.c.nombre != 'Petra'))
# ejecutar(s)
# s = usuarios.select((usuarios.c.edad < 35) & (usuarios.c.nombre != 'Hambre'))
# ejecutar(s)
# s = usuarios.select((usuarios.c.edad < 35) | (usuarios.c.nombre != 'Hambre'))
# ejecutar(s)
# s = usuarios.select(usuarios.c.nombre.startswith('P'))
# ejecutar(s)
# s = select([func.count('*')], from_obj = [usuarios])
# ejecutar(s)

#-----------------------------------------------------------------------------------------#

# usuarios = Table('usuarios', metadata,
#                  Column('id', Integer, primary_key=True),
#                  Column('nombre', String(30)),
#                  Column('edad', Integer),
#                  Column('password', String),)
#
# usuarios.create()
#
# #insercion de Datos
# try:
#     i = usuarios.insert()
#     i.execute(nombre = 'Petra', edad = 50, passw = 'ella')
#     i.execute({'nombre': 'Juan', 'edad': 17},
#             {'nombre': 'No', 'edad': 20},
#             {'nombre': 'Hambre', 'edad': 23})
# except Exception as e:
#     print(e)
#
# #BUSQUEDA DE DATOS
#
# s = usuarios.select()
# rs = s.execute()
# fila = rs.fetchone()
# print('ID           |', fila[0])
# print('Nombre       |', fila['nombre'])
# print('Edad         |', fila.edad)
# print('Contraseña   |', fila[usuarios.c.password])
#
# for fila in rs:
#     print(fila.nombre, 'Tiene', fila.edad, 'años.')