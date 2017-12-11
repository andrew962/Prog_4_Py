from flask import Flask
from flask import render_template,redirect,request,url_for,session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MascotasDB.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtAfertA'
db = SQLAlchemy(app)

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(20),unique = True)
#     pets = db.relationship('Pet', backref = 'owner', lazy = 'dynamic')
#     def __init__(self,name = None):
#         self.name = name
#
# class Pet(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(20))
#     owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#
# try:
#     # r = Person.query.filter_by(name='lalo').first()
#     # print(r)
#     # print(r.pets.all())
#     # for i in r.pets.all():
#     #     print(i.name)
#     person = input('Nombre: ')
#     mascota = input('Mascota: ')
#     nueva_person = Person(name=person)
#     nueva_mascota = Pet(name = mascota, owner = nueva_person)
#     db.session.add(nueva_person)
#     db.session.add(nueva_mascota)
#     db.session.commit()
# #---------------------------------------------------------------------------------------------------------------#
#     # person_four = Person(name='Jose')
#     # pet_four = Pet(name='lolo', owner = person_four)
#     # db.session.add(person_four)
#     # db.session.add(pet_four)
#     # db.session.commit()
# #---------------------------------------------------------------------------------------------------------------#
#except Exception as e:
#    print(e)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address', backref='person', lazy='dynamic')
    def __init__(self,name):
        self.name = name

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),nullable=False)

name = input('Nombre: ')
correo = input('Correo: ')
try:
    nuevo_nombre = Person(name=name)
    nuevo_correo= Address(email = correo, person= nuevo_nombre)
    db.session.add(nuevo_nombre)
    db.session.add(nuevo_correo)
    db.session.commit()
except Exception as e:
    print(e)

if __name__ == '__main__':
    try:
        db.create_all()
    except Exception as a:
        print(a)
        print('Tabla ya creada')